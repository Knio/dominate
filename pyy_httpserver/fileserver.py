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

import stackless
import os
import os.path
import sys
import threadio
import http
import time
import warnings
from urllib import unquote_plus
from http import HTTPError


class fileserver(object):
  def __init__(self, root='.'):
    self.root = root

  def handle(self, conn, req, res, path, *args):
    if not req.method in ['GET', 'HEAD']:
      raise HTTPError(405)
    
    path = os.path.join(self.root, unquote_plus(path))
    path = os.path.realpath(os.path.abspath(path))
    root = os.path.realpath(os.path.abspath(self.root))
  
    # don't let them go outside root
    if not path.startswith(root):
      raise HTTPError(403)
    
    # does it exist?
    if not os.path.exists(path):
      raise HTTPError(404)

    # dir listing
    if os.path.isdir(path):
      res.headers['Content-Type'] = 'text/html'
      res.body = self.dir_listing(path)
      return

    if not os.path.isfile(path):
      # then what is it?
      raise HTTPError(406)

    # ok, its a file
    return self.serve_file(conn, req, res, path, *args)


  def serve_file(self, conn, req, res, path, *args):
    
    mtime = os.path.getmtime(path)
    fsize = os.path.getsize(path)
    
    for k,v in req.headers.iteritems():
      if k == 'If-Modified-Since':
        try:
          t = http.httptime(v).timetuple()
        except:
          continue
        if time.gmtime(mtime) <= t: # I hate time libraries so much
          res.status = 304 # not modified
          return
      
      elif k == 'Expect':
        raise HTTPError(417)

      elif k == 'If-Range': raise HTTPError(501)
      elif k == 'Range':    raise HTTPError(501)


      #else:
      #  warnings.warn('unhandled request header: %s: %s' % (k,v))

    
    try:
      ext = os.path.basename(path).split('.')[-1]
    except:
      ext = ''
    res.headers['Content-Type']   = self.MIME.get(ext, 'text/plain')
    res.headers['Content-Length'] = fsize
    res.headers['Last-Modified']  = http.httptime(time.gmtime(mtime))
      
    if req.method == 'HEAD':
      return
    
    elif req.method == 'GET':
      return self.write_file(conn, req, res, path, *args)
    
    else:
      raise HTTPError(405)


  def write_file(self, conn, req, res, path, *args):
    fsize = os.path.getsize(path)
    f = file(path, 'rb')
    ft = threadio.threadio(f) # this causes blocking in select()

    def write():
      while 1:
        data = ft.read(256*1024)
        if not data: break
        conn.conn.write(data)
      f.close()

    if fsize < 256*1024:
      res.body = f.read()
      ft.close()
      return
    return write

  def dir_listing(self, path):
    f = os.listdir(path)
    f = (os.path.isdir(os.path.join(path,i)) and i+'/' or i for i in f)
    
    r = ['<html>','<body>']
    r.extend('<a href="%s">%s</a><br />' % (i,i) for i in f)
    r.extend(['</html>','</body>'])
    return '\r\n'.join(r)

      
  MIME = {
  'htm':  'text/html',
  'html': 'text/html',
  'pyc':  'application/octet-stream',
  }
