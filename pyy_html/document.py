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

class document(object):
    def __init__(self, title='HTML Page'):
        self.title   = title
        self.cookies = {}
        self.doctype = None
        self.html    = None
    
    def getbody(self):
        if not self.html:
            raise ValueError('No html tag found.') #Likely not instantiated from a child class
        
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
    
    def render(self):
        r = []
        
        if self.doctype:
            r.append(self.doctype)
            r.append('\n')
        
        if not 'title' in self.html:
            #FILTHY hack to add a title element from whatever spec was imported
            head = self.html.get('head')
            if head:
                import sys
                for spec in ['pyy_html.xhtml11', 'pyy_html.html5', 'pyy_html.xhtml10strict', 'pyy_html.html4strict', 'pyy_html.xhtml10frameset', 'pyy_html.html4frameset']:
                    if spec in sys.modules:
                        head[0] += sys.modules[spec].title(self.title)
        
        r.append(self.html)
        return ''.join(map(str, r))
    
    def __str__(self):
        return self.render()
