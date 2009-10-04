from pyy_html import *
def handle_error(handler, req, res, status, *args):
  tb = res.body
  d = document()
  d += html.div(html.h2('Oops! something bad happened'), html.pre(tb))
  res.body = d.render()
  res.headers['Content-Type'] = 'text/html'
