from xhtml11 import *
from web     import *

class cookie(object):
    def __init__(self, name, value, perm=False):
        self.name   = name
        self.value  = value
        self.perm   = perm
    
    def render(self):
        if self.perm: 
            return 'Set-Cookie: %s=%s; expires=Thu, 14-Jan-2021 01:25:36 GMT; path=/; domain=%s;' % (self.name, self.value, server)
        else:
            return 'Set-Cookie: %s=%s; path=/; domain=%s;' % (self.name, self.value, server)


class xhtmlpage(object):
    def __init__(self, title='XHTML Page'):
        self.xml = '<?xml version="1.0" encoding="utf-8"?>'
        self.doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
        
        self.title = title
        
        self.html = html(xmlns='http://www.w3.org/1999/xhtml',
            xml_lang='en',
            xmlns_xsi='http://www.w3.org/2001/XMLSchema-instance')
            #Apparently the w3 validator doesn't know the xhtml spec
            #xsi_schemaLocation='http://www.w3.org/MarkUp/SCHEMA/xhtml11.xsd')
        
        self.html.head = self.html.add(head())
        self.html.body = self.html.add(body())
        self._entry = self.html.body
        self.cookies = {}
    
    def add(self, obj):
        return self._entry.add(obj)
    
    def __add__(self, obj):
        self.add(obj)
        return self
    
    def set_cookie(self, name, value, perm=False):
        self.cookies[name] = cookie(name, value, perm)
    
    def render(self, just_html=False):
        if not just_html:
            import web
            
            if not title in self.html.head:
                self.html.head.add(title(self.title))
            
            if web.is_internetexplorer:
                # IE doesn't know how to open application/xhtml+xml
                print 'Content-Type: text/html'
            else:
                # google adsense doesnt work on strict xhtml
                print 'Content-Type: text/html'
                #print 'Content-Type: application/xhtml+xml'
            
            print 'Cache-Control: no-cache'
            
            print '\n'.join(cookie.render() for cookie in self.cookies.values())
            print
        
        #Don't print XML declaration if IE so DOCTYPE is first
        if not just_html and not web.is_internetexplorer:
            print self.xml
        print self.doctype
        print
        print self.html
    
    def __str__(self):
        return self.render()
