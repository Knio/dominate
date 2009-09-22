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
from pyy_html.html     import div, hr, comment
from pyy_html.document import document
from pyy_html.parser   import parse, pageparse

class ParsingTests(unittest.TestCase):
  def testBasic(self):
    h = div()
    s = '<div></div>'
    self.assertEquals(h.render(), parse(s).render())

  def testSingle(self):
    h = hr()
    s = '<hr />'
    self.assertEquals(h.render(), parse(s).render())

  def testDoctype(self):
    h = document()
    s = h.render()
    self.assertEquals(h.render(), pageparse(s).render())



