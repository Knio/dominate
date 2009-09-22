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
from pyy_html.html     import a, br, div, hr, comment
from pyy_html.document import document
from pyy_html.parser   import parse, pageparse

class ParsingTests(unittest.TestCase):
  def testTag(self):
    h = div()
    s = '<div></div>'
    self.assertEquals(h.render(), parse(s).render())

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

  def testDoctype(self):
    h = document()
    s = h.render()
    self.assertEquals(h.render(), pageparse(s).render())

