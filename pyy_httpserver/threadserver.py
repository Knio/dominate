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

'''

This module implements a threaded socket server

'''

import socket
import threading
import time

class connection(object):
  '''
  A connection object. Wraps socket

  Public API:

  .read(n)      returns n bytes
  .write(data)  writes data
  .close([how]) closes the socket

  .unread(data) pushes data back onto read buffer
  '''


  OPEN = 1
  CLOSED = 0

  def __init__(self, server, sock, addr):
    self.server   = server
    self.addr     = addr
    self.sock     = sock

    self.readbuffer  = []

    self.status = connection.OPEN

  def fileno(self):
    return self.sock.fileno()

  def read(self, n=None):
    if not n:
      if self.readbuffer:
        data = ''.join(self.readbuffer)
        self.readbuffer = []
        return data

      else:
        while 1:
          try:
            data = self.sock.recv(1024*1024)
            if data == '':
              self.status = connection.CLOSED
              raise EOFError()
            return data
          except socket.error, e:
            # resource temp unavailable
            if e.args[0] == 11: time.sleep(0.1)
            else: raise


    while sum(map(len, self.readbuffer)) < n:
      try:
        data = self.sock.recv(1024*1024)
        if data == '':  raise EOFError()
        self.readbuffer.append(data)
      except socket.error, e:
        # resource temp unavailable
        if e.args[0] == 11: time.sleep(0.1)
        else: raise

    data = ''.join(self.readbuffer)

    self.readbuffer = [data[n:]]
    return data[:n]

  def write(self, data):
    while data:
      try:
        data = data[self.sock.send(data):]
      except socket.error, e:
        # resource temp unavailable
        if e.args[0] == 11: time.sleep(0.1)
        else: raise


  def close(self, how=socket.SHUT_RDWR):
    self.sock.shutdown(how)
    self.sock.close()
    self.status = 0

  def unread(self, data):
    self.readbuffer[0:0] = [data]


class server(object):
  '''
  A socket server

  .listen(addr, handler, *a, **kw)

  Listen on addr. When a connetion is accepted,
  call handler(server, connection, *a, **kw)
  '''


  def __init__(self):
    self.listenthreads = []
    self.done = False

  def listen(self, addr, handler, *args, **kwargs):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(1.0)
    sock.bind(addr)
    sock.listen(5)

    def listen():
      while not self.done:
        try:
          newsock, newaddr = sock.accept()
        except socket.timeout:
          time.sleep(0.1)

        else:
          newsock.settimeout(5.0)
          conn = connection(self, newsock, newaddr)

          def handle():
            try:
              handler(self, conn, *args, **kwargs)
            finally:
              newsock.close()

          def profile():
            h = handle
            import cProfile as profile
            profile.runctx("h()", globals(), locals())

          thread = threading.Thread(target=handle)
          thread.daemon = True
          thread.start()

    listenthread = threading.Thread(target=listen)
    listenthread.start()
    self.listenthreads.append(listenthread)
    print('Listening on %r' % (addr,))

  def quit(self):
    if self.done: return
    print('Quitting server')
    self.done = True

  def run(self):
    try:
      while not self.done:
        time.sleep(5.0)

    finally:
      self.quit()

def main():
  '''
  Sample echo server
  '''

  def echo(serv, conn):
    while 1:
      conn.write(conn.read())

  s = server()
  s.listen(('',1234), echo)
  s.run()

if __name__ == '__main__':
  main()




