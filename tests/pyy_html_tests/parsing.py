import unittest
from pyy_html.xhtml11 import html, head, body, h1, p
from pyy_html.html    import comment
from pyy_html.parser  import parse


class ParsingTests(unittest.TestCase):
  def testBasic(self):
    h = div()
    s = '<div></div>'
    self.assertEquals(h.render(), parse(s).render())
    
    
    

