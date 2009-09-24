import types


from pyy_html       import *
from pyy_html.html  import *
from pyy_html.util  import *

class pyy_doc(document):
  def __init__(self, module):
    self.module = module
    document.__init__(self, '%s - docs' % module, None)
    self.generate()

  def generate(self):
    mod = __import__(self.module)
    
    d = div(h2('Module %s' % self.module), pre(escape(str(mod.__doc__))))
    self += d

    constants = self.add(div(h3('Constants')))
    modules   = self.add(div(h3('Submodules')))
    classes   = self.add(div(h3('Classes')))
    functions = self.add(div(h3('Functions')))
    
    constants += table()
    modules   += table()
    classes   += table()
    functions += table()
    
    
    for k, v in mod.__dict__.items():
      if k.startswith('_'): continue
      if type(v) is types.ModuleType:
        modules.get()[1] += tr(td(a(k, href=k)), td(escape(str(v.__doc__)[:100])))
      elif type(v) is type:
        classes.get()[1] += tr(td(a(k,href=k)), td(escape(str(v.__doc__)[:100])))
      elif type(v) is types.FunctionType:
        functions.get()[1] += tr(td(a(k+'()',href=k)), td(escape(str(v.__doc__)[:100])))
      else:
        print k, v
        constants.get()[1] += tr(td(k), td(escape(repr(v))))   



def main(handler, req, res, *args):
  print args
  d = pyy_doc(args[0])
  
  res.headers['Content-Type'] = 'text/html'
  res.body = d.render()
  
  
  
  


