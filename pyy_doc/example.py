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

import types

from pyy_html       import *
from pyy_html.html  import *
from pyy_html.util  import *


class pyy_doc(document):
  def __init__(self, module):
    self.module = module
    document.__init__(self, title='%s - docs' % module)
    self.generate()

  def generate(self, show_hidden=False, trim_doc=100):
    mod = __import__(self.module)
    
    #Module Header
    self += div(h2('Module %s' % self.module), pre(escape(str(mod.__doc__).strip())))
    
    #Sections
    con, mod, cla, fun = self.add(div(h3('Constants') , table()), \
                                  div(h3('Submodules'), table()), \
                                  div(h3('Classes')   , table()), \
                                  div(h3('Functions') , table()))
    constants = con[1].add(tbody())
    modules   = mod[1].add(tbody())
    classes   = cla[1].add(tbody())
    functions = fun[1].add(tbody())
    
    #Add module items to respective sections
    for k, v in mod.__dict__.items():
      if k.startswith('_') and not show_hidden: continue
      if type(v) is types.ModuleType:
        modules   += tr(td(a(k, href=k), __inline=True), td(escape(str(v.__doc__).strip()[:trim_doc]), __inline=True))
      elif type(v) is type:
        classes   += tr(td(a(k, href=k), __inline=True), td(escape(str(v.__doc__).strip()[:trim_doc]), __inline=True))
      elif type(v) is types.FunctionType:
        functions += tr(td(a(k+'()', href=k), __inline=True), td(escape(str(v.__doc__).strip()[:trim_doc]), __inline=True))
      else:
        constants += tr(td(k), td(escape(repr(v)), __inline=True))



def main(handler, req, res, *args):
  print args
  d = pyy_doc(args[0])
  
  res.headers['Content-Type'] = 'text/html'
  res.body = d.render()
  





