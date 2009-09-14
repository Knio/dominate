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

from html4strict   import html4strict
from pyy_html.html import frameset, frame, noframes, iframe

class html4frameset(html4strict):
  docstring = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">'
  
  #Will this work?
  valid.update({
    frameset: {'valid': ['rows', 'cols', 'onload', 'onunload'] + COMMON_CORE}
    frame   : {'valid': ['longdesc', 'name', 'src', 'frameborder', 'marginwidth', 'marginheight', 'noresize', 'scrolling'] + COMMON_CORE}
    noframes: {'valid': COMMON}
    iframe  : {'valid': ['longdesc', 'name', 'src', 'frameborder', 'marginwidth', 'marginheight', 'scrolling', 'align', 'height', 'width'] + COMMON_CORE}
  })
