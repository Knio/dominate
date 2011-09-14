# cgi.py - pyy CGI gateway
#
# WARNING: Edit this file very carefully, a bug will crash your site!

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

import os
import sys
import imp


def get_request():
  env = os.environ
  req = httprequest()
  
  req.read   = sys.stdin.read
  req.method = env['REQUEST_METHOD']
  req.uri    = env['REQUEST_URI']
  
  http = env['SERVER_PROTOCOL']
  if http == 'HTTP/1.0':
    req.http = 1.0
  elif http == 'HTTP/1.1':
    req.http = 1.1

  HEADERS = {
    'CONTENT_LENGTH':       'Content-Length',
    'CONTENT_TYPE':         'Content-Type',
    'HTTP_USER_AGENT':      'User-Agent',
    'HTTP_COOKIE':          'Cookie',
    'HTTP_TE':              'Transfer-Encoding',
    'HTTP_COOKIE2':         'Cookie2',
    'HTTP_HOST':            'Host',
    'HTTP_CONNECTION':      'Connection',
    'HTTP_ACCEPT':          'Accept',
    'HTTP_ACCEPT_LANGUAGE': 'Accept-Language',
    'HTTP_ACCEPT_ENCODING': 'Accept-Encoding',
    'HTTP_ACCEPT_CHARSET':  'Accept-Charset',
  }
  
  for key, value in env.iteritems():
    if key in HEADERS:
      req.headers[HEADERS[key]] = value
  
  return req


def make_response(res):
  if res.body is None: res.body = ''
  res.headers.setdefault('Content-Type', 'text/plain; charset=ISO-8859-4')
  res.headers.setdefault('Cache-Control', 'no-cache')
  #res.headers.setdefault('Content-Length', len(res.body))

def write_response(res):
  if res.status:
    print 'Status: %d %s' % (res.statusnum, res.statusmsg)
  
  for key, value in res.headers.iteritems():
    print '%s: %s' % (key, value)

  print
  print res.body



if 'REQUEST_METHOD' in os.environ:
  import os
  import sys
  import imp
  from pyy.web import *
  
  fname = sys.argv[0]
  mname = os.path.basename(fname).split('.')[0]
  dname = os.path.dirname(fname)
  sys.path.append(dname)
  
  f = open(fname, 'U')
  
  try:
    m   = imp.load_module(mname, f, fname, ('.py', 'U', 1))
    req = get_request()
    res = httpresponse()
    
    result = None
    try:
      h = getattr(m, req.method.lower(), getattr(m, 'handle', None))
      if not h:
        raise httperror(405) # method not allowed
      result = h(None, req, res)
      
    except httperror, e:
      res = httpresponse()
      res.status = e.args[0]
      res.body   = '%d %s' % (res.statusnum, res.statusmsg)
      # TODO let the page do custom error handling

    make_response(res)
    write_response(res)
    if result:
      result()

  except SystemExit:
    pass

  except Exception, e:
    import traceback
    print 'Content-Type: text/html'
    print
    print '<html><head><title>Error</title></head><body><pre>'
    print 'An error occured while generating this page:'
    print
    print traceback.format_exc()
    print '</pre></body></html>'
      
  f.close()
  sys.exit(0)
