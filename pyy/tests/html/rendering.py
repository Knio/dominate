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
from pyy.html.document import document
from pyy.html.tags     import body, h1, p, comment
from pyy.html.util     import *


class RenderingTests(unittest.TestCase):
  def testInline(self):
    self.assertEqual(str(p(h1(), __inline=True)), '<p><h1></h1></p>')
  
  def testIndented(self):
    self.assertEqual(str(p(h1())), '<p>\n\t<h1></h1>\n</p>')
  
  def testIndentedChildren(self):
    self.assertEqual(str(body(p(), p())), '<body>\n\t<p></p>\n\t<p></p>\n</body>')
  
  def testComment(self):
    self.assertEqual(str(comment('test')), '<!--test-->')
  
  def testCommentWithTags(self):
    self.assertEqual(str(body(p(), comment(p()))), '<body>\n\t<p></p>\n\t<!--\n\t<p></p>\n\t-->\n</body>')
  
  def testConditionalComment(self):
    self.assertEqual(str(comment(p(), condition='lt IE 7')), '<!--[if lt IE 7]>\n<p></p>\n<![endif]-->')
  
  def testIndentedConditionalComment(self):
    self.assertEqual(str(body(p(), comment(p(), condition='lt IE 7'))), '<body>\n\t<p></p>\n\t<!--[if lt IE 7]>\n\t<p></p>\n\t<![endif]-->\n</body>')
  
  def testDocumentTitleUpdate(self):
    d1 = document()
    rd1 = d1.render()
    d1.title = "test"
    rd1 = d1.render()
    d2 = document(title="test")
    rd2 = d2.render()
    self.assertEqual(rd1, rd2)

  def testEscape(self):
    self.assertEqual(str(p('Hi & There')), '<p>Hi & There</p>')
    self.assertEqual(str(p(escape('Hi & There'))), '<p>Hi &amp; There</p>')
    self.assertEqual(str(p(unescape('Hi &amp; There'))), '<p>Hi & There</p>')
    
    
