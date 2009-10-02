



'''
This is an example website intended to show off the major features of pyy.
It's also a good for test-driven development, to decide what 
the interfaces should look like and make sure they work.
'''


from pyy_httpserver import *

class exampleserver(httpserver):
  port = 50005

  # TODO: make pyy_httpserver acctually support this

  sites = [
    '^example.zkpq.ca$', [
      '^/(\w+)$',   lambda x:pyyscript        ('.', '%s.py' %x),
      '/src(.*)$',  lambda x:syntaxfileserver ('../..',  x),   # serve the source dir
      '/doc(.*)$',  lambda x:fileserver       ('../',    x),   # serve the documentation

      HttpError:    lambda :pyyscript('.', 'error.py'), # generic error
      404:          lambda :pyyscript('.', '404.py'),   # specific error
    ]
    
  ]

  # for now, since that doesn't work yet

exampleserver().run()

