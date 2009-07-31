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

from pyy.pyy_tag    import pyy_tag
from pyy.dom1core   import dom1core

class html_tag(pyy_tag, dom1core):
    
    valid         = []    #List of all attributes which are valid for a tag
    required      = []    #List of all attributes which are required for a tag (must be in self.valid)
    default       = {}    #Default values to be used for omitted required attributes
    allow_invalid = False #Allows missing required attributes and invalid attributes if True
    

    def __init__(self, *args, **kwargs):
        self.allow_invalid = kwargs.pop('__invalid', False)
        pyy_tag.__init__(self, *args, **kwargs)
        
        for attr, val in self.default.iteritems():
            if attr in self.attributes: continue
            self.set_attribute(attr, value)

        #Check for missing required attributes
        missing = [i for i in self.required if i not in self.attributes]
        if missing: 
            raise AttributeError("Missing required attribute(s): '%s'" % ','.join(missing))


    def set_attribute(self, attr, value):
        if attribute not in self.valid and not self.allow_invalid:
            raise AttributeError("Invalid attribute '%s'." % attribute)
        return pyy_tag.set_attribute(attr, value)
    



################################################################################
######################## Html_tag-based Utility Classes ########################
################################################################################

class single(html_tag): is_single = True
class ugly  (html_tag): is_pretty = False

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
    import re
    
    ATTRIBUTE_CONDITION = 'condition'
    ATTRIBUTE_DOWNLEVEL = 'downlevel' #Valid values are 'hidden' or 'revealed'
    REPLACE = [
        (re.compile(r'<!--\[if (.*?)\]>(.*?)<!\[endif\]-->', re.S), r'<comment condition="\1">\2</comment>'),
        (re.compile(r'<!--(.*?)-->', re.S)                        , r'<comment>\1</comment>'),
        (re.compile(r'<!\[if (.*?)\]>(.*?)<!\[endif]>', re.S)     , r'<comment condition="\1" downlevel="revealed">\2</comment>'),
    ]
    
    valid = [ATTRIBUTE_CONDITION, ATTRIBUTE_DOWNLEVEL]
    
    def __init__(self, *args, **kwargs):
        html_tag.__init__(self, *args, **kwargs)
        #Preserve whitespace if we are not a conditional comment
        self.is_pretty = comment.ATTRIBUTE_CONDITION not in self.attributes
    
    def render(self, indent=1, inline=False):
        has_condition = comment.ATTRIBUTE_CONDITION in self.attributes
        is_revealed = comment.ATTRIBUTE_DOWNLEVEL in self.attributes and self.attributes[comment.ATTRIBUTE_DOWNLEVEL] == 'revealed'
        
        rendered = '<!'
        if not is_revealed:
            rendered += '--'
        if has_condition:
            rendered += '[if %s]>' % self.attributes[comment.ATTRIBUTE_CONDITION]
        
        rendered += self.render_children(indent, inline)
        
        #XXX: This might be able to be changed to if len(self.children) > 1 since adjacent strings should always be joined
        if any(isinstance(child, html_tag) for child in self.children):
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
        for search, replace in comment.REPLACE:
            data = search.sub(replace, data)
        return data


