



'''
This is an example website intended to show off the major features of pyy.
It's also a good for test-driven development, to decide what 
the interfaces should look like and make sure they work.
'''


from pyy_httpserver import *
from pyy_web        import httperror





class exampleserver(httpserver):   
  '''
  format of httpserver.sites:
  
  [ SPECIFIER, HANDLER, ... ]
  where SPECIFIER is one of:
    * a regular expression string - matches that hostname (or uri, in a sub-handler)
    * an HTTP error code          - matches that error code
    * httperror                   - matches all errors
    * None                        - matches None or the empty string
    * True                        - matches everything
  
  If no specifiers match, an httperror(404) will be returned.
  If multiple SPECIFIERs match, the last one will be used. If the last one returns a 404 error, then the second last one will be used, etc.
  Note that if a leaf-node (final handler) raises a 404, that error will be handled normally and will not cause the resolver to keep looking
  
  and HANDLER is one of:
    * [ SPECIFIER, HANDLER, ...]  - to do further processing
    * a function object           - will be called with f(*args) where args is a list of all regex matches that were encountered in the entire processing of this request. The function's return value will then be used as a new HANDLER
    * a handler object            - will be called with .handle(httpserver, request, response, *args) (or .handle_error(..) if this is an error match)
    * None                        - do nothing
    * an httperror instance       - this error will be raised
  
  '''
  
  # an example:

  srcserv = fileserver('../..')
  docserv = syntaxfileserver('../..')

  sites = [
    
    True, [ 
      # example.zkpq.ca didn't match, redirect the user to the right hostname
      '^/(.*)$', lambda x: httperror(302, 'http://example.zkpq.ca:50005/%s' % x)
    ],
    
    '^example.zkpq.ca$', [
      '^/(\w*)$',   lambda x:pyyscript('.', '%s.py' %x), # need lambda to add '.py'
      '^/src(.*)$', syntaxfileserver ('../..'), # serve the source dir with highlighting. don't need a lambda here, but it works
      '^/doc(.*)$', fileserver('../'),          # serve the documentation 
      
      httperror,    lambda :pyyscript('.', 'error.py'), # generic error
      404,          lambda :pyyscript('.', '404.py'),   # specific error
    ]
    
  ]
  
  # TODO: make pyy_httpserver acctually implement this!
  
  port = 50005

exampleserver().run(1)

