import html
from htmlpage import xhtmlpage
import re

## TODO
## -Cookies? Mmmm...
## -Parse DOCTYPE and allow_invalid accordingly
## -Add levels of invalidity (uppercase tags, invalid attributes, not including
##    all required attributes, etc.)
## -Use **kwargs and parse so there are not 1000 args with defaults

COMMENTS_FIX = (
    (re.compile(r'<!--\[if (.*?)\]>'), r'<comment condition="\1">'),
    (re.compile(r'<!--'), '<comment>'),
    (re.compile(r'(<!\[endif\])?-->'), r'</comment>'),
)

def XHTMLParse(data, allow_invalid=False, debug=False, start=0):
    #Change comments to fake tags for easy parsing
    for search, replace in COMMENTS_FIX:
        data = search.sub(replace, data)
    
    r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[a-z0-9]+)(?(isEndTag)|(?P<attributes>(\s([\-a-z0-9:]+)=(".*?")\s*)*)(?P<isSingleTag>/)?)>|(?P<comment><!--(\[.*\]>)?|(<!\[endif\])?-->)''')
    r_att = re.compile(r'''(?P<name>[\-a-z0-9:]+)="(?P<value>.*?)"''')
    
    if allow_invalid:
        r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[a-zA-Z0-9]+)(?(isEndTag)|(?P<attributes>(\s([\-a-zA-Z0-9:]+)=("?.*?"?)\s*)*)(?P<isSingleTag>/)?)>''')
        r_att = re.compile(r'''(?P<name>[\-a-zA-Z0-9:]+)="?(?P<value>.*?)"?''')
    
    #Initialize tag tree stack with dummy element
    result = html.dummy()
    stack = [result]
    preserve_whitespace = 0
    
    data_length = len(data)
    while start < data_length:
        #Attempt to get next match
        match = r_tag.search(data, start)
        if not match: break
        match_start, match_end = match.span()
        
        #If match ahead of start point, add plain text
        if start < match_start:
            text = data[start:match_start]
            #Only add text if it is not all whitespace
            if len(text.strip()) > 0:
                if '\n' in text and not preserve_whitespace:
                    text = text.strip()
                stack[-1] += text
                if debug: print "  ADDED TEXT: %s" % text
        
        name = match.group('name')
        if allow_invalid: name = name.lower()
        if debug: print "\n%s\n  MATCHED: %s" % (data[match_start:match_end], name)
        
        if match.group('isEndTag'):
            #Fix things like <div>--></div> which should use <div>--&gt;</div>
            if name == html.comment.__name__ and not any(isinstance(tag, html.comment) for tag in stack):
                stack[-1] += '--&gt;'
                if debug: print "  ADDED TEXT: --%gt;"
            else:
                if debug: print "  IS END TAG"
                
                #Pop last tag off the stack
                result = stack.pop()
                if debug: print "  POPPED: %s (%s)" % (type(result).__name__, ','.join(type(x).__name__ for x in stack))
                
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
                if debug: print "  IS SINGLE TAG\n  ADDED TO: %s (%s)" % (type(stack[-1]).__name__, ','.join(type(x).__name__ for x in stack[:-1]))
            elif not allow_invalid or not new.is_single:
                stack.append(new)
                if debug: print "  PUSHED: %s (%s)" % (name, ','.join(type(x).__name__ for x in stack[:-1]))
        
        #Move to after current tag
        start = match_end
    
    return result


def PageParse(data, allow_invalid=False, debug=False):
    r_xml = re.compile(r'''<\?xml ([a-z]="\w+")+\?>''')
    r_doc = re.compile(r'''<!DOCTYPE\s+(:HTML|html)\s+PUBLIC\s+"[^"]+"\s+"[^"]+">''')
    
    start = 0
    page = xhtmlpage()
    
    #Locate possible XML declaration and add it to page
    xml = r_xml.search(data, start)
    if xml:
        start, end = xml.span()
        xml = data[start:end]
        if debug: print "GOT XML: %s" % xml
        page.xml = xml
        start = end
    
    #Locate possible DOCTYPE declaration and add it to page
    doctype = r_doc.search(data, start)
    if doctype:
        start, end = doctype.span()
        doctype = data[start:end]
        if debug: print "GOT DOCTYPE: %s" % doctype
        page.doctype = doctype
        start = end
    
    #Parse main XHTML data
    page.html = XHTMLParse(data, allow_invalid, debug, start)
    
    return page


def parse(data):
    '''
    DEPRICATED: Use XHTMLParse
    '''
    return XHTMLParse(data, True)


def test(url='http://docs.python.org/library/re.html'):
    import urllib
    return XHTMLParse(urllib.urlopen(url).read(), True, True)