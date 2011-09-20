# wsgi.py - pyy WSGI gateway
#
# WARNING: Edit this file very carefully, a bug will crash your site!

import routing

def application(environ, start_response):
  method = environ['REQUEST_METHOD']
  uri = environ['PATH_INFO']

  try:
    #TODO check return value, pass args
    body = str(routing.match(uri, method)())
    status = '200 OK'

  except SystemExit:
    pass

  except Exception, e:
    import traceback
    body = '''<!DOCTYPE html>
<html><head><title>Error</title></head><body><pre>
An error occured while generating this page:

%s
</pre></body></html>''' % traceback.format_exc()
    status = '500 INTERNAL SERVER ERROR'

  headers = [
    ('Content-Type', 'text/plain'),
    ('Content-Length', str(len(body))),
  ]
  start_response(status, headers)

  return body
