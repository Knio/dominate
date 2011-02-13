__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy.  If not, see
<http://www.gnu.org/licenses/>.
'''

import stackless
import socket
import select
import threading
import time

class connection(object):
  READABLE = 1
  WRITABLE = 2
  OPEN = 1

  def __init__(self, server, sock, addr):
    self.server   = server
    self.addr     = addr
    self.sock     = sock
    self.handler  = None

    self.readbuffer  = []
    self.writebuffer = []

    self.readchannel  = stackless.channel()
    self.writechannel = stackless.channel()

    self.status = connection.OPEN

  def fileno(self):
    return self.sock.fileno()

  def onreadable(self):
    if not self.status: return
    try:
      data = self.sock.recv(256*1024)
    except socket.error, e:
      if  e.args[0] == 10053  or \
          e.args[0] == 10054  or \
          e.args[0] == 9      or \
          e.args[0] == 105    or \
          e.args[0] == 104:         # Connection reset by peer
        #print 'Client %s closed the connection' % (self.addr,)
        self.onclose(e)
        return
      if e.args[0] == 10035:  # would have blocked
        return
      if e.args[0] == 11:     # resource temp unavailable
        return
      else: raise

    if data == '':
      # TODO
      # This happens when the client sent a FIN.
      # It might still be listening for data, however!
      #print 'Client %s closed the connection' % (self.addr,)
      self.onclose()
      return

    # print '%s GOT DATA: %r' % (self.addr, data)
    self.readbuffer.append(data)
    if self.handler and self.handler.hasattr('ondata'):
      self.handler.ondata(data)

    # is someone waiting on read?
    if self.readchannel.balance < 0:
      self.readchannel.send(None)

  def onwritable(self):
    if not self.status: return
    while self.writebuffer:
      d = self.writebuffer[0]
      o = d
      #print '%s SENDING: %r' % (self.addr, d[:80])

      try:
        while d:
          d = d[self.sock.send(d):]
          self.writebuffer[0] = d
        self.writebuffer.pop(0)
        self.writechannel.send(o)

      except socket.error, e:
        if e.args[0] == 10053:  # closed the connection
          self.onclose(e)
          return
        if e.args[0] == 10035:  # would have blocked
          return
        if e.args[0] == 11:     # resource temp unavailable
          return
        else: raise

    self.server.set_writable(self, False)

  def onclose(self, e=None):
    if not self.status: return # we closed already
    while self.readchannel.balance < 0:
      self.readchannel.send_exception(EOFError, EOFError('connection reset', e))
    while self.writechannel.balance < 0:
      self.writechannel.send_exception(EOFError, EOFError(e))

    self.server.close(self)
    self.status = 0
    if self.handler and self.handler.hasattr('onclose'):
      self.handler.onclose()

  def write(self, data):
    if not self.status:
      raise EOFError('write on closed connection')
    assert type(data) == str
    #print 'WRITE: %r' % data[:80]
    self.writebuffer.append(data)
    self.server.set_writable(self)
    # block until it sent
    r = self.writechannel.receive()
    #assert data == r, (len(data), len(r), data[:80], r[:80])
    assert data.endswith(r) # this is not a very strong check, but
                            # the one above fails when the loop on
                            # line 87 is interrupted and o != data
                            # on the next onwritable() call
    return r

  def read(self, x=None):
    if not self.status:
      raise EOFError('read on closed connection')
    if not any(self.readbuffer):
      self.server.set_readable(self)
      # block until data availible
      self.readchannel.receive()
    data = ''.join(self.readbuffer)
    self.readbuffer = x and [data[x:]] or []
    return data[:x]

  def close(self, how=socket.SHUT_RDWR):
    #print 'CLOSING: %s' % (self.addr,)
    if self.writebuffer:
      #self.write('')
      raise Exception('attempt to close connection with unsent data', self.writebuffer)
    self.sock.shutdown(how)
    self.sock.close()
    self.onclose()


class listener(connection):
  def __init__(self, server, sock, addr, handler, *args):
    connection.__init__(self, server, sock, addr)
    self.handler  = handler
    self.args     = args
    self.server.set_readable(self)

  def onreadable(self):
    while 1:
      try:
        sock, addr = self.sock.accept()
      except socket.error, e:
        if e.args[0] == 10035: # would have blocked
          return
        if e.args[0] == 11:     # resource temp unavailable
          return
        else: raise

      sock.setblocking(0)
      conn = connection(self.server, sock, addr)
      self.server.requests.add(conn)
      handler = stackless.tasklet(self.handler)(self.server, conn, *self.args)
      #print 'Accepted connection: %s' % (addr,)


class handler(object):
  def __init__(self, server, conn, *args):
    self.conn = conn
    self.server = server


class server(object):
  def __init__(self):
    self.listeners = []
    self.requests  = set()
    self.readable  = set()
    self.writable  = set()
    self.selectch  = stackless.channel()
    self.done      = False

  def listen(self, addr, handler, *args):
    sock = socket.socket()
    sock.setblocking(0)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(addr)
    sock.listen(100)
    self.listeners.append(listener(
      self, sock, addr, handler, *args))
    print 'Listening on %s' % (addr,)

  def set_readable(self, req, x=True):
    if x: self.readable.add(req)
    else: self.readable.discard(req)
    if x: self.interrupt()

  def set_writable(self, req, x=True):
    if x: self.writable.add(req)
    else: self.writable.discard(req)
    if x: self.interrupt()

  def close(self, req):
    self.readable.discard(req)
    self.writable.discard(req)
    self.requests.discard(req)

  def interrupt(self):
    if self.selectch.balance < 0:
      self.selectch.send(([],[],[]))

  def select(self, timeout):
    if timeout==0:
      r, w, e = select.select(
        self.readable, self.writable, [], timeout)

      return r, w, e

    def thread():
      r = select.select(
        self.readable, self.writable, [], timeout)
      #if self.selectch.balance < 0: # this causes stackless to crash!
      self.selectch.send(r)

    threading.Thread(target=thread).start()

    r = self.selectch.receive()
    while self.selectch.balance > 0:
      r2 = self.selectch.receive()
      map(lambda x:reduce(list.extend,x) ,zip(r,r2))
    return r

  def tick(self, timeout=None):
    readable, writable, _e = self.select(timeout)

    for i in readable:
      i.onreadable()

    for i in writable:
      i.onwritable()

  def run(self, timeout=None):
    def mainloop():
      try:
        while 1:
          self.tick(timeout)
          stackless.schedule()
          time.sleep(0.05)
      except KeyboardInterrupt: pass
      finally:
        self.quit(timeout)

    stackless.tasklet(mainloop)()
    stackless.run(threadblock=True)

  def quit(self, timeout):
    self.done = True
    print 'Quiting'
    time.sleep(timeout or 0)
    while self.selectch.balance > 0:
      self.selectch.receive()

def main():
  s = server()
  s.listen(('',1234), handlers.echohandler)
  s.run()

if __name__ == '__main__':
  main()



