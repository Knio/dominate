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

from response    import response
from request     import BROWSER_IE
from html4strict import *
from html4strict import __all__

###############################################################################

class htmlpage(response):
    def __init__(self, title='XHTML 1.0 Strict Page', request=None):
        response.__init__(self, title, request)
        
        self.headers['Content-Type'] = 'application/xhtml+xml'
        self.doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'
        self.html    = html()
        self.html.head, self.html.body = self.html.add(head(), body())
    
    def render(self, just_html=False):
        if not just_html and self.request.browser == BROWSER_IE:
            self.headers['Content-Type'] = 'text/html'
        return response.render(self, just_html)
