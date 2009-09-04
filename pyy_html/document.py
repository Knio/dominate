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

from html import html, body, head, title

class document(object):
    def __init__(self, title='HTML Page'):
        self.title   = title
        self.cookies = {}
        self.doctype = None
        self.html    = html()
        self.head    = self.html.add(head())
        self.body    = self.html.add(body())
    
    def getbody(self):
        if not self.html:
            raise ValueError('No html tag found.')
        
        bodys = self.html.getElementsByTagName('body')
        
        if not bodys:
            raise ValueError('No body tag found.')
        
        return bodys[0]
    
    def add(self, obj):
        if not self._entry:
            self._entry = self.getbody()
        return self._entry.add(obj)
    
    def __iadd__(self, obj):
        if not self._entry:
            self._entry = self.getbody()
        
        self._entry += obj
        return self
    
    def validate(self, root=None):
        if root is None:
            root = self.html
        for child in root.children:
            if child in self.doctype.valid[root]['children']:
                self.validate(child)
            else:
                raise ValueError('%s element cannot contain %s element as child.' % (type(root).__name__, type(child).__name__))
    
    def render(self):
        r = []
        
        if self.doctype:
            r.append(self.doctype)
            r.append('\n')
        
        if title not in self.html:
            self.head += title(self.title)
        
        r.append(self.html)
        return ''.join(map(str, r))
    
    def __str__(self):
        return self.render()
