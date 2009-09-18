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

class pyy_tag(object):
    TAB = '  '#'\t'
    
    is_single = False #Tag does not require matching end tag (ex. <hr/>)
    is_pretty = True  #Text inside the tag should be left as-is (ex. <pre>)
    
    def __init__(self, *args, **kwargs):
        self.attributes = {}
        self.children   = []
        self.parent     = None
        self.document   = None
        
        #Does not insert newlines on all children if True (recursive attribute)
        self.do_inline = kwargs.pop('__inline', False)
        
        #Add child elements
        self.add(*args)
        
        for attr, value in kwargs.items():
            self.set_attribute(*pyy_tag.clean_pair(attr, value))
    
    
    def set_attribute(self, attr, value):
        '''
        Add or update the value of an attribute.
        '''
        self.attributes[attr] = value
    __setitem__ = set_attribute
    
    def setdocument(self, doc):
        self.document = doc
        for i in self.children:
            if not isinstance(i, pyy_tag): return
            i.setdocument(doc)

    def add(self, *args):
        for obj in args:
            if   isinstance(obj, basestring):
                if self.document and self.document.doctype:
                    self.document.doctype.validate(self, obj)
                self.children.append(obj)
            elif isinstance(obj, pyy_tag):
                if self.document and self.document.doctype:
                    self.document.doctype.validate(self, obj)
                self.children.append(obj)
                obj.parent = self
                obj.setdocument(self.document)
            elif hasattr(obj, '__iter__'):
                for subobj in obj:
                    self.add(subobj)
            else: # wtf is it?
                raise ValueError('%r not a tag or string' % obj)
                self.children.append(obj)
        
        if len(args) > 1:
            return args
        elif len(args) == 1:
            return args[0]
    
    def get(self, tag=None, **kwargs):
        '''
        Recursively searches children for tags of a certain type with matching attributes.
        '''
        #Stupid workaround since we can not use pyy_tag in the method declaration
        if tag is None: tag = pyy_tag
        
        results = []
        for child in self.children:
            if (isinstance(tag, basestring) and type(child).__name__ == tag) or (not isinstance(tag, basestring) and isinstance(child, tag)):
                if all(pyy_tag.clean_attribute(attribute) in child.attributes and child.attributes[pyy_tag.clean_attribute(attribute)] == value for attribute, value in kwargs.iteritems()):
                    #If the child is of correct type and has all attribute and values in kwargs add as a result
                    results.append(child)
            if isinstance(child, pyy_tag):
                #If the child is an pyy_tag extend the search down its children
                results.extend(child.get(tag, **kwargs))
        return results
    
    
    def __getitem__(self, attr):
        '''
        Returns the stored value of the specified attribute (if it exists).
        '''
        try: return self.attributes[attr]
        except KeyError: raise AttributeError('Attribute "%s" does not exist.' % attr)
    __getattr__ = __getitem__
    
    def __len__(self):
        '''
        Number of child elements.
        '''
        return len(self.children)

    def __nonzero__(self):
        'Hack for "if x" and __len__'
        return True
      
    def __iter__(self):
        '''
        Iterates over child elements.
        '''
        return self.children.__iter__()
    
    def __contains__(self, item):
        '''
        Checks recursively if item is in children tree. Accepts both a string and a class.
        '''
        return bool(self.get(item))
    
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
        
        #Workaround for python keywords and standard classes/methods (del, object, input)
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
            no_children = self.is_pretty and self.children and (not (len(self.children) == 1 and not isinstance(self.children[0], pyy_tag)))
            
            if no_children and not inline:
                rendered += '\n'
                rendered += pyy_tag.TAB * (indent - 1)
            rendered += '</'
            rendered += name
            rendered += '>'
        
        return rendered
    
    #String and unicode representations are the same as render()
    def __unicode__(self):
        return self.render()
    __str__ = __unicode__
    
    def render_children(self, indent=1, inline=False):
        children = ''
        for child in self.children:
            if isinstance(child, pyy_tag):
                if not inline and self.is_pretty:
                    children += '\n'
                    children += pyy_tag.TAB * indent
                children += child.render(indent + 1, inline)
            else:
                children += str(child)
        return children
    
    def __repr__(self):
        name = '%s.%s' % (self.__module__, type(self).__name__)
        
        attributes_len = len(self.attributes)
        attributes = '%s attribute' % attributes_len
        if attributes_len != 1: attributes += 's'
        
        children_len = len(self.children)
        children = '%s child' % children_len
        if children_len != 1: children += 'ren'
        
        return '<%s: %s, %s>' % (name, attributes, children)
    
    @staticmethod
    def clean_attribute(attribute):
        #Workaround for python's reserved words
        if attribute[0] == '_': attribute = attribute[1:]
        #Workaround for inability to use colon in python keywords
        return attribute.replace('_', ':').lower()
    
    @staticmethod
    def clean_pair(attribute, value):
        attribute = pyy_tag.clean_attribute(attribute)
        if value is True:
            value = attribute
        return (attribute, value)

# escape() is used in render
from utils import escape

