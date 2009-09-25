'''
HTML tag classes.
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

from pyy_tag  import pyy_tag
from dom1core import dom1core

class html_tag(pyy_tag, dom1core):
  def __init__(self, *args, **kwargs):
    #Allows missing required attributes and invalid attributes if True
    self.allow_invalid = kwargs.pop('__invalid', False)
    pyy_tag.__init__(self, *args, **kwargs)


class single(html_tag): is_single = True
class ugly  (html_tag): is_pretty = False


################################################################################
############################### Html Tag Classes ###############################
################################################################################

class a           (html_tag): pass
class abbr        (html_tag): pass
class acronym     (html_tag): pass
class address     (html_tag): pass
class applet      (html_tag): pass
class area        (single):   pass
class article     (html_tag): pass
class aside       (html_tag): pass
class audio       (html_tag): pass
class b           (html_tag): pass
class bb          (html_tag): pass
class base        (single):   pass
class basefont    (single):   pass
class bdo         (html_tag): pass
class big         (html_tag): pass
class blockquote  (html_tag): pass
class body        (html_tag): pass
class br          (single):   pass
class button      (html_tag): pass
class canvas      (html_tag): pass
class caption     (html_tag): pass
class center      (html_tag): pass
class cite        (html_tag): pass
class code        (html_tag): pass
class col         (single):   pass
class colgroup    (html_tag): pass
class command     (html_tag): pass
class datagrid    (html_tag): pass
class datalist    (html_tag): pass
class datatemplate(html_tag): pass
class dd          (html_tag): pass
class del_        (html_tag): pass
class details     (html_tag): pass
class dialog      (html_tag): pass
class dir         (html_tag): pass
class div         (html_tag): pass
class dfn         (html_tag): pass
class dl          (html_tag): pass
class dt          (html_tag): pass
class em          (html_tag): pass
class embed       (html_tag): pass
class eventsource (html_tag): pass
class fieldset    (html_tag): pass
class figure      (html_tag): pass
class font        (html_tag): pass
class footer      (html_tag): pass
class form        (html_tag): pass
class frame       (single):   pass
class frameset    (html_tag): pass
class h1          (html_tag): pass
class h2          (html_tag): pass
class h3          (html_tag): pass
class h4          (html_tag): pass
class h5          (html_tag): pass
class h6          (html_tag): pass
class head        (html_tag): pass
class header      (html_tag): pass
class hgroup      (html_tag): pass
class hr          (single):   pass
class html        (html_tag): pass
class i           (html_tag): pass
class iframe      (html_tag): pass
class img         (single):   pass
class input_      (single):   pass
class ins         (html_tag): pass
class isindex     (html_tag): pass
class kbd         (html_tag): pass
class keygen      (html_tag): pass
class label       (html_tag): pass
class legend      (html_tag): pass
class li          (html_tag): pass
class link        (single):   pass
class math        (html_tag): pass
class mark        (html_tag): pass
class map_        (html_tag): pass
class menu        (html_tag): pass
class meter       (html_tag): pass
class meta        (single):   pass
class nav         (html_tag): pass
class nest        (html_tag): pass
class noframes    (html_tag): pass
class noscript    (html_tag): pass
class object_     (html_tag): pass
class ol          (html_tag): pass
class optgroup    (html_tag): pass
class option      (html_tag): pass
class output      (html_tag): pass
class p           (html_tag): pass
class param       (single):   pass
class pre         (ugly):     pass
class progress    (html_tag): pass
class q           (html_tag): pass
class rb          (html_tag): pass
class rbc         (html_tag): pass
class rt          (html_tag): pass
class rtc         (html_tag): pass
class rp          (html_tag): pass
class ruby        (html_tag): pass
class rule        (html_tag): pass
class s           (html_tag): pass
class samp        (html_tag): pass
class script      (ugly):     pass
class section     (html_tag): pass
class select      (html_tag): pass
class small       (html_tag): pass
class source      (html_tag): pass
class span        (html_tag): pass
class strike      (html_tag): pass
class strong      (html_tag): pass
class style       (html_tag): pass
class sub         (html_tag): pass
class sup         (html_tag): pass
class svg         (html_tag): pass
class table       (html_tag): pass
class tbody       (html_tag): pass
class td          (html_tag): pass
class textarea    (html_tag): pass
class tfoot       (html_tag): pass
class th          (html_tag): pass
class thead       (html_tag): pass
class time        (html_tag): pass
class title       (html_tag): pass
class tr          (html_tag): pass
class tt          (html_tag): pass
class u           (html_tag): pass
class ul          (html_tag): pass
class var         (html_tag): pass
class video       (html_tag): pass
class xmp         (html_tag): pass

class comment(html_tag):
  '''
  Normal, one-line comment:
    >>> print comment("Hello, comments!")
    <!--Hello, comments!-->
  
  For IE's "if" statement comments:
    >>> print comment(p("Upgrade your browser."), condition='lt IE6')
    <!--[if lt IE6]><p>Upgrade your browser.</p><![endif]-->
  
  Downlevel conditional comments:
    >>> print comment(p("You are using a ", em("downlevel"), " browser."), condition='false', downlevel='revealed')
    <![if false]><p>You are using a <em>downlevel</em> browser.</p><![endif]>
  
  For more on conditional comments see:
    http://msdn.microsoft.com/en-us/library/ms537512(VS.85).aspx
  '''
  ATTRIBUTE_CONDITION = 'condition'
  ATTRIBUTE_DOWNLEVEL = 'downlevel' #Valid values are 'hidden' or 'revealed'
  
  def render(self, indent=1, inline=False):
    has_condition = comment.ATTRIBUTE_CONDITION in self.attributes
    is_revealed   = comment.ATTRIBUTE_DOWNLEVEL in self.attributes and self.attributes[comment.ATTRIBUTE_DOWNLEVEL] == 'revealed'
    
    rendered = '<!'
    if not is_revealed:
      rendered += '--'
    if has_condition:
      rendered += '[if %s]>' % self.attributes[comment.ATTRIBUTE_CONDITION]
    
    rendered += self.render_children(indent - 1, inline)
    
    #TODO: This might be able to be changed to if len(self.children) > 1 since adjacent strings should always be joined
    if any(isinstance(child, pyy_tag) for child in self):
      rendered += '\n'
      rendered += html_tag.TAB * (indent - 1)
    
    if has_condition:
      rendered += '<![endif]'
    if not is_revealed:
      rendered += '--'
    rendered += '>'
    
    return rendered
  
  @staticmethod
  def comments2tags(data):
    '''
    Changes <!--comments--> to <comment>tags</comment> for easy parsing.
    '''
    import re
    
    REPLACE = [
      (re.compile(r'<!--\[if (.*?)\]>(.*?)<!\[endif\]-->', re.S), r'<comment condition="\1">\2</comment>'),
      (re.compile(r'<!--(.*?)-->', re.S)                        , r'<comment>\1</comment>'),
      (re.compile(r'<!\[if (.*?)\]>(.*?)<!\[endif\]>', re.S)    , r'<comment condition="\1" downlevel="revealed">\2</comment>'),
    ]
    
    for search, replace in REPLACE:
      data = search.sub(replace, data)
    return data


