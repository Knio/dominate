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

import parsers

class httperror(Exception): pass

class httpmessage(object):
  def __init__(self):
    self.http    = 0
    self.headers = {}
    self.body    = None

class httprequest(httpmessage):
  def __init__(self):
    httpmessage.__init__(self)
    self.method = None
    self.uri    = None
    del self.body

  def read(self):
    raise NotImplementedError

  def _get(self):
    try:    get = self.uri.split('?', 1)[1]
    except: get = ''
    return parsers.parse_query(get)

  def _cookie(self):
    return parsers.parse_semi(self.headers.get('Cookie', ''))

  def _post(self):
    ct = self.headers.get('Content-Type','')
    if ct.startswith('multipart/form-data'):
      return parsers.parse_multipart(ct, self.body)
      
    elif ct.startswith('application/x-www-form-urlencoded'):
      return parsers.parse_query(self.body)

    else:
      return {}

  def _ua(self):
    return parsers.parse_user_agent(self.headers.get('User-Agent', ''))

  def _body(self):
    return self.read()

  def __getattr__(self, attr):
    if not hasattr(self, '_' + attr):
      raise AttributeError

    val = getattr(self, '_' + attr)()
    setattr(self, attr, val)
    return val

class httpresponse(httpmessage):
  def __init__(self):
    httpmessage.__init__(self)
    self.statusnum = None
    self.statusmsg = None
    self.compress  = True
    self.cookies   = {}

  def set_cookie(self, cookie):
    self.cookies[cookie.name] = cookie
    self.headers['Cookie'] = ' '.join(c.render() for c in self.cookies.values())
  
  def write(self, data):
    raise NotImplementedError

  def set_status(self, x):
    self.statusnum = x
    self.statusmsg = httpresponse.STATUS.get(x, 'OK')
  
  status = property(lambda s: s.statusnum, set_status)
  
  STATUS = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Time-out",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request-URI Too Large",
    415: "Unsupported Media Type",
    416: "Requested range not satisfiable",
    417: "Expectation Failed",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Time-out",
    505: "HTTP Version not supported",
  }
