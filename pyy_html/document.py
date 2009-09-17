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
  def __init__(self, title='PYY Page', doctype=None):
    self.title    = title
    self.cookies  = {}
    self.doctype  = doctype
    self.html     = html()
    self.html.document = self
    self.head     = self.html.add(head())
    self.body     = self.html.add(body())
    self._entry   = self.body
    
  def setdoctype(self, doctype=None):
    if doctype: doctype.validate(self.html)
    self.doctype = doctype

  def add(self, obj):
    return self._entry.add(obj)
  
  def __iadd__(self, obj):
    self._entry += obj
    return self
     
  def render(self):
    r = ""
    
    if title not in self.html:
        self.head += title(self.title)

    if self.doctype:
        r += self.doctype.render() + '\n'

    r += self.html.render()
    return r
  
  def __str__(self):
    return self.render()


