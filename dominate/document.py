__license__ = '''
This file is part of Dominate.

Dominate is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

Dominate is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with Dominate.  If not, see
<http://www.gnu.org/licenses/>.
'''

from . import tags

try:
  basestring = basestring
except NameError: # py3
  basestring = str
  unicode = str

class document(tags.html):
  tagname = 'html'
  def __init__(self, title='Dominate', doctype='<!DOCTYPE html>', request=None):
    '''
    Creates a new document instance. Accepts `title`, `doctype`, and `request` keyword arguments.
    '''
    super(document, self).__init__()
    self.doctype    = doctype
    self.head       = super(document, self).add(tags.head())
    self.body       = super(document, self).add(tags.body())
    self.title_node = self.head.add(tags.title(title))
    self._entry     = self.body

  def get_title(self):
    return self.title_node.text

  def set_title(self, title):
    if isinstance(title, basestring):
      self.title_node.text = title
    else:
      self.head.remove(self.title_node)
      self.head.add(title)
      self.title_node = title

  title = property(get_title, set_title)

  def add(self, *args):
    '''
    Adding tags to a document appends them to the <body>.
    '''
    return self._entry.add(*args)

  def render(self, *args, **kwargs):
    '''
    Creates a <title> tag if not present and renders the DOCTYPE and tag tree.
    '''
    r = []

    #Validates the tag tree and adds the doctype if one was set
    if self.doctype:
      r.append(self.doctype)
      r.append('\n')
    r.append(super(document, self).render(*args, **kwargs))

    return u''.join(r)
  __str__ = __unicode__ = render

  def __repr__(self):
    return '<dominate.document "%s">' % self.title
