TAB = '  '#'    '

COMMON_CORE          = ['class', 'id', 'title']
COMMON_INTERNATIONAL = ['xml:lang', 'dir']
COMMON_EVENT         = ['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup']
COMMON_STYLE         = ['style']
COMMON               = COMMON_CORE + COMMON_INTERNATIONAL + COMMON_EVENT + COMMON_STYLE

ATTRIBUTE_INLINE    = '__inline'
ATTRIBUTE_INVALID   = '__invalid'
ATTRIBUTE_CONDITION = 'condition'

class html_tag(object):
    is_single     = False
    is_pretty     = True
    do_inline     = False #Does not insert newlines on all children if True (recursive attribute)
    allow_invalid = False #Allows missing required attributes and invalid attributes if True
    valid         = []
    required      = []
    default       = {}
    
    def __init__(self, *args, **kwargs):
        self.attributes = {}
        self.children   = []
        
        for i in args:
            self.add(i)
        
        #Check for special attributes. Must do first and not in the loop!
        if ATTRIBUTE_INVALID in kwargs.keys():
            self.allow_invalid = kwargs[ATTRIBUTE_INVALID]
            del kwargs[ATTRIBUTE_INVALID]
        if ATTRIBUTE_INLINE in kwargs.keys():
            self.do_inline = kwargs[ATTRIBUTE_INLINE]
            del kwargs[ATTRIBUTE_INLINE]
        
        for attribute, value in kwargs.items():
            #Workaround for python's reserved words
            if attribute[0] == '_': attribute = attribute[1:]
            #Workaround for inability to use colon in python keywords
            attribute = attribute.replace('_', ':')
            
            if not attribute in self.valid and not self.allow_invalid:
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
                self.add(*obj.children)
                continue
            elif isinstance(obj, str) and len(self.children) > 0 and isinstance(self.children[-1], str):
                self.children[-1] += obj
                continue
            
            self.children.append(obj)
            if isinstance(obj, html_tag):
                obj.parent = self
        return args[-1]
    
    def tag(self, tag):
        if isinstance(tag, str): tag = globals()[tag]
        return [i for i in self.children if type(i) is tag]
    
    def get(self, attr, value, type=object):
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
class dummy  (html_tag): pass #Ignored, automatically unboxed

class comment(html_tag):
    '''
    Normal, one-line comment:
      comment("Hello, comments!")
    
    For IE's "if" statement comments:
      comment(p("Upgrade your browser."), condition='lt IE6')
    '''
    is_single = True
    valid = [ATTRIBUTE_CONDITION]
    
    def render(self, indent=1, inline=False):
        s = '<!--'
        if ATTRIBUTE_CONDITION in self.attributes:
            s += '[%s]>' % self.attributes[ATTRIBUTE_CONDITION]
        
        s += self.render_children(indent, inline)
        
        if any(isinstance(child, html_tag) for child in self.children):
            s += '\n'
            s += TAB * (indent-1)
        
        if ATTRIBUTE_CONDITION in self.attributes:
            s += '<![endif]'
        s += '-->'
        return s

class invalid(html_tag):
    def render(self, indent=1, inline=False):
        #XXX: This might affect rendering
        #import warnings
        #warnings.warn("Using invalid tag: %s" % type(self).__name__)
        return html_tag.render(self, indent, inline)

################################################################################
########################## XHTML 1.1 Tag Specification #########################
################################################################################
#Structure & Header
class base (single):
    valid    = ['href']
    required = ['href']
class body (html_tag): valid = ['onload', 'onunload'] + COMMON
class head (html_tag): valid = ['profile'] + COMMON_INTERNATIONAL
class html (html_tag):
    valid    = ['xmlns', 'xml:lang', 'xmlns:xsi', 'xsi:schemaLocation', 'version'] + COMMON_INTERNATIONAL
    required = ['xmlns']
    default  = {'xmlns': 'http://www.w3.org/1999/xhtml'}
class link (single):   valid = ['href', 'media', 'type', 'charset', 'hreflang', 'rel', 'rev'] + COMMON
class meta (single):
    valid    = ['content', 'name', 'http-equiv', 'scheme'] + COMMON_INTERNATIONAL
    required = ['name']
class script(ugly):
    valid    = ['src', 'type', 'charset', 'defer', 'xml:space'] + COMMON
    required = ['type']
class style(ugly):
    valid    = ['media', 'title', 'type', 'xml:space'] + COMMON_INTERNATIONAL
    required = ['type']
class title(html_tag): valid = COMMON_INTERNATIONAL

#Block elements
class address   (html_tag): valid = COMMON
class blockquote(html_tag): valid = ['cite'] + COMMON
class _del      (html_tag): valid = ['cite', 'datetime'] + COMMON
class div       (html_tag): valid = COMMON
class dl        (html_tag): valid = COMMON
class fieldset  (html_tag): valid = COMMON
class form      (html_tag): valid = ['action', 'method', 'accept', 'accept-charsets', 'enctype', 'onreset', 'onsubmit'] + COMMON
class h1        (html_tag): valid = COMMON
class h2        (html_tag): valid = COMMON
class h3        (html_tag): valid = COMMON
class h4        (html_tag): valid = COMMON
class h5        (html_tag): valid = COMMON
class h6        (html_tag): valid = COMMON
class hr        (single):   valid = COMMON
class ins       (html_tag): valid = ['cite', 'datetime'] + COMMON
class noscript  (html_tag): valid = COMMON
class ol        (html_tag): valid = COMMON
class p         (html_tag): valid = COMMON
class pre       (ugly):     valid = ['xml:space'] + COMMON
class table     (html_tag): valid = ['border', 'cellpadding', 'cellspacing', 'summary', 'width', 'frame', 'rules'] + COMMON
class ul        (html_tag): valid = COMMON

