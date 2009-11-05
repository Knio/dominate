'''
This is an example website intended to show off the major features of pyy.
It's also a good for test-driven development, to decide what 
the interfaces should look like and make sure they work.
'''

__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy.  If not, see
<http://www.gnu.org/licenses/>.
'''

from pyy_httpserver import *
from pyy_web        import httperror


class exampleserver(httpserver):   

  srcserv = fileserver('../..')
  docserv = syntaxfileserver('../..')

  sites = [
    
    True, [ 
      # example.zkpq.ca didn't match, redirect the user to the right hostname
      '^/(.*)$', lambda x: httperror(302, 'http://example.zkpq.ca:50005/%s' % x)
    ],
    
    '^example.zkpq.ca$', [
      '^/(\w*)$'   , lambda x:pyyscript('.', '%s.py' %x), # need lambda to add '.py'
      '^/src/(.*)$', syntaxfileserver ('../..'), # serve the source dir with highlighting. don't need a lambda here, but it works
      '^/doc/(.*)$', fileserver('../'),          # serve the documentation 
      
      httperror, lambda :pyyscript('.', 'error.py'), # generic error
      404,       lambda :pyyscript('.', '404.py'),   # specific error
    ]
    
  ]
  
  port = 50005

exampleserver().run(1)

