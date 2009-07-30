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

class html_tag(object):
    ATTRIBUTE_INLINE  = '__inline'  #Special attribute to output all child elements on one line
    ATTRIBUTE_INVALID = '__invalid' #Special attribute to allow invalid attributes on element
    
    TAB = '  '#'\t'
    
    is_single     = False #Tag does not require matching end tag (ex. <hr/>)
    is_pretty     = True  #Text inside the tag should be left as-is (ex. <pre>)
    do_inline     = False #Does not insert newlines on all children if True (recursive attribute)
    allow_invalid = False #Allows missing required attributes and invalid attributes if True
    valid         = []    #List of all attributes which are valid for a tag
    required      = []    #List of all attributes which are required for a tag (must be in self.valid)
    default       = {}    #Default values to be used for omitted required attributes
    
    def __init__(self, *args, **kwargs):
        self.attributes = {}
        self.children   = []
        
        #Add child elements
        self.add(*args)
        
        #Check for special attributes. Must be done first and not in the loop!
        if html_tag.ATTRIBUTE_INVALID in kwargs.keys():
            self.allow_invalid = kwargs[html_tag.ATTRIBUTE_INVALID]
            del kwargs[html_tag.ATTRIBUTE_INVALID]
        if html_tag.ATTRIBUTE_INLINE in kwargs.keys():
            self.do_inline = kwargs[html_tag.ATTRIBUTE_INLINE]
            del kwargs[html_tag.ATTRIBUTE_INLINE]
        
        for attribute, value in kwargs.items():
            attribute = html_tag.clean_attribute(attribute)
            
            if attribute not in self.valid and not self.allow_invalid:
                raise AttributeError("Invalid attribute '%s'." % attribute)
            
            self.attributes[attribute] = value
        
        #Check for missing required attributes
        missing = set(self.required) - set(self.attributes)
        
        #Attempt to assign default values to missing required attributes
        for attribute in missing:
            if attribute in self.default:
                self.attributes[attribute] = self.default[attribute]
        
        #Recheck for missing attributes
        missing = set(self.required) - set(self.attributes)
        
        if missing and not self.allow_invalid:
            raise AttributeError("Missing required attribute(s): '%s'" % ','.join(missing))
        
    def add(self, *args):
        if self.is_single and args:
            raise ValueError("<%s> tag can not have child elements." % type(self).__name__)
        
        for obj in args:
            if isinstance(obj, basestring) and len(self.children) > 0 and isinstance(self.children[-1], basestring):
                #Join adjacent strings
                self.children[-1] += obj
            elif not isinstance(obj, html_tag) and hasattr(obj, '__iter__'):
                #Add all items of an interable as long as they are not html tags
                for subobj in obj:
                    self.add(subobj)
            else:
                self.children.append(obj)
                if isinstance(obj, html_tag):
                    #DOM API: add link to parent node
                    obj.parentNode = self
        
        if len(args) > 1:
            return args
        elif len(args) == 1:
            return args[0]
    
    def get(self, tag=None, **kwargs):
        '''
        Recursively searches children for tags of a certain type with matching attributes.
        '''
        #Stupid workaround since we can not use html_tag in the method declaration
        if not tag: tag = html_tag
        
        results = []
        for child in self.children:
            if (isinstance(tag, basestring) and type(child).__name__ == tag) or (not isinstance(tag, basestring) and isinstance(child, tag)):
                if all(html_tag.clean_attribute(attribute) in child.attributes and child.attributes[html_tag.clean_attribute(attribute)] == value for attribute, value in kwargs.iteritems()):
                    #If the child is of correct type and has all attribute and values in kwargs add as a result
                    results.append(child)
            if isinstance(child, html_tag):
                #If the child is an html_tag extend the search down its children
                results.extend(child.get(tag, **kwargs))
        return results
    
    def getElementById(self, id):
        '''
        DOM API: Returns single element with matching id value.
        '''
        results = self.get(id=id)
        if len(results) > 1:
            raise ValueError('Multiple tags with id "%s" found.' % id)
        elif results:
            return results[0]
        else:
            return None
    
    def getElementsByTagName(self, name):
        '''
        DOM API: Returns all tags that match name.
        '''
        if isinstance(name, basestring):
            return self.get(name)
        else:
            return None
    
    def __getitem__(self, attr):
        '''
        Returns the stored value of the specified attribute (if it exists).
        '''
        try: return self.attributes[attr]
        except KeyError: raise AttributeError('Attribute "%s" does not exist.' % attr)
    __getattr__ = __getitem__
    
    def __setitem__(self, attr, value):
        '''
        Add or update the value of an attribute.
        '''
        self.attributes[attr] = value
    
    def __len__(self):
        '''
        Number of child elements.
        '''
        return len(self.children)
    
    def __iter__(self):
        '''
        Iterates over child elements.
        '''
        return self.children.__iter__()
    
    def __contains__(self, item):
        '''
        Checks recursively if item is in children tree. Accepts both a string and class.
        '''
        return bool(self.get(item))
    
    def appendChild(self, obj):
        '''
        DOM API: Add an item to the end of the children list.
        '''
        self.add(obj)
        return self
    append = appendChild
    
    def extend(self, obj_list):
        '''
        Extend the children list by adding all the items in the given list.
        '''
        self.add(*obj_list)
        return self
    
    def insert(self, position, obj):
        '''
        Insert an item into the children list at the given position.
        '''
        if self.is_single:
            raise ValueError("<%s> tag can not contain child elements." % type(self).__name__)
        
        self.children.insert(position, obj)
        return self
    
    def __iadd__(self, obj):
        '''
        Reflexive binary addition simply adds tag as a child.
        '''
        self.add(obj)
        return self
    
    def render(self, indent=1, inline=False):
        '''
        Returns a well-formatted string representation of the tag and renderings
        of all its child tags.
        '''
        inline = self.do_inline or inline
        
        #Workaround for python keywords
        if type(self).__name__[-1] == "_":
            name = type(self).__name__[:-1]
        else:
            name = type(self).__name__
        rendered = '<' + name
        
        for attribute, value in self.attributes.items():
            rendered += ' %s="%s"' % (attribute, escape.escape(str(value), True))
        
        if self.is_single:
            rendered += ' />'
        else:
            rendered += '>'
            rendered += self.render_children(indent, inline)
            
            # if there are no children, or only 1 child that is not an html element, do not add tabs and newlines
            no_children = self.is_pretty and self.children and (not (len(self.children) == 1 and not isinstance(self.children[0], html_tag)))
            
            if no_children and not inline:
                rendered += '\n'
                rendered += html_tag.TAB * (indent - 1)
            rendered += '</'
            rendered += name
            rendered += '>'
        
        return rendered
    
    #String and unicode representations are the same as render()
    __str__ = __unicode__ = render
    
    def render_children(self, indent=1, inline=False):
        children = ''
        for child in self.children:
            if isinstance(child, html_tag):
                if not inline and self.is_pretty:
                    children += '\n'
                    children += html_tag.TAB * indent
                children += child.render(indent + 1, inline)
            else:
                children += str(child)
        return children
    
    def __repr__(self):
        name = '%s.%s' % (self.__module__, type(self).__name__)
        
        attributes_len = len(self.attributes)
        attributes = '%s attribute' % attributes_len
        if attributes_len > 1: attributes += 's'
        
        children_len = len(self.children)
        children = '%s child' % children_len
        if children_len > 1: children += 'ren'
        
        return '<%s: %s, %s>' % (name, attributes, children)
    
    @staticmethod
    def clean_attribute(attribute):
        #Workaround for python's reserved words
        if attribute[0] == '_': attribute = attribute[1:]
        #Workaround for inability to use colon in python keywords
        return attribute.replace('_', ':').lower()

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

