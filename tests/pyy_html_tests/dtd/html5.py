import unittest
from pyy_html.html     import *
from pyy_html.document import document
from pyy_html.dtd      import html5

class Html5Tests(unittest.TestCase):
    def testAllTags(self):
        d = document()
        
        #METADATA (title, base, link, meta, style)
        d.html.head += title('Test')
        d.html.head += base(href='')
        d.html.head += base(target='')
        d.html.head += link()
        d.html.head += meta(name='', content='')
        d.html.head += meta(http_equiv='', content='')
        d.html.head += meta(content='')
        d.html.head += meta(charset='')
        d.html.head += meta(itemprop='', content='')
        d.html.head += style()
        
        #SCRIPTING (script, noscript)
        d.html.body += script('stuff')
        d.html.body += script(src='stuff')
        d.html.body += noscript()
        
        #SECTIONS (section, nav, article, aside, h1, h2, h3, h4, h5, h6, hgroup, header, footer, address)
        d.html.body += section(hgroup(h1(''), h2('')))
        d.html.body += nav('')
        d.html.body += article(h3(''), h4(''))
        d.html.body += article(h5(''), h6(''))
        d.html.body += header('')
        d.html.body += footer('')
        d.html.body += address('')
        
        #GROUPING
        d.html.body += p(hr(), br(), pre('test'))
        d.html.body += dialog(dt('hi'), dd('hi'))
        d.html.body += blockquote('long quote')
        