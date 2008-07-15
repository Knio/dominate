TAB = ''#'    '

class html(object):
    single  = False
    child   = None
    pretty  = True
    def __init__(self, *args, **kwargs):
        self.attributes = kwargs
        self.children   = []
        
        if '_class' in self.attributes: # work around for python keyword
            self.attributes['class'] = self.attributes['_class']
            del self.attributes['_class']
        
        for i in args:
            self.add(i)
        
    def add(self, *args):
        for obj in args:
            if self.child and not isinstance(obj, self.child):
                obj = self.child(obj)
            self.children.append(obj)
            if isinstance(obj, html):
                obj.parent = self
        return args[-1]
    
    def tag(self, tag):
        if isinstance(tag, str): tag = globals()[tag]
        return [i for i in self.children if type(i) is tag]
    
    def get(self, attr, value, type=object):
        result = []
        for i in self.children:
            if not isinstance(i, html): continue
            if (not attr or i.attributes.get(attr,None) == value) and isinstance(i,type):
                result.append(i)
            result.extend(i.get(attr,value,type))
        return result
    
    def __getattr__(self, attr):
        try: return self.attributes[attr]
        except KeyError: raise AttributeError
    
    def __add__(self, obj):
        self.add(obj)
        return self
    
    def __iadd__(self, obj):
        self.add(obj)
        return self
    
    def render(self, n=1):
        s = '<'
        s += type(self).__name__
        for k, v in self.attributes.items():
            s += ' %s="%s"' % (k, str(v))
        if self.single and not self.children:
            s += ' />'
        else:
            # if there are no children, or only 1 child that is not an html element, do not add tabs and newlines
            nl = self.pretty and self.children and (not (len(self.children) == 1 and not isinstance(self.children[0], html)))
            
            s += '>'
            s += self.render_children(n)
            
            if nl:
                s += '\n'
                s += TAB*(n-1)
            s += '</'
            s += type(self).__name__
            s += '>'
        return s
        
    def render_children(self, n=1):
        
        if not self.pretty:
            return ''.join(map(str, self.children))
            
        s = ''
        for i in self.children:
                if isinstance(i, html):
                    s += '\n'
                    s += TAB*n
                    s += i.render(n+1)
                else:
                    s += str(i)
        return s
    
    def __str__(self):
        return self.render()

    def __iadd__(self, obj):
        self.add(obj)
        return self

class single(html):     single = True
class hr    (single):   pass
class link  (single):   pass
class br    (single):   pass

class body  (html):     pass
class head  (html):     pass
class title (html):     pass
class style (html):     pass
class script(html):     pretty = False
class form  (html):     pass
class input (html):     pass

class img   (single):     pass

class h1    (html):     pass
class h2    (html):     pass
class h3    (html):     pass
class h4    (html):     pass
class h5    (html):     pass
class font  (html):     pass
class strong(html):     pass
class div   (html):     pass
class span  (html):     pass
class p     (html):     pass
class a     (html):     pass
class td    (html):     pass
class th    (html):     pass
class tr    (html):     pass
class table (html):     pass
class tbody (html):     pass
class ol    (html):     pass
class ul    (html):     pass
class li    (html):     pass
class label (html):     pass
class pre   (html):
    pretty = False
    def render(self, n=1):
        return html.render(self, 0)

class include(html):
    def __init__(self, f):
        fl = file(f, 'rb')
        self.data = fl.read()
        fl.close()
        
    def render(self, n=1):
        return self.data
        
def pread(cmd, data='', mode='t'):
    import os
    fin, fout = os.popen4(cmd, mode)
    fin.write(data)
    fin.close()
    return fout.read()
        
class pipe(html):
    def __init__(self, cmd, data=''):
        self.data = pread(cmd, data)
        
    def render(self, n=1):
        return self.data

class escape(html):
    def render(self, n=1):
        return self.escape(html.render_children(self, n))
        
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





