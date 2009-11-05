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
  
  def add(self, obj):
    '''
    Adding tags to a document appends them to the <body>.
    '''
    return self._entry.add(obj)
  
  def __iadd__(self, obj):
    self._entry += obj
    return self
  
  
  def _get_title(self):
    if title not in self.head:
      self.head += title("PYY Page")
    return self.head.get(title)[0].children[0]
  
  def _set_title(self, value):
    if title in self.head:
      self.head.get(title)[0].children = [value]
    else:
      self.head += title(value)
  
  title = property(_get_title, _set_title, None, 'Document title.')
  
  
  def validate(self):
    '''
    Validates the tag tree against a DOCTYPE
    '''
    if self.doctype:
      self.doctype.validate(self.html)
    else:
      raise ValueError('No DOCTYPE has been assigned.')
  
  def render(self):
    '''
    Creates a <title> tag if not present and renders the DOCTYPE and tag tree.
    '''
    r = ""
    
    #Validates the tag tree and adds the doctype if one was set
    if self.doctype:
      self.validate()
      r += self.doctype.render() + '\n'
    
    r += self.html.render()
    return r
  __str__ = __unicode__ = render
  
  def __repr__(self):
    r = '<pyy_html.document.document'
    
    if self.doctype:
      r += ' '
      r += self.doctype.__name__
    
    r += ' "%s">' % self.title
    
    return r

