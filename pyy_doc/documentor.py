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

from pyy_html      import *
from pyy_html.util import *

class pyy_doc(document):
  def __init__(self, module, **kwargs):
    self.module      = module
    self.description = ''
    self.submodules  = {}
    self.classes     = {}
    self.functions   = {}
    self.constants   = {}
    
    document.__init__(self, title='%s - Documentation' % module, **kwargs)
    
    self.generate()
  
  def generate(self, show_hidden=False, trim_doc=100):
    module = __import__(self.module)
    
    #Module Header
    self.description = str(module.__doc__).strip()
    self += div(h1('Module %s' % self.module), pre(escape(self.description)), id='module-header')
    
    #Set up sections and get vars that point to respective tbody elements
    con = self.add(div(h2('Constants') , table(tbody()), id='module-constants' , _class='module-section'))[1][0]
    sub = self.add(div(h2('Submodules'), table(tbody()), id='module-submodules', _class='module-section'))[1][0]
    cls = self.add(div(h2('Classes')   , table(tbody()), id='module-classes'   , _class='module-section'))[1][0]
    fun = self.add(div(h2('Functions') , table(tbody()), id='module-functions' , _class='module-section'))[1][0]
    
    #Add module items to respective dictionaries and tables
    for name, item in module.__dict__.items():
      if name.startswith('_') and not show_hidden: continue
      if type(item) is types.ModuleType:
        self.submodules[name] = str(item.__doc__).strip()
        sub += tr(td(a(name, href='%s.%s.html'%(module,name)), __inline=True), td(escape(self.submodules[name][:trim_doc]), __inline=True))
      elif type(item) is type:
        self.classes[name] = str(item.__doc__).strip()
        cls += tr(td(name), td(escape(self.classes[name][:trim_doc]), __inline=True))
      elif type(item) is types.FunctionType:
        self.functions[name] = str(item.__doc__).strip()
        fun += tr(td(name), td(escape(self.functions[name][:trim_doc]), __inline=True))
      else:
        self.constants[name] = repr(item)
        con += tr(td(name), td(self.constants[name]))
