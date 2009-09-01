import os
import sys
import imp
from http import HTTPError

class pyyserver(object):
  def __init__(self):
    pass

  def handle(self, handler, req, res, fname):
    
    mname = os.path.basename(fname).split('.')[0]
    dname = os.path.dirname(fname)
    sys.path.append(dname)

    if not os.path.exists(fname):
      raise HTTPError(404)

    if not os.path.isfile(fname):
      raise HTTPError(401)
    
    f = open(fname, 'U')
    
    try:
      m = imp.load_module(mname, f, fname, ('.py', 'U', 1))
      m.main(handler, req, res)
    except Exception, e:
      raise HTTPError(500, e)
    finally:
      sys.path.remove(dname)

