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

# http://www.w3.org/Protocols/rfc2616/rfc2616.html
import warnings
import time
import datetime
import socket

from pyy.web import httprequest, httpresponse, httperror

def httptime(t=None):
  fmt = '%a, %d %b %Y %H:%M:%S GMT' # http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3.1
  if isinstance(t, str):
    return datetime.datetime.strptime(t, fmt)
  if isinstance(t, float):
    return time.strftime(fmt, t)
  return datetime.datetime.utcnow().strftime(fmt)

CRLF = '\r\n'

class endconnection(EOFError): pass

class httphandler(object):
  '''
  httphandler class

  httphandler(conn, handler)
    conn - an object that supports blocking
              .read([n])
              .unread(data)
              .write(data)
              .close()


    handler - http server confoguration object.
            will document later



    this class reads data from the connection,
    processes HTTP requests,
    lets handler handle them,
    and writes the results back over HTTP.

    Supports HTTP/1.1 and pipelining

  '''
  id = 0
  def __init__(self, conn, handler):
    self.conn = conn
    self.handler = handler

    self.conn.sock.settimeout(60.0)
    self.requests = 0
    self.id = httphandler.id
    httphandler.id += 1

    while self.conn.status:
      self.do_request()

  def do_request(self):
    req     = None
    res     = httpresponse()
    error   = None
    finish  = None
    self.requests += 1

    try:
      try:
        req = self.parse_request()
        self.validate_request(req)
        self.process_request(req)

        try:
          finish = self.handler.handle(self, req, res)
        except httperror:
          raise
        except Exception, e:
          error = (500, e)

      except endconnection:
        return

      except httperror, e:
        error = e.args

      if error:
        res = httpresponse()
        res.status = error[0]
        if (res.status <= 100) or (res.status in (204,304)) \
          or (req and req.method == 'HEAD'):
          # these messages cannot have a body
          pass
        else:
          res.body = '%s %s' % (res.status, res.statusmsg)
        try:
          self.handler.handle_error(self, req, res, error[0], *error[1:])
        except: # error handler had an error!
          res = httpresponse()
          res.status = 500
          res.body = '%s %s' % (res.status, res.statusmsg)
          import traceback
          traceback.print_exc()

      self.make_response(req, res, finish)
      self.write_response(res)

      if finish:
        try:   finish()
        except:
          # we already sent out the response+headers,
          # nothing to tell the client at this point
          import traceback
          traceback.print_exc()
          self.conn.close()

      self.finish_response(req, res)

    except IOError, e:
      print e
      self.conn.close()
      return

  def parse_request(self):
    '''
    reads one request from the client and returns it
    '''
    req = httprequest()

    # read the body of the HTTP message, or '' if the client
    # did not specify a C-L
    def read(bytes=None):
      l = cl = int(req.headers.get('Content-Length','0'))
      if not cl: return ''
      data = []
      while l:
        data.append(self.conn.read(l))
        l -= len(data[-1])
      data = ''.join(data)
      assert len(data) == cl, (len(data), cl)
      return data

    req.read = read

    self.readline = self.readrequest
    self._lines = ['']
    try:
      # check if there is a next line to so we can
      # gracefully handle socket closes.
      # we still want to throw an exception if the socket
      # closes when we are reading headers etc
      self._lines.insert(0, self.next_line())
    except EOFError:
      raise endconnection
    while hasattr(self, 'readline'):
      self.readline(req, self.next_line())
    return req

  def next_line(self):
    if len(self._lines[-1]) > 512*1024:
      raise httperror(414) # don't let malicious users use up all the memory

    while len(self._lines) < 2:
      data = self._lines.pop() + self.conn.read()
      self._lines.extend(data.split(CRLF))

    line = self._lines.pop(0)
    return line

  def readrequest(self, request, line):
    if not line: return
    try:
      method, uri, http = line.split(' ')
    except ValueError: raise httperror(400)
    request.method = method
    request.uri = uri
    if   http == 'HTTP/1.0':
      request.http = 1.0
    elif http == 'HTTP/1.1':
      request.http = 1.1
    else:
      raise httperror(505)

    self.readline = self.readheader

  def readheader(self, request, line):
    # TODO: headers can span lines! implement this
    if not line:
      return self.end_headers(request)

    key, val = line.split(':', 1)
    key = key.title()
    val = val.lstrip()

    if key in request.headers:
      #http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2
      val = request.headers[key] + ', ' + val
    request.headers[key] = val

  def end_headers(self, request):
    # we are done. clean up
    del self.readline
    # if we got extra data, push it back to the front of
    # the connection's read buffer, so someone can read() later
    # this is an abuse of the api because most file objects
    # wont support unread().
    # fix this later.
    last = self._lines.pop()
    l = [i + CRLF for i in self._lines] + [last]
    self.conn.unread(''.join(l))
    del self._lines

  def validate_request(self, req):
    host = req.headers.get('Host')
    if host:
      req.host = host.split(':')[0]
    else:
      req.host = None

    if req.http == 1.1 and not host:
      raise httperror(400)

  def process_request(self, req):
    if req.http == 1.1:
      if req.headers.get('Connection') != 'close':
        # get value from K-A header?
        # set K-A header?
        self.conn.sock.settimeout(300)

  def make_response(self, req, res, finish):
    '''
    create a response object based on the request
    '''
    if not res.http:
      try:     res.http = req.http
      except:  res.http = 1.1

    if not res.status:  res.status = 200
    res.headers.setdefault('Server', 'pyy-httpserver-test')
    res.headers.setdefault('Content-Type', 'text/plain; charset=ISO-8859-4')
    res.headers.setdefault('Date', httptime())

    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html#sec8.1.2
    # default should be to keep the connection open, but this is easier for testing
    res.headers.setdefault('Connection', 'keep-alive')

    if res.body is not None:
      res.body = str(res.body)

    s = []
    if req:
      for k, v in req.headers.iteritems():
        if   k == 'User-Agent': pass
        elif k == 'Host':       pass
        elif k == 'Referer':    pass
        elif k == 'Accept':     pass
        elif k == 'If-Modified-Since':  pass
        elif k == 'Accept-Language':    pass
        elif k == 'Accept-Charset':     pass
        elif k == 'Accept-Encoding':
          res.headers.setdefault('Content-Encoding', 'identity')
          if not res.body:             continue
          if not self.handler.compress:continue
          if not res.compress:         continue
          if finish:                   continue
          tokens = v.lower().split(',')
          len1 = len(res.body)
          if 'deflate' in tokens: # zlib is better, try it first
            if len1 < 32: continue
            import zlib
            res.body = zlib.compress(res.body, 9)
            len2 = len(res.body)
            res.headers['Content-Encoding'] = 'deflate'

          elif 'gzip' in tokens:
            len1 = len(res.body)
            if len1 < 64: continue
            # python's old libraries are retarded.
            # why can't there just be a compress(str) function?
            import gzip, cStringIO
            ss = cStringIO.StringIO()
            gz = gzip.GzipFile(compresslevel=9, mode='wb', fileobj=ss)
            gz.write(res.body)
            gz.flush()
            # end retardedness
            res.body = ss.getvalue()
            len2 = len(res.body)
            res.headers['Content-Encoding'] = 'gzip'

          else: # unsupported encoding. leave it as identity
            continue
            # [C-E] 'identity' ?

          res.headers['Content-Length'] = len2
          s.append('%d/%s (%2.0f%%)' % (len2, len1, 100.*len2/len1))

        elif k == 'Connection':
          if v == 'keep-alive':
            res.headers['Connection'] = v
          else:
            warnings.warn('Unknown Connection token: %s' % v)

        elif k == 'Keep-Alive':
          pass

        else:
          warnings.warn('Unhandled request header: %s: %s' % (k,v))

    if res.body is None:  res.body = ''

    lb = len(res.body)
    if not finish:
      cl = res.headers.get('Content-Length', lb)
      if cl != lb:
        raise Exception('Set C-L header (%d) that was not equal to '
          'response body (%d)' % (cl, lb))
      else:
        res.headers['Content-Length'] = lb

    print '[%d.%d] %d %s %s' % \
        (self.id, self.requests, res.statusnum, req and req.uri, ' '.join(s))
    return res

  def write_response(self, res):
    '''
    write the response object to the client.
    (but maybe not all the content)
    '''
    r = ['HTTP/%.1f %d %s' % (res.http, res.statusnum, res.statusmsg)]
    for k,v in res.headers.iteritems():
      r.append('%s: %s' % (k, v))
    r.append(CRLF)
    self.conn.write(CRLF.join(r))
    self.conn.write(res.body)

  def finish_response(self, req, res):
    '''
    clean up a response. (close the connection if required)
    '''
    con = res.headers.get('Connection')
    if con is None:
      if req.http == 1.0:
        self.conn.close()
    elif con == 'close':
      self.conn.close()
    elif con == 'keep-alive':
      if res.headers.get('Content-Length') is None:
        # TODO don't do this if Transfer-Encoding is chunked
        raise Exception('tried to keep-alive with no C-L')
    else:
      raise Exception('unknown Connecton: token')
