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
import sys
from pyy.httpserver import *


from fileserver import fileserver
from pyyserver  import pyyscript

if __name__ == '__main__':
  args = list(sys.argv[1:])

  port = 8080
  dir  = '.'
  while args:
    c = args.pop(0)
    if c == '-p':
      port = int(args.pop(0))
    if c == '-d':
      dir = args.pop(0)


  class myserver(httpserver):
    port = port
    uri = [
      '^/(.*)$',                   fileserver(dir),
      '^/(.*(.py|c|h|js|java))$',  syntaxfileserver(dir),
      # ('^/(.*\.m)$',                gvimfileserver(dir)),
      # ('^/(.*\.pyy)$',              pyyscript(dir)),
    ]

  myserver().run()

