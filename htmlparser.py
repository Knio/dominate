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
    start = 0
    is_ugly = 0
    
    #Locate possible XML declaration and add it to xhtmlpage
    xml = r_xml.search(data, start)
    if xml:
        start, end = xml.span()
        xml = data[start:end]
        if debug: print "GOT XML: %s" % xml
        #page.xml = xml
        start = end
    
    #Locate possible DOCTYPE declaration and add it to xhtmlpage
    doctype = r_doc.search(data, start)
    if doctype:
        start, end = doctype.span()
        doctype = data[start:end]
        if debug: print "GOT DOCTYPE: %s" % doctype
        #page.doctype = doctype
        start = end
    
    #Initialize tag tree stack with dummy element
    result = html.dummy()
    stack = [result]
    
    while start < len(data):
        #Attempt to get next match
        match = r_tag.search(data, start)
        if not match: break
        
        #Get indeces of current match
        match_start, match_end = match.span()
        if debug: print "\nMATCHED: %s" % data[match_start:match_end]
        
        #If there anything but whitespace since the last match and we are not
        #  inside a "pretty" function add it
        if match_start > start:
            text = data[start:match_start]
            if len(text.strip()) > 0:
                if '\n' in text and not is_ugly:
                    text = text.strip()
                stack[-1] += text
                if debug: print "  ADDED TEXT: %s" % text
        
        #Get the tag name
        name = match.group('name')
        if allow_invalid: name = name.lower()
        
        if match.group('isEndTag'):
            if debug: print "  IS END TAG"
            
            #Pop last tag off the stack
            result = stack.pop()
            if debug: print "  POPPED: %s (%s)" % (type(result).__name__, ','.join(type(x).__name__ for x in stack))
            
            if not result.is_pretty:
                is_ugly -= 1
            
            #Check if the tag we are popping off the stack is matching tag
            if type(result).__name__ != name:
                raise TypeError('Tag mismatch. %s != %s' % (type(result).__name__, name))
        else:
            #Iterate over the attributes and assemble into dictionary
            kwargs = {}
            if match.group('attributes'):
                for attribute in r_att.finditer(match.group('attributes')):
                    kwargs[attribute.group('name')] = attribute.group('value')
                    if debug: print '  ATTR: %s = "%s"' % (attribute.group('name'), attribute.group('value'))
            
            #Create tag object and add it as child tag to parent
            new = getattr(html, name)(__invalid=allow_invalid, **kwargs)
            stack[-1] += new
            
            if not new.is_pretty:
                is_ugly += 1
            
            #If it is a single tag mark as such, otherwise push it to the stack
            if match.group('isSingleTag') or new.is_single:
                stack[-1].is_single = True
                if debug: print "  IS SINGLE TAG\n  ADDED TO: %s (%s)" % (type(stack[-1]).__name__, ','.join(type(x).__name__ for x in stack[:-1]))
            else:
                stack.append(new)
                if debug: print "  PUSHED: %s (%s)" % (name, ','.join(type(x).__name__ for x in stack[:-1]))
        
        #Move to after current tag
        start = match_end
    
    #return page
    return result

def test(url='http://docs.python.org/library/re.html'):
    import urllib
    return XHTMLParse(urllib.urlopen(url).read(), True, True)