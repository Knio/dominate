from pyy.html import document
from pyy.html.tags import *

class page(document):
  prefix  = ''
  css     = []
  script  = []
  inline  = False

  def __init__(self, **kwargs):
    document.__init__(self, **kwargs)

    for i in self.css:
      if self.inline:
        self.head += style(include(i), type="text/css")
      else:
        if not i.startswith('http://'):
          i = self.prefix + i
        self.head += link(href=i, type="text/css", rel="stylesheet")

    for i in self.script:
      if self.inline:
        self.head += script(include(i), type="text/javascript")
      else:
        if not i.startswith('http://'):
          i = self.prefix + i
        self.head += script(src=i, type="text/javascript")


  @classmethod
  def get(cls, handler ,req, res, *args, **kwargs):
    p = cls()
    p.do_get(*args, **kwargs)
    res.headers['Content-Type'] = 'text/html'
    res.body = p.render()

  @classmethod
  def post(cls, handler ,req, res, *args, **kwargs):
     raise httperror(405)

  @classmethod
  def handle(cls, handler, req, res, *args, **kwargs):
    h = getattr(cls, req.method.lower(), None)
    if not h: raise httperror(405)
    h(handler, req, res, *args, **kwargs)

  @classmethod
  def handle_error(cls, handler, req, res, status, *args):
    p = cls()
    h = getattr(p, 'do_%d' % status, getattr(p, 'do_error', None))
    if not h: raise httperror(405)
    h(status, *args)
    res.headers['Content-Type'] = 'text/html'
    res.body = p.render()
