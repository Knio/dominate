TAB = '    '

class html(object):
    single  = False
    child   = None
    def __init__(self, *args, **kwargs):
        self.attributes = kwargs
        self.children   = []
        for i in args:
            self.add(i)

    def add(self, obj):
        if self.child and not isinstance(obj, self.child):
            obj = self.child(obj)
        self.children.append(obj)
        return obj
    
    def render(self, n=1):
        s = '<'
        s += type(self).__name__
        for k, v in self.attributes.items():
            s += ' %s="%s"' % (k, str(v))
        if self.single and not self.children:
            s += ' />'
        else:
            # if there are no children, or only 1 child that is not an html element, do not add tabs and newlines
            nl = self.children and (not (len(self.children) == 1 and not isinstance(self.children[0], html)))
            
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
class form  (html):     pass
class input (html):     pass

class img   (html):     pass

class h1    (html):     pass
class h2    (html):     pass
class h3    (html):     pass
class h4    (html):     pass
class h5    (html):     pass
class font  (html):     pass
class div   (html):     pass
class span  (html):     pass
class p     (html):     pass
class a     (html):     pass
class b     (html):     pass
class td    (html):     pass
class th    (html):     pass
class tr    (html):     pass
class table (html):     pass
class pre   (html):
    def render(self, n=1):
        return html.render(self, 0)

class include(html):
    def __init__(self, f):
        fl = file(f, 'rb')
        self.data = fl.read()
        fl.close()
        
    def render(self, n=1):
        return self.data
        
class pipe(html):
    def __init__(self, cmd, data=''):
        import os
        fin, fout = os.popen4(cmd)
        fin.write(data)
        fin.close()
        self.data = fout.read()
        
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