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

import os
import sys
import imp
from http import HTTPError

class pyyserver(object):
  def __init__(self, root='.'):
    self.root = root

  def handle(self, handler, req, res, fname, *args):
    fname = os.path.join(self.root, fname)
    mname = os.path.basename(fname).split('.')[0]
    dname = os.path.dirname(fname)
    sys.path.append(dname)

    if not os.path.exists(fname):
      raise HTTPError(404)

    if not os.path.isfile(fname):
      raise HTTPError(401)
    
    f = open(fname, 'U')
    m = imp.load_module(mname, f, fname, ('.py', 'U', 1))
    
    h = getattr(m, req.method.lower())
    h(handler, req, res, *args)
    
    sys.path.remove(self.root)

