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


