__license__ = '''
This file is part of pyy.
 
pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.
 
pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.
 
You should have received a copy of the GNU Lesser General
Public License along with pyy. If not, see
<http://www.gnu.org/licenses/>.
'''

import unittest
from pyy_html           import dtd
from pyy_html.html      import a, b, br, div, hr, p, comment
from pyy_html.document  import document
from pyy_html.parser    import parse, pageparse

class ParsingTests(unittest.TestCase):
  def testTag(self):
    s = '<div></div>'
    self.assertTrue(isinstance(parse(s), div))

  def testSingle(self):
    s = '<hr />'
    self.assertTrue(isinstance(parse(s), hr))
  
  def testAdjacentSingle(self):
    s = '<hr /><br />'
    r = parse(s)
    self.assertTrue(isinstance(r, list))
    self.assertTrue(isinstance(r[0], hr))
    self.assertTrue(isinstance(r[1], br))
  
  def testAdjancentMixed(self):
    s = '<hr /><a></a>'
    r = parse(s)
    self.assertTrue(isinstance(r, list))
    self.assertTrue(isinstance(r[0], hr))
    self.assertTrue(isinstance(r[1], a))
  
  def testAdjacentTags(self):
    s = '<a></a><p></p>'
    r = parse(s)
    self.assertTrue(isinstance(r, list))
    self.assertTrue(isinstance(r[0], a))
    self.assertTrue(isinstance(r[1], p))

  def testDoctypes(self):
    for i in (dtd.html4frameset, dtd.html4strict, dtd.html5, dtd.xhtml10frameset, dtd.xhtml10strict, dtd.xhtml11):
      h = document(doctype=i)
      s = h.render()
      self.assertEquals(s, pageparse(s).render())

  # malformed documents
  def testNoClose(self):
    h = div('hi')
    s = '<div>hi'
    self.assertEquals(parse(s, allow_invalid_markup=True).render(), h.render())
  
  def testNoCloseButError(self):
    s = '<div>hi'
    try:
      parse(s)
      self.fail('Should throw parsing error: "%s"' % s)
    except ValueError:
      pass

  def testOutOfOrder(self):
    h = div('hi there ', b('im bold'))
    s = '<div>hi there <b>im bold</div></b>'
    self.assertEquals(parse(s, allow_invalid_markup=True).render(), h.render())

  def testNotXml(self):
    # some people don't write single tags as <br />
    h = div('line', br(), 'new line', br(), 'new line')
    s = '<div>line<br>new line<BR>new line</div>'
    self.assertEquals(parse(s, allow_invalid_markup=True).render(), h.render())

  def testNoClose2(self):
    # some people think <p> is a single
    h = div('paragraph', p('new paragraph', p('new paragraph')))
    s = '<div>paragraph<p>new paragraph<P>new paragraph</div>'
    self.assertEquals(parse(s, allow_invalid_markup=True).render(), h.render())

  def testComment(self):
    h = div(comment('hi there'))
    s = '<div><!--hi there--></div>'
    self.assertEquals(parse(s).render(), h.render())
    

