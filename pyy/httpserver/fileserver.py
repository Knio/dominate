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

# import stackless
import os
import os.path
import sys
import http
import time
import warnings
from datetime import datetime
from urllib   import unquote_plus
from pyy.web  import httperror


class staticserver(object):
  def __init__(self, handler):
    self.handler  = handler

  def handle(self, conn, req, res, *args):
    if not req.method in ['GET', 'HEAD']:
      raise httperror(405)

    cache     = True
    modified  = True
    for k,v in req.headers.iteritems():
      if k == 'If-Modified-Since':
        try:     t = http.httptime(v)
        except:  continue # malformed header value
        if self.handler.get_mtime(*args) <= t: # I hate time libraries so much
          modified = False

      elif k == 'Cache-Control':
        if v == 'no-cache':
          cache = False

      elif k == 'Expect':   raise httperror(417)
      elif k == 'If-Range': raise httperror(501)
      elif k == 'Range':    raise httperror(501)

      elif k == 'Referrer': pass

      else:
        warnings.warn('unhandled request header: %s: %s' % (k,v))

    if not modified and cache:
      raise httperror(304)

    return self.handler.handle(conn, req, res, *args)


# from stacklessfileIOCP import stacklessfile

class fileserver(object):
  MIME = {
  'txt':  'text/plain',
  'htm':  'text/html',
  'html': 'text/html',
  'pyc':  'application/octet-stream',
  'css':  'text/css',
  'jpg':  'image/jpeg',
  'jpeg': 'image/jpeg',
  'png':  'image/png',
  }

  COMPRESS = {
  'png':  False,
  'jpg':  False,
  'jpeg': False,
  'gif':  False,
  'zip':  False,
  'rar':  False,
  'mp3':  False,
  'avi':  False,
  }

  def __init__(self, root='.', dir_listing=True):
    self.root = root
    self.dir_listing = dir_listing

  def check_path(self, path):
    if path.startswith('/'):
      path = path[1:]

    path = os.path.join(self.root, unquote_plus(path))
    path = os.path.realpath(os.path.abspath(path))
    root = os.path.realpath(os.path.abspath(self.root))

    # don't let them go outside root
    if not path.startswith(root):
      raise httperror(403)

    # does it exist?
    if not os.path.exists(path):
      raise httperror(404)

    valid = False
    if os.path.isfile(path): valid = True
    if os.path.isdir(path) and self.dir_listing: valid = True

    if not valid:
      raise httperror(406)

    return path

  def get_mtime(self, *args):
    path = self.check_path(*args)
    return datetime.utcfromtimestamp(os.path.getmtime(path))

  def handle(self, conn, req, res, path, *unused):
    path = self.check_path(path)

    if os.path.isfile(path):
      fsize = os.path.getsize(path)
      mtime = os.path.getmtime(path)
      try:    ext = os.path.basename(path).split('.')[-1]
      except: ext = ''
      res.compress  = self.COMPRESS.get(ext, True)
      res.headers['Content-Type']   = self.MIME.get(ext, 'text/plain')
      res.headers['Content-Length'] = fsize
      res.headers['Last-Modified']  = http.httptime(time.gmtime(mtime))

      if req.method == 'GET':
        return self.write_file(conn, req, res, path)

    if os.path.isdir(path):
      # what if HEAD?
      res.headers['Content-Type'] = 'text/html'
      res.body = self.write_dir_listing(path)


  def write_file(self, conn, req, res, path):
    fsize = os.path.getsize(path)

    f = file(path, 'rb')

    # res.body = f.read()
    # return

    def write():
      while 1:
        data = f.read(256*1024)
        if not data: break
        conn.conn.write(data)
      f.close()

    return write

  def write_dir_listing(self, path):
    f = os.listdir(path)
    f = (os.path.isdir(os.path.join(path,i)) and i+'/' or i for i in f)

    r = ['<html>','<body>']
    r.extend('<a href="%s">%s</a><br />' % (i,i) for i in f)
    r.extend(['</html>','</body>'])
    return '\r\n'.join(r)
