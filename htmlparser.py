import html
from htmlpage import xhtmlpage
import re

## TODO
## -Cookies? Mmmm...

def XHTMLParse(data, allow_invalid=False, debug=False, start=0):
    r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[a-z0-9]+)(?(isEndTag)|(?P<attributes>(\s([\-a-z0-9:]+)=(".*?")\s*)*)(?P<isSingleTag>/)?)>''')
    r_att = re.compile(r'''(?P<name>[\-a-z0-9:]+)="(?P<value>.*?)"''')
    r_com = re.compile(r'''<!(--(?P<body>.*)--|--\[(?P<condition>.+)\]|\[(?P<isEndTag>endif)\]--)>''')
    
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
        
        name = match.group('name')
        if allow_invalid: name = name.lower()
        
        #Get indeces of current match
        match_start, match_end = match.span()
        
        #If match ahead of start point, plain text and/or comments before
        while start < match_start:
            comment_match = r_com.search(data, start, match_start)
            if comment_match:
                comment_start, comment_end = comment_match.span()
            else:
                comment_start = comment_end = match_start
            
            #If comment ahead of start point, plain text before
            if start < comment_start:
                text = data[start:comment_start]
                #Only add text if it is not all whitespace
                if len(text.strip()) > 0:
                    if '\n' in text and not preserve_whitespace:
                        text = text.strip()
                    stack[-1] += text
                    if debug: print "  ADDED TEXT: %s" % text
            
            #This is a beastly...
            if comment_match:
                if comment_match.group('body'):
                    new = html.comment(comment_match.group('body'))
                    stack[-1] += new
                    if debug: print "  ADDED COMMENT: %s" % new
                elif comment_match.group('condition'):
                    new = html.comment(__invalid=allow_invalid, condition=comment_match.group('condition'))
                    stack[-1] += new
                    stack.append(new)
                    if debug: print "\n%s\n  MATCHED: comment\n  PUSHED: comment (%s)" % (data[comment_start:comment_end], ','.join(type(x).__name__ for x in stack[:-1]))
                else:
                    #This will send us into the first 'if' branch below and rearrage variables
                    name = html.comment.__name__
                    match = comment_match
                    comment_end = match_start
                    match_start, match_end = comment_match.span()
            
            start = comment_end
            
        if debug: print "\n%s\n  MATCHED: %s" % (data[match_start:match_end], name)
        
        if match.group('isEndTag'):
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