import html
from htmlpage import xhtmlpage
import re

## TODO
## -Get comments regex working
## -Cookies? Mmmm...

def XHTMLParse(data, allow_invalid=False, debug=False):
    def DEBUG(message='\n'):
        if debug:
            print message
    
    r_xml = re.compile(r'''<\?xml ([a-z]="\w+")+\?>''')
    r_doc = re.compile(r'''<!DOCTYPE\s+(:HTML|html)\s+PUBLIC\s+"[^"]+"\s+"[^"]+">''')
    r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[a-z0-9]+)(?(isEndTag)|(?P<attributes>(\s([\-a-z0-9:]+)=(".*?")\s*)*)(?P<isSingleTag>/)?)>''')
    r_att = re.compile(r'''(?P<name>[\-a-z0-9:]+)="(?P<value>.*?)"''')
    r_com = re.compile(r'''<!--([(?P<condition>\w+)]>)?(?(condition)|(?P<separator>\s))(?P<body>.*?)(?(condition)<![endif]|(?=separator))-->''')
    
    if allow_invalid:
        r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[a-zA-Z0-9]+)(?(isEndTag)|(?P<attributes>(\s([\-a-zA-Z0-9:]+)=("?.*?"?)\s*)*)(?P<isSingleTag>/)?)>''')
        r_att = re.compile(r'''(?P<name>[\-a-zA-Z0-9:]+)="?(?P<value>.*?)"?''')
    
    start = 0
    preserve_whitespace = 0
    page = xhtmlpage()
    
    #Locate possible XML declaration and add it to page
    xml = r_xml.search(data, start)
    if xml:
        start, end = xml.span()
        xml = data[start:end]
        DEBUG("GOT XML: %s" % xml)
        page.xml = xml
        start = end
    
    #Locate possible DOCTYPE declaration and add it to page
    doctype = r_doc.search(data, start)
    if doctype:
        start, end = doctype.span()
        doctype = data[start:end]
        DEBUG("GOT DOCTYPE: %s" % doctype)
        page.doctype = doctype
        start = end
    
    #Initialize tag tree stack with dummy element
    result = html.dummy()
    stack = [result]
    
    data_length = len(data)
    while start < data_length:
        #Attempt to get next match
        match = r_tag.search(data, start)
        if not match: break
        
        name = match.group('name')
        if allow_invalid: name = name.lower()
        
        #Get indeces of current match
        match_start, match_end = match.span()
        DEBUG("\n%s\n  MATCHED: %s" % (data[match_start:match_end], name))
        
        #If we are ahead of the end of last match then there is plain text
        if match_start > start:
            text = data[start:match_start]
            
            ##TODO: this is where we should check for comments
            
            #Only add text if it is not all whitespace
            if len(text.strip()) > 0:
                if '\n' in text and not preserve_whitespace:
                    text = text.strip()
                stack[-1] += text
                DEBUG("  ADDED TEXT: %s" % text)
        
        if match.group('isEndTag'):
            DEBUG("  IS END TAG")
            
            #Pop last tag off the stack
            result = stack.pop()
            DEBUG("  POPPED: %s (%s)" % (type(result).__name__, ','.join(type(x).__name__ for x in stack)))
            
            #Update value of preserve_whitespace
            if not result.is_pretty:
                preserve_whitespace -= 1
            
            #Check if the tag we are popping off the stack is matching tag
            if type(result).__name__ != name:
                raise TypeError('Tag mismatch. %s != %s' % (type(result).__name__, name))
        else:
            #Assemble attributes (if exist) into a dictionary
            kwargs = dict(r_att.findall(match.group('attributes') or ''))
            
            #Create new object and push onto the stack
            new = getattr(html, name)(__invalid=allow_invalid, **kwargs)
            stack[-1] += new
            
            #Update value of preserve_whitespace
            if not new.is_pretty:
                preserve_whitespace += 1
            
            #If it is a single tag (or supposed to be) mark as such
            if match.group('isSingleTag'):
                stack[-1].is_single = True
                DEBUG("  IS SINGLE TAG\n  ADDED TO: %s (%s)" % (type(stack[-1]).__name__, ','.join(type(x).__name__ for x in stack[:-1])))
            elif not allow_invalid or not tag.is_single:
                stack.append(new)
                DEBUG("  PUSHED: %s (%s)" % (name, ','.join(type(x).__name__ for x in stack[:-1])))
        
        #Move to after current tag
        start = match_end
    
    page.html = result
    return page

def parse(data):
    return XHTMLParse(data, True).html

def test(url='http://docs.python.org/library/re.html'):
    import urllib
    return XHTMLParse(urllib.urlopen(url).read(), True, True)