__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy. If not, see
<http://www.gnu.org/licenses/>.
'''

import imp
import re
import os
import string
import sys

from pyy_web import httperror


def RegexResolver(mapping, request):
  for regex, pageclass in mapping:
    match = re.match(regex, request.uri)
    if match:
      request.get.update(match.groupdict())
      return pageclass(request=request)
  raise httperror(404)


def FileHeirarchyResolver(root, request):
  root = os.path.abspath(root)
  if not os.path.isdir(root):
    raise httperror(404)
  
  def resolve_chunk(root, chunks):
    if root is []:
      return False #too deep!
    
    #If we have chunks look at them, otherwise check __init__ for an Index class
    if chunks:
      thedir = os.path.join(root, chunks[0])
      
      #Check if the first chunk is a folder, if so, recursively continue searching inside
      if os.path.isdir(thedir):
        page = resolve_chunk(thedir, chunks[1:])
        if page:
          return page
    else:
      chunks = ['__init__']
    
    thefile = os.path.join(root, '%s.py' % chunks[0])
    
    #Check if the first chunk is a file in the current directory
    if os.path.isfile(thefile):
      #Add file directory to path so relative imports work
      sys.path.insert(0, root);
      
      f = open(thefile, 'U')
      module = imp.load_module(chunks[0], f, thefile, ('.py', 'U', 1))
      f.close()
      
      if len(chunks) > 1:
        #Convert to PascalCasing with hyphens going to underscores
        classname = ''.join(map(string.capitalize, chunks[1].split('_'))).replace('-', '_')
      else:
        classname ='Index'
      
      if hasattr(module, classname):
        request.uri = '/' + '/'.join(chunks[2:])
        return getattr(module, classname)(request=request)
    return False
  
  page = resolve_chunk(root, filter(None, request.uri.split('/')))
  if not page:
    raise httperror(404)
  
  return page
 