'''
Utility classes for creating dynamic html documents
'''

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

from pyy_tag import pyy_tag


class include(pyy_tag):
  '''
  includes the contents of a file on disk.
  takes a filename
  '''
  def __init__(self, f):
    fl = file(f, 'rb')
    self.data = fl.read()
    fl.close()
  
  def render(self, indent=1, inline=False):
    return self.data


class pipe(pyy_tag):
  '''
  pipes the output of a program
  '''
  def __init__(self, cmd, data='', mode='t'):
    import os
    fin, fout = os.popen4(cmd, mode)
    fin.write(data)
    fin.close()
    self.data = fout.read()
  
  def render(self, indent=1, inline=False):
    return self.data

def pipe2(cmd, data='', mode='t'):
  import os
  fin, fout = os.popen4(cmd, mode)
  fin.write(data)
  fin.close()
  return fout.read()


class escape(pyy_tag):
  '''
  escapes special characters into their html entities
  '''
  @staticmethod
  def escape(data, quote=False): # stoled from std lib cgi
    '''
    Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true, the quotation mark character (")
    is also translated.
    '''
    data = data.replace("&", "&amp;") # Must be done first!
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    if quote:
      data = data.replace('"', "&quot;")
    return data
  
  def render(self, indent=1, inline=False):
    return self.escape(pyy_tag._render_children(self, indent, inline))

_unescape = {'quot' :34,
             'amp'  :38,
             'lt'   :60,
             'gt'   :62,
             'nbsp' :32,
             # more here
             'yuml' :255
             }


def unescape(data):
  '''
  unescapes html entities
  '''
  import re
  cc = re.compile('&(?:(?:#(\d+))|([^;]+));')
  
  result = []
  m = cc.search(data)
  while m:
    result.append(data[0:m.start()])
    d = m.group(1)
    if d:
      d = int(d)
      result.append(d > 255 and unichr(d) or chr(d))
    else:
      d = _unescape.get(m.group(2), ord('?'))
      result.append(d > 255 and unichr(d) or chr(d))
    
    data = data[m.end():]
    m = cc.search(data)
  
  result.append(data)
  return ''.join(result)


class lazy(pyy_tag):
  '''
  delays function execution until render
  '''
  def __init__(self, func, *args, **kwargs):
    self.func = func
    self.args = args
    self.kwargs = kwargs
  
  def render(self, indent=1, inline=False):
    return self.func(*self.args, **self.kwargs)