#Inline elements
class a       (html_tag): valid = ['href', 'accesskey', 'charset', 'choords', 'hreflang', 'onblur', 'onfocus', 'rel', 'rev', 'shape', 'tabindex', 'type'] + COMMON
class abbr    (html_tag): valid = COMMON
class acronym (html_tag): valid = COMMON
class b       (html_tag): valid = COMMON
class bdo     (html_tag): valid = ['dir'] + COMMON
class big     (html_tag): valid = COMMON
class br      (single):   valid = COMMON
class button  (html_tag): valid = ['name', 'type', 'value', 'accesskey', 'disabled', 'onblur', 'onfocus', 'tabindex'] + COMMON
class cite    (html_tag): valid = COMMON
class code    (ugly):     valid = COMMON
class dfn     (html_tag): valid = COMMON
class em      (html_tag): valid = COMMON
class i       (html_tag): valid = COMMON
class img     (single):
    valid    = ['alt', 'height', 'src', 'width', 'ismap', 'longdesc', 'usemap'] + COMMON
    required = ['alt', 'src']
    default  = {'alt': ''}
class input   (single):   valid = ['alt', 'checked', 'maxlength', 'name', 'size', 'type', 'value', 'accept', 'accesskey', 'disabled', 'ismap', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'src', 'tabindex', 'usemap'] + COMMON
class kbd     (html_tag): valid = COMMON
class label   (html_tag): valid = ['for', 'accesskey', 'onblur', 'onfocus'] + COMMON
class _map    (html_tag): valid = COMMON
class object  (html_tag): valid = ['classid', 'codebase', 'height', 'name', 'type', 'width', 'archive', 'codetype', 'data', 'declare', 'standby', 'tabindex', 'usemap'] + COMMON
class q       (html_tag): valid = ['cite'] + COMMON
class ruby    (html_tag): valid = COMMON
class samp    (html_tag): valid = COMMON
class select  (html_tag): valid = ['multiple', 'name', 'size', 'disabled', 'onblur', 'onchange', 'onfocus', 'tabindex'] + COMMON
class small   (html_tag): valid = COMMON
class span    (html_tag): valid = COMMON
class strong  (html_tag): valid = COMMON
class sub     (html_tag): valid = COMMON
class sup     (html_tag): valid = COMMON
class textarea(html_tag): valid = ['cols', 'name', 'rows', 'accesskey', 'disabled', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'tabindex'] + COMMON
class tt      (ugly):     valid = COMMON
class var     (html_tag): valid = COMMON

#List item elements
class dd(html_tag): valid = COMMON
class dt(html_tag): valid = COMMON
class li(html_tag): valid = COMMON

#Table content elements
class caption (html_tag): valid = COMMON
class col     (single):   valid = ['align', 'span', 'valign', 'width', 'char', 'charoff'] + COMMON
class colgroup(html_tag): valid = ['align', 'span', 'valign', 'width', 'char', 'charoff'] + COMMON
class tbody   (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON
class td      (html_tag): valid = ['align', 'colspan', 'headers', 'rowspan', 'valign', 'axis', 'char', 'charoff'] + COMMON
class tfoot   (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON
class th      (html_tag): valid = ['abbr', 'align', 'colspan', 'rowspan', 'valign', 'axis', 'char', 'charoff', 'scope'] + COMMON
class thead   (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON
class tr      (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON

#Form fieldset legends
class legend(html_tag): valid = ['accesskey'] + COMMON

#Form menu options
class optgroup(html_tag): valid = ['label', 'disabled'] + COMMON
class option  (html_tag): valid = ['selected', 'value', 'disabled', 'label'] + COMMON

#Map areas
class area(single):
    valid    = ['alt', 'coords', 'href', 'shape', 'accesskey', 'onblur', 'onfocus', 'nohref', 'tabindex'] + COMMON
    required = ['alt']
    default  = {'alt': ''}

#Object parameters
class param(single):
    valid    = ['name', 'value', 'id', 'type', 'valuetype']
    required = ['name']

#Ruby annotations
class rb (html_tag): valid = COMMON
class rbc(html_tag): valid = COMMON
class rp (html_tag): valid = COMMON
class rt (html_tag): valid = ['rbspan'] + COMMON
class rtc(html_tag): valid = COMMON

################################################################################
########################## !!! NON-XHTML SPEC TAGS !!! #########################
################################################################################

class iframe(invalid):
    valid = ['align', 'frameborder', 'height', 'longdesc', 'marginheight', 'marginwidth', 'name', 'scroling', 'src', 'width'] + COMMON_CORE + COMMON_STYLE
class embed (invalid):
    valid = ['src', 'width', 'height', 'align', 'name', 'pluginspage', 'pluginurl', 'hidden', 'href', 'target', 'autostart', 'loop', 'playcount', 'volume', 'controls', 'controller', 'mastersound', 'starttime', 'endtime']
class layer (invalid):
    valid = ['id', 'left', 'top', 'bgcolor', 'width', 'height', 'visibility', 'src']
class u     (invalid): valid = COMMON

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

class escape(html_tag):
    def render(self, indent=1, inline=False):
        return self.escape(html_tag.render_children(self, indent))
        
    def escape(self, s, quote=None): # stoled from std lib cgi 
        '''Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true, the quotation mark character (")
        is also translated.'''
        s = s.replace("&", "&amp;") # Must be done first!
        s = s.replace("<", "&lt;")
        s = s.replace(">", "&gt;")
        if quote:
            s = s.replace('"', "&quot;")
        return s


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