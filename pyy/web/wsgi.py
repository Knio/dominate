# wsgi.py - pyy WSGI gateway
#
# WARNING: Edit this file very carefully, a bug will crash your site!

import routing

def application(environ, start_response):
  method = environ['REQUEST_METHOD']
  uri = environ['PATH_INFO']
  body = str(routing.match(uri, method)())
  #TODO check return value, pass args

  status = '200 OK'
  headers = [
    ('Content-Type', 'text/plain'),
    ('Content-Length', str(len(body))),
  ]
  start_response(status, headers)

  return body
