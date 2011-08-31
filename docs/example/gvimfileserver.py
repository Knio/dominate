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

from pyy.httpserver import fileserver
from pyy.httpserver import threadio
import os

class gvimfileserver(fileserver):
  def write_file(self, conn, req, res, path, *args):
               
    cmd = r'Z:\Programs\GVimPortable\GVimPortable.exe'\
        r' -f +":let html_use_css = 1" +":let use_xhtml=1" +":TOhtml" +":wq!" +":q!" "'+path+'"'

    fin, fout = os.popen4(cmd, 't')
    threadio.threadio(fin).close()
    threadio.threadio(fout).read()
    path += '.html'
    
    res.headers['Content-Length'] = fsize = os.path.getsize(path)
    res.headers['Content-Type'] = 'text/html' # xhtml?
    
    return fileserver.write_file(self, conn, req, res, path, *args)


