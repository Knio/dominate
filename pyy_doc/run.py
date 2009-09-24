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

'''This file configures a pyy_httpserver to run the pyy example website'''

from pyy_httpserver import *

class ExampleServer(httpserver):
  port = 50004
  uri = [
    ('^/(.*\.py)/(.*)$', pyyserver(dir)),
  ]

ExampleServer().run(1)

  #sites = 
  #{ 'example.pyy.zkpq.ca':
  #    ('^/(.*)$',        lambda x: pyyscript('.',$1+'.py')),
  #    ('^/source/(.*)$', syntaxfileserver('../../..', $1)),
  #  None:
  #    '^/(.*)$':        HttpError(404, $1)
  #}

  



