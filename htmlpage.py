from html import *

class xhtmlpage(object):
    def __init__(self):
        self.html = html()
        self.html.attributes = {'xmlns':'http://www.w3.org/1999/xhtml', 'xml:lang':'en'} #, 'lang':'en'}
        self.html.head = self.html.add(head())
        self.html.body = self.html.add(body())
        
    def add(self, obj):
        return self.html.body.add(obj)
        
    def render(self):
        
        self.html.head.title = self.html.head.add(title('XHTML Page'))
        
        
        print 'Content-Type: application/xhtml+xml'
        print
        print '<?xml version="1.0" encoding="iso-8859-1"?>'
        
        print '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
        
        print self.html
        
