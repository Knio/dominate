'''
This file configures a pyy_httpserver to run the pyy example website

'''

from pyy_httpserver import *

class ExampleServer(httpserver):
  port = 50004
  uri = [
    ('^/(.*\.py)/(.*)$', pyyserver('.')),
  ]
  
ExampleServer().run(1)

  #sites = 
  #{ 'example.pyy.zkpq.ca':
  #    ('^/(.*)$',        lambda x: pyyscript('.',$1+'.py')),
  #    ('^/source/(.*)$', syntaxfileserver('../../..', $1)),
  #  None:
  #    '^/(.*)$':        HttpError(404, $1)
  #}

  



