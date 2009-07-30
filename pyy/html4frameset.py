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

from html        import html_tag, single
from html4strict import *
from html4strict import htmlpage as strictpage
from html4strict import __all__ as __html4strict_all__

__all__ = __html4strict_all__ + ['frameset', 'frame', 'noframes', 'iframe']

class frameset(html_tag): valid = ['rows', 'cols', 'onload', 'onunload'] + COMMON_CORE
class frame   (single):   valid = ['longdesc', 'name', 'src', 'frameborder', 'marginwidth', 'marginheight', 'noresize', 'scrolling'] + COMMON_CORE
class noframes(html_tag): valid = COMMON
class iframe  (html_tag): valid = ['longdesc', 'name', 'src', 'frameborder', 'marginwidth', 'marginheight', 'scrolling', 'align', 'height', 'width'] + COMMON_CORE

###############################################################################

class htmlpage(strictpage):
    def __init__(self, title='HTML 4 Frameset Page'):
        strictpage.__init__(self, title)
        self.doctype = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN" "http://www.w3.org/TR/html4/frameset.dtd">'
