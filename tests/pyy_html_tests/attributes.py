import unittest
from pyy_html.html import html, img

class AttributeTests(unittest.TestCase):
    def testAddViaDict(self):
        i = img()
        i['src'] = 'test.png'
        self.assertEqual(str(i), '<img src="test.png" />')
    
    def testAddViaKeywordArg(self):
        i = img(src='test.png')
        self.assertEqual(str(i), '<img src="test.png" />')