# TODO these utilities should be somewhere else.

class include(html_tag):
    def __init__(self, f):
        fl = file(f, 'rb')
        self.data = fl.read()
        fl.close()
    
    def render(self, n=1, inline=False):
        return self.data

class pipe(html_tag):
    def __init__(self, cmd, data='', mode='t'):
        import os
        fin, fout = os.popen4(cmd, mode)
        fin.write(data)
        fin.close()
        self.data = fout.read()
    
    def render(self, indent=1, inline=False):
        return self.data

class escape(html_tag):
    @staticmethod
    def escape(data, quote=False): # stoled from std lib cgi
        '''
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true, the quotation mark character (")
        is also translated.
        '''
        data = data.replace("&", "&amp;") # Must be done first!
        data = data.replace("<", "&lt;")
        data = data.replace(">", "&gt;")
        if quote:
            data = data.replace('"', "&quot;")
        return data
    
    def render(self, indent=1, inline=False):
        return self.escape(html_tag.render_children(self, indent, inline))

_unescape = {'quot' :34,
             'amp'  :38,
             'lt'   :60,
             'gt'   :62,
             'nbsp' :32,
             
             # more here
             
             'yuml' :255
             }

def unescape(data):
    import re
    cc = re.compile('&(?:(?:#(\d+))|([^;]+));')
    
    result = []
    m = cc.search(data)
    while m:
        result.append(data[0:m.start()])
        d = m.group(1)
        if d:
            d = int(d)
            result.append(d > 255 and unichr(d) or chr(d))
        else:
            d = _unescape.get(m.group(2), ord('?'))
            result.append(d > 255 and unichr(d) or chr(d))
            
        data = data[m.end():]
        m = cc.search(data)
    
    result.append(data)
    return ''.join(result)

class lazy(html_tag):
    '''
    Delays function execution until render
    '''
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        
    def render(self, indent=1, inline=False):
        return self.func(*self.args, **self.kwargs)
