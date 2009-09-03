import unittest
from pyy_html.xhtml11 import html, head, body, h1, p, div, htmlpage
from pyy_html.html    import comment
from pyy_html.parser  import parse


class ParsingTests(unittest.TestCase):
  def testBasic(self):
    h = div()
    s = '<div></div>'
    self.assertEquals(h.render(), parse(s).render())

  def testSingle(self):
    h = p()
    s = '<p/>'
    self.assertEquals(h.render(), parse(s).render())

  def testDoctype(self):
    h = htmlpage()
    s = h.render()
    self.assertEquals(h.render(), parse(s).render())

    

