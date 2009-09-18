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



