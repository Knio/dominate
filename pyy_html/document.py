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
  def __init__(self, title='PYY Page', doctype=None, request=None):
    '''
    Creates a new document instance. Accepts `title`, `doctype`, and `request` keyword arguments.
    '''
    self.cookies       = {}
    self.doctype       = doctype
    self.html          = html()
    self.html.document = self
    self.head          = self.html.add(head())
    self.body          = self.html.add(body())
    self._entry        = self.body
    self.title         = title
    self.request       = request
  
  def setdoctype(self, doctype=None):
    '''
    Assigns a doctype to the document for tag tree validation.
    '''
    if doctype: doctype.validate(self.html)
    self.doctype = doctype
  
  def add(self, obj):
    '''
    Adding tags to a document appends them to the <body>.
    '''
    return self._entry.add(obj)
  
  def __iadd__(self, obj):
    self._entry += obj
    return self
  
  def __setattr__(self, attr, value):
    if attr == 'title' and title in self.html:
        self.html.get(title)[0].children = [value]
    object.__setattr__(self, attr, value)
  
  def render(self):
    '''
    Create a <title> tag if not present and render the DOCTYPE and tag tree.
    '''
    r = ""
    
    #Add a title tag if it does not exist
    if title not in self.html:
        self.head += title(self.title)
    
    #Add the doctype if one was set
    if self.doctype:
        r += self.doctype.render() + '\n'
    
    r += self.html.render()
    return r
  __str__ = __unicode__ = render
  
  def __repr__(self):
    r = '<pyy_html.document.document'
    
    if (self.doctype):
      r += ' '
      r += self.doctype.__name__
    
    if (self.title):
      r += ' "%s"' % self.title
    
    r += '>'
    return r

