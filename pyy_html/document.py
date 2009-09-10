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
        
        #Add default attributes
        if 'default' in self.doctype.valid[root.__class__]:
            for attribute, value in self.doctype.valid[root.__class__]['default'].iteritems():
                if attribute not in root.attributes:
                    root[attribute] = value
        if not root.allow_invalid:
            #Check for invalid attributes
            invalid_attributes = []
            for attribute, value in root.attributes.iteritems():
                if attribute not in self.doctype.valid[root.__class__]['valid']:
                    invalid_attributes.append(attribute)
            if invalid_attributes:
                raise AttributeError('%s element has one or more invalid attributes: %s.' % (type(root).__name__, ', '.join(invalid_attributes)))
            #Check for missing required attributes
            if 'required' in self.doctype.valid[root.__class__]:
                missing_attributes = [attribute for attribute in self.doctype.valid[root.__class__]['required'] if attribute not in root.attributes]
                if missing_attributes:
                    raise AttributeError('%s element has one or more missing attributes that are required: %s.' % (type(root).__name__, ', '.join(missing_attributes)))
        
        #Check children
        for child in root.children:
            if child.is_single and child.children:
                raise ValueError('%s element cannot contain any child elements. Currently has: %s.' % (type(root).__name__, ', '.join(type(c).__name__ for c in root.children)))
            elif child.__class__ not in self.doctype.valid[root.__class__]['children']:
                raise ValueError('%s element cannot contain %s element as child.' % (type(root).__name__, type(child).__name__))
            else:
                self.validate(child)
        
        return True
    
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
