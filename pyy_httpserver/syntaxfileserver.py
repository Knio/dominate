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

class syntaxfileserver(fileserver.fileserver):
  def write_file(self, conn, req, res, path, type):
    try:
      from pygments            import highlight
      from pygments.lexers     import get_lexer_for_filename
      from pygments.formatters import HtmlFormatter
      import threadio
      
      #TODO: use threadio?
      code = open.popen4(path, 't').read()
      name = os.path.basename(path)
      
      ret = highlight(code, get_lexer_for_filename(name), HtmlFormatter())
    except ImportError:
      import fileserver
      ret = fileserver.fileserver.write_file(self, conn, req, res, path)
    
    res.headers['Content-Length'] = os.path.getsize(ret)
    res.headers['Content-Type']   = 'text/html'
    return ret


