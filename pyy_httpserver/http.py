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

from pyy_web import httprequest, httpresponse

def httptime(t=None):
  fmt = '%a, %d %b %Y %H:%M:%S GMT' # http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3.1
  if isinstance(t, str):
    return datetime.datetime.strptime(t, fmt)
  if isinstance(t, float):
    return time.strftime(fmt, t)
  return datetime.datetime.utcnow().strftime(fmt)

class HTTPError(Exception): pass

CRLF = '\r\n'



class httphandler(object):
  def __init__(self, server, conn, handler):
    self.server = server
    self.conn = conn
    self.handler = handler
    
    try:
      while self.conn.status:
        self.do_request()
    except EOFError:
      # client closed the connection
      pass
    except Exception, e:
      import traceback
      traceback.print_exc()

  def do_request(self):
    req     = None
    res     = None
    error   = None
    finish  = None

    try:
      req = self.parse_request()
      self.validate_request(req)
      res = httpresponse()
      finish = self.handler.handle(self, req, res)

    except Exception, e:
      try: raise
      except HTTPError, e:
        error = e.args
      except EOFError:
        raise
      except Exception, e:
        error = (500, e)
      res = httpresponse()
      res.status = error[0]
      res.body = '%s %s' % (res.status, res.statusmsg)
      try:
        self.handler.handle_error(self, req, res, error[0], *error[1:])
      except:
        res = httpresponse()
        res.status = 500
        res.body = '%s %s' % (res.status, res.statusmsg)
        import traceback
        traceback.print_exc()

    self.make_response(req, res)
    self.write_response(res)

    if finish:
      try:
        finish()
      except:
        # we already sent out the response+headers,
        # nothing to tell the client at this point
        import traceback
        traceback.print_exc()
    self.finish_response(res)

    
  def parse_request(self):
    '''
    reads one request from the client and returns it
    '''
    req = httprequest()

    def read(bytes=None):
      cl = int(req.headers.get('Content-Type','0'))
      if not cl: return ''
      return self.conn.read(cl)
        
    req.read = read
    
    self.readline = self.readrequest
    self._lines = ['']
    while hasattr(self, 'readline'):
      self.readline(req, self.next_line())
    return req
    
  def next_line(self):
    if len(self._lines[-1]) > 512*1024:
      raise HTTPError(414) # don't let malicious users use up all the memory
    
    while len(self._lines) < 2:
      data = self._lines.pop() + self.conn.read()
      self._lines.extend(data.split(CRLF))

    return self._lines.pop(0)
    
  def readrequest(self, request, line):
    if not line: return
    try:
      method, uri, http = line.split(' ')
    except ValueError: raise HTTPError(400)
    request.method = method
    request.uri = uri
    if   http == 'HTTP/1.0':
      request.http = 1.0
    elif http == 'HTTP/1.1':
      request.http = 1.1
    else:
      raise HTTPError(505)
    
    self.readline = self.readheader

  def readheader(self, request, line):
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
    self.conn.readbuffer[0:0] = self._lines
    del self._lines
  
  def make_response(self, req, res):
    '''
    create a response object based on the request
    '''
    if not res.http:
      try:
        res.http = req.http
      except:
        res.http = 1.1

    if not res.status:
      res.status = 200
    res.headers.setdefault('Server', 'pyy-httpserver-test')
    res.headers.setdefault('Content-Type', 'text/plain; charset=ISO-8859-4')
    res.headers.setdefault('Date', httptime())

    # http://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html#sec8.1.2
    # default should be to keep the connection open, but this is easier for testing
    res.headers.setdefault('Connection', 'close')
     
    if req:
      for k, v in req.headers.iteritems():
        if   k == 'User-Agent': pass
        elif k == 'Host':       pass
        elif k == 'Referer':    pass
        elif k == 'Accept':     pass
        elif k == 'Accept-Language':  pass
        elif k == 'Accept-Charset':   pass
        elif k == 'Accept-Encoding':
          if not res.body: continue
          tokens = v.lower().split(',')
          len1 = len(res.body)
          if 'deflate' in tokens: # zlib is better
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
            res.body = ss.getvalue()
            len2 = len(res.body)
            res.headers['Content-Encoding'] = 'gzip'


          else: # unsupported encoding
            res.headers.setdefault('Content-Encoding', 'identity')
            continue

          res.headers['Content-Length'] = len2
          print 'compressed response to %d/%s (%2.0f%%) %s' % (len2, len1, 100.*len2/len1, tokens)

        elif k == 'Connection':
          if v == 'keep-alive':
            res.headers['Connection'] = v
          else:
            warnings.warn('Unknown Connection token: %s' % v)

        elif k == 'Keep-Alive':
          pass
        
        else:
          warnings.warn('Unhandled request header: %s: %s' % (k,v))
    
    if res.body is None:
      res.body = ''
    
    res.headers.setdefault('Content-Length', len(res.body))
   
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
    
  def finish_response(self, res):
    '''
    clean up a response. (close the connection if required)
    '''
    con = res.headers.get('Connection')
    if con is None:
      self.conn.close()
    elif con == 'close':
      self.conn.close()
    elif con == 'keep-alive':
      if res.headers.get('Content-Length') is None:
        raise Exception('tried to keep-alive with no C-L')
    else:
      raise Exception('unknown Connecton: token')

  def validate_request(self, req):
    if req.http == 1.1:
      if not 'Host' in req.headers:
        raise HTTPError(400)
      
