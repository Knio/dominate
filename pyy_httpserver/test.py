from pyy_httpserver import *

class myserver(httpserver):
  uri = [
    ('^/(.*)$',         fileserver('.')),
    ('^/(.*\.(py|c))$', syntaxfileserver('.')),
    ('^/(.*\.pyy)$',    pyyserver()),
  ]

if __name__ == '__main__':
  myserver().run(0.1)


