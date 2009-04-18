import html
#import htmlpage.xhtmlpage
import re

## TODO
## 1. Update xhtmlpage to support xml and doctype
## 2. If allow_invalid is true use re.IGNORECASE flag
## 3. Use alternate regex's for allow_invalid==True to support uppercase
##    tags, no quotes around attribute values, etc.

def parse(data):
    #return XHTMLParse(data, True).html
    return XHTMLParse(data, True)

def XHTMLParse(data, allow_invalid=False, debug=False):
    r_xml = re.compile(r'''<\?xml ([a-z]="\w+")+\?>''')
    r_doc = re.compile(r'''<!DOCTYPE\s+HTML\s+PUBLIC\s+"[^"]+"\s+"([^"]+)/([^/]+)\.dtd">\s+''')
    r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[a-z0-9]+)(?!isEndTag)((?P<attributes>(\s([\-a-z0-9:]+)=(".*?")\s*)*)(?P<isSingleTag>/)?)>''')
    r_att = re.compile(r'''(?P<name>[\-a-z0-9:]+)="(?P<value>.*?)"''')
    r_com = re.compile(r'''<!--(?P<separator>)(?P<comment>.*)(?=separator)-->''')
    
    #page = xhtmlpage()
    
    xml = r_xml.search(data)
    if xml:
        start, end = xml.span()
        xml = data[start:end]
        print "GOT XML: %s" % xml
        #page.xml = xml
        data = data[end:]
    
    doctype = r_doc.search(data)
    if doctype:
        start, end = doctype.span()
        doctype = data[start:end]
        print "GOT DOCTYPE: %s" % doctype
        #page.doctype = doctype
        data = data[end:]
    
    result = html.html_tag()
    stack = [result]
    
    while data:
        #Get next tag match
        match = r_tag.search(data)
        if not match: break
        start, end = match.span()
        if debug: print "\nMATCHED: %s" % data[start:end]
        
        #If we don't match at 0 add text to previous tag (if not whitespace)
        if start and len(data[0:start].strip()) > 0:
            stack[-1] += data[0:start]
            if debug: print "  ADDED TEXT: %s" % data[0:start]
        
        #Get the tag name
        name = match.group('name')
        if allow_invalid: name = name.lower()
        
        if match.group('isEndTag'):
            if debug: print "  IS END TAG"
            
            #Pop last tag off the stack
            result = stack.pop()
            if debug: print "  POPPED: %s (%s)" % (type(result).__name__, ','.join(type(x).__name__ for x in stack))
            
            if type(result).__name__ != name:
                raise TypeError('Tag mismatch. %s != %s' % (type(result).__name__, name))
        else:
            #Iterate over the attributes
            kwargs = {}
            if match.group('attributes'):
                for attribute in r_att.finditer(match.group('attributes')):
                    kwargs[attribute.group('name')] = attribute.group('value')
                    if debug: print '  ATTR: %s = "%s"' % (attribute.group('name'), attribute.group('value'))
            
            #Create object and push it to the stack
            new = getattr(html, name)(__invalid=allow_invalid, **kwargs)
            stack[-1] += new
            
            #If it is a single tag mark as such, otherwise push `new` to stack head
            if match.group('isSingleTag') or new.is_single:
                stack[-1].is_single = True
                if debug: print "  IS SINGLE TAG\n  ADDED TO: %s (%s)" % (type(stack[-1]).__name__, ','.join(type(x).__name__ for x in stack[:-1]))
            else:
                stack.append(new)
                if debug: print "  PUSHED: %s (%s)" % (name, ','.join(type(x).__name__ for x in stack[:-1]))
        
        #Move to after current tag
        data = data[end:]
    
    #return page
    return result

def test(url='http://docs.python.org/library/re.html'):
    import urllib
    return XHTMLParse(urllib.urlopen(url).read(), True, True)