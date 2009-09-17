import os
import sys
import imp
from http import HTTPError

class pyyserver(object):
  def __init__(self, root='.'):
    self.root = root

  def handle(self, handler, req, res, fname):
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
    
    m.main(handler, req, res)
    
    sys.path.remove(dname)

