from pyy_web import *
from pyy_html import *

import subprocess

class page(document):
  css     = []
  script  = []
  inline  = False

  def __init__(self, **kwargs):
    document.__init__(self, **kwargs)
    for i in self.css:
      if self.inline:  self.head += style(include(i), type="text/css")
      else:            self.head += link (href=i,     type="text/css", rel="stylesheet")

    for i in self.script:
      if self.inline:  self.head += script(include(i), type="text/javascript")
      else:            self.head += script(src=i,      type="text/javascript")


  @classmethod
  def get(cls, handler ,req, res, *args, **kwargs):
    p = cls(*args, **kwargs)
    res.headers['Content-Type'] = 'text/html'
    res.body = p.render()
    
  @classmethod
  def post(self, handler ,req, res, *args, **kwargs):
     raise httperror(405)
    
    
  @classmethod
  def handle(self, handler, req, res, *args, **kwargs):
    h = getattr(self, req.method.lower(), None)
    if not h:
      raise httperror(405)
    h(handler, req, res, *args, **kwargs)
    
    
      
    
    


