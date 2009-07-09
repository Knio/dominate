TAB = '  '#'\t'

class html_tag(object):
    ATTRIBUTE_INLINE  = '__inline'  #Special attribute to output all child elements on one line
    ATTRIBUTE_INVALID = '__invalid' #Special attribute to allow invalid attributes on element
    
    is_single     = False #Tag does not require matching end tag (ex. <hr/>)
    is_pretty     = True  #Text inside the tag should be left as is (ex. <pre>)
    do_inline     = False #Does not insert newlines on all children if True (recursive attribute)
    allow_invalid = False #Allows missing required attributes and invalid attributes if True
    valid         = []    #List of all attributes which are valid for a tag
    required      = []    #List of all attributes which are required for a tag (must be in self.valid)
    default       = {}    #Default values to be used for omitted required attributes
    
    def __init__(self, *args, **kwargs):
        self.attributes = {}
        self.children   = []
        
        #Add child tags
        for i in args:
            self.add(i)
        
        #Check for special attributes. Must be done first and not in the loop!
        if html_tag.ATTRIBUTE_INVALID in kwargs.keys():
            self.allow_invalid = kwargs[html_tag.ATTRIBUTE_INVALID]
            del kwargs[html_tag.ATTRIBUTE_INVALID]
        if html_tag.ATTRIBUTE_INLINE in kwargs.keys():
            self.do_inline = kwargs[html_tag.ATTRIBUTE_INLINE]
            del kwargs[html_tag.ATTRIBUTE_INLINE]
        
        for attribute, value in kwargs.items():
            #Workaround for python's reserved words
            if attribute[0] == '_': attribute = attribute[1:]
            #Workaround for inability to use colon in python keywords
            attribute = attribute.replace('_', ':')
            
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
        for obj in args:
            if isinstance(obj, dummy):
                #Unbox dummy tags
                self.add(*obj.children)
                continue
            elif isinstance(obj, basestring) and len(self.children) > 0 and isinstance(self.children[-1], basestring):
                #Join adjacent strings
                self.children[-1] += obj
                continue
            
            self.children.append(obj)
            if isinstance(obj, html_tag):
                obj.parent = self
        return args[-1]
    
    def tag(self, tag):
        if isinstance(tag, basestring): tag = globals()[tag]
        return [i for i in self.children if type(i) is tag]
    
    def get(self, attr=None, value=None, type=object):
        result = []
        for i in self.children:
            if not isinstance(i, html_tag): continue
            if (not attr or i.attributes.get(attr, None) == value) and isinstance(i, type):
                result.append(i)
            result.extend(i.get(attr, value, type))
        return result
    
    def __getattr__(self, attr):
        return self.__getitem__(attr)
    
    def __getitem__(self, attr):
        try: return self.attributes[attr]
        except KeyError: raise AttributeError
    
    def __setitem__(self, attr, value):
        self.attributes[attr] = value
    
    def __len__(self):
        return len(self.children)
    
    def __iter__(self):
        return self.children.__iter__()
    
    def __add__(self, obj):
        if isinstance(self, dummy):
            return self.__iadd__(obj)
        elif isinstance(obj, dummy):
            return obj.__iadd__(self)
        else:
            return dummy(self, obj)
    
    def __iadd__(self, obj):
        self.add(obj)
        return self
    
    def render(self, indent=1, inline=False):
        inline = self.do_inline or inline
        
        #Workaround for python keywords
        if type(self).__name__[0] == "_":
            name = type(self).__name__[1:]
        else:
            name = type(self).__name__
        s = '<' + name
        
        for attribute, value in self.attributes.items():
            s += ' %s="%s"' % (attribute, str(value))
        
        if self.is_single and not self.children:
            s += ' />'
        else:
            s += '>'
            s += self.render_children(indent, inline)
            
            # if there are no children, or only 1 child that is not an html element, do not add tabs and newlines
            no_children = self.is_pretty and self.children and (not (len(self.children) == 1 and not isinstance(self.children[0], html_tag)))
            
            if no_children and not inline:
                s += '\n'
                s += TAB * (indent - 1)
            s += '</'
            s += name
            s += '>'
        return s
        
    def render_children(self, indent=1, inline=False):
        s = ''
        for i in self.children:
            if isinstance(i, html_tag):
                if not inline and self.is_pretty:
                    s += '\n'
                    s += TAB * indent
                s += i.render(indent + 1, inline)
            else:
                s += str(i)
        return s
    
    def __str__(self):
        return self.render()

################################################################################
######################## Html_tag-based Utility Classes ########################
################################################################################

class single (html_tag): is_single = True
class ugly   (html_tag): is_pretty = False

class dummy  (html_tag):
    '''
    Container for building adjacent tags without a parent. Automatically unboxed
    by add() but sometimes still might be rendered.
    '''
    def render(self, indent=1, inline=False):
        return self.render_children(indent - 1, inline)[1:] #Removes our indent and newline

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
    
    For more on conditional comments see MSDN:
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
        
        s = '<!'
        if not is_revealed:
            s+= '--'
        if has_condition:
            s += '[if %s]>' % self.attributes[comment.ATTRIBUTE_CONDITION]
        
        s += self.render_children(indent, inline)
        
        #XXX: This might be able to be changed to if len(self.children) > 1 since adjacent strings should always be joined
        if any(isinstance(child, html_tag) for child in self.children):
            s += '\n'
            s += TAB * (indent - 1)
        
        if has_condition:
            s += '<![endif]'
        if not is_revealed:
            s += '--'
        s += '>'
        return s
    
    @staticmethod
    def comments2tags(data):
        for search, replace in comment.REPLACE:
            data = search.sub(replace, data)
        return data

class invalid(html_tag):
    def render(self, indent=1, inline=False):
        #XXX: This might affect rendering
        #import warnings
        #warnings.warn("Using invalid tag: %s" % type(self).__name__)
        return html_tag.render(self, indent, inline)

################################################################################
################## Utilities for easily manipulating HTML ######################
################################################################################

class include(html_tag):
    def __init__(self, f):
        fl = file(f, 'rb')
        self.data = fl.read()
        fl.close()
        
    def render(self, n=1, inline=False):
        return self.data
        
def pread(cmd, data='', mode='t'):
    import os
    fin, fout = os.popen4(cmd, mode)
    fin.write(data)
    fin.close()
    return fout.read()
        
class pipe(html_tag):
    def __init__(self, cmd, data=''):
        self.data = pread(cmd, data)
        
    def render(self, indent=1, inline=False):
        return self.data

def _escape(data, quote=False): # stoled from std lib cgi 
    '''Replace special characters "&", "<" and ">" to HTML-safe sequences.
    If the optional flag quote is true, the quotation mark character (")
    is also translated.'''
    data = data.replace("&", "&amp;") # Must be done first!
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    if quote:
        data = data.replace('"', "&quot;")
    return data

class escape(html_tag):
    def render(self, indent=1, inline=False):
        return _escape(html_tag.render_children(self, indent, inline))

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
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        
    def render(self, indent=1, inline=False):
        return self.func(*self.args, **self.kwargs)