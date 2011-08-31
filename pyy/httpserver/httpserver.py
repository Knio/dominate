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
import types

import http
import threadserver as server

from pyy.web import httperror

class httpserver(object):
  compress = True
  rewrite = []
  sites   = []
  uri     = []
  port    = 8080

  def __init__(self):
    if not self.sites:
      self.sites = [True, self.uri]


  def find_handler(self, uri, config, *args):
    handler = False
    for r, c in reversed(zip(config[0::2], config[1::2])):
      h = False
      # unconditionaly matches
      if r is True: h = c
      # matches None or empty string
      elif r is None:
        if not uri: h = c
      # matches that error code
      elif isinstance(r, int):
        if isinstance(uri, httperror) and uri.args[0] == r:
          h = c
      # matches all errors
      elif r is httperror:
        if isinstance(uri, httperror):  h = c
      # matches regex string
      elif isinstance(r, str):
        if isinstance(uri, str):
          m = re.match(r, uri)
          if m:
            args += m.groups()
            uri = uri[:m.span()[1]]
            h = c
      # didn't match anything
      if h is not False:
        handler = h
        break
    return handler, uri, args


  def handle(self, conn, req, res):
    handler = None
    args = ()

    # rewrite uris
    for r,s in self.rewrite:
      req.uri = re.sub(r, s, req.uri)

    # find a handler
    handler, uri, args = self.find_handler(req.host, self.sites)
    uri = req.uri
    while 1:
      if isinstance(handler, str):
        handler, uri, args = self.find_handler(handler, self.sites)

      if isinstance(handler, list):
        handler, uri, args = self.find_handler(uri, handler)

      elif isinstance(handler, httperror):
        raise handler

      elif isinstance(handler, (types.FunctionType, types.MethodType)):
        handler = handler(*args)
        args = ()

      elif hasattr(handler, 'handle'):
        return handler.handle(conn, req, res, *args)

      elif handler is False:  raise httperror(404)
      elif handler is None:   return False
      else:                   raise ValueError(handler)

  def handle_error(self, conn, req, res, status, *errors):
    if status == 500:
      import traceback
      res.body = traceback.format_exc()

    elif status in (301, 302, 303):
      if errors:
        res.headers['Location'] = errors[0]

    handler, uri, args = self.find_handler(req and req.host, self.sites)
    uri = httperror(status, *errors)
    try:
      while 1:
        if isinstance(handler, list):
          handler, uri, args = self.find_handler(uri, handler)

        elif isinstance(handler, httperror):
          raise handler

        elif isinstance(handler, (types.FunctionType, types.MethodType)):
          handler = handler(*args)
          args = ()

        elif hasattr(handler, 'handle_error'):
          return handler.handle_error(conn, req, res, status, *args)

        # why is this two different cases?
        elif handler is None:
          if status == 500:
            import traceback
            traceback.print_exc()
          return False
        elif handler is False:
          if status == 500:
            import traceback
            traceback.print_exc()
          return
        else: raise ValueError(handler)

    except httperror, e:
      if e.args == (status,)+errors:
        return self.handle_error(conn, req, res, 500, 'infinite recursion in error handler')
      return self.handle_error(conn, req, res, e.args[0], *e.args[1:])


  def run(self, *args):
    s = server.server()
    def handle(server, conn):
      return http.httphandler(conn, self)

    s.listen(('',self.port), handle)
    s.run()

