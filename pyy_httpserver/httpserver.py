import re
import http
import server



class httpserver(object):
  uri = []

  def __init__(self):
    pass

  def handle(self, conn, req, res):
    handler = None
    args = ()
    for r, h in reversed(self.uri):
      m = re.match(r, req.uri)
      if m:
        handler = h
        args = m.groups()
        break

    if not handler:
      raise http.HTTPError(404)

    return handler.handle(conn, req, res, *args)

  def handle_error(self, http, req, res, status, *errors):
        
    if status == 500:
      import traceback
      res.body = traceback.format_exc()

  def run(self, *args):
    s = server.server()
    s.listen(('',54321), http.httphandler, self)
    s.run(*args)


