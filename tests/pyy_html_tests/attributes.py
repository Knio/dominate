import unittest
from pyy_html.xhtml11 import html, img

class AttributeTests(unittest.TestCase):
    def testDefaultBlank(self):
        self.assertEqual(str(img(src='test.png')), '<img src="test.png" alt="" />')
    
    def testDefault(self):
        self.assertEqual(str(html()), '<html xmlns="http://www.w3.org/1999/xhtml"></html>')
    
    def testInvalid(self):
        self.assertRaises(AttributeError, html, src='')
    
    def testAllowInvalid(self):
        try:
            h = html(src='', __invalid=True)
        except AttributeError:
            self.fail()
