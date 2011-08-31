from pyy.html import *

def get(handler, req, res, *args):
  d = document()
  d += "Hi there!"
  res.body = d.render()





