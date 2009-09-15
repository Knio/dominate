import unittest
from pyy_html.html import html, head, body, h1, p, comment

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
