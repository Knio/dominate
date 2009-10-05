from pyy_html import *
ief handle_error(handler, req, res, status, *args):
  if status == 500:
    tb = res.body
    d = document()
    d += html.div(html.h2('Oops! something bad happened'), html.pre(tb))
    res.body = d.render()
    res.headers['Content-Type'] = 'text/html'
