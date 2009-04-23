import html
from htmlpage import xhtmlpage
import re

COMMENTS_FIX = (
    (re.compile(r'<!--\[if (.*?)\]>(.*?)<!\[endif\]-->', re.S), r'<comment condition="\1">\2</comment>'),
    (re.compile(r'<!--(.*?)-->', re.S)                        , r'<comment>\1</comment>'),
    (re.compile(r'<!\[if (.*?)\]>(.*?)<!\[endif]>', re.S)     , r'<comment condition="\1" downlevel="revealed">\2</comment>'),
)

def XHTMLParse(data, start=0, debug=False, allow_invalid=False, allow_invalid_attributes=False, allow_invalid_markup=False):
    if allow_invalid:
        allow_invalid_attributes = allow_invalid_markup = allow_invalid
    
    #Change comments to fake tags for easy parsing
    for search, replace in COMMENTS_FIX:
        data = search.sub(replace, data)
    
    if allow_invalid_markup:
        regex_attributes = {'name': 'a-zA-Z0-9', 'attribute_name': r'\-a-zA-Z0-9:', 'attribute_quote': '"?'}
    else:
        regex_attributes = {'name': 'a-z0-9'   , 'attribute_name': r'\-a-z0-9:'   , 'attribute_quote': '"' }
    
    r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[%(name)s]+)(?(isEndTag)|(?P<attributes>(\s([%(attribute_name)s]+)=(%(attribute_quote)s.*?%(attribute_quote)s)\s*)*)(?P<isSingleTag>/)?)>''' % regex_attributes)
    r_att = re.compile(r'''(?P<name>[%(attribute_name)s]+)=%(attribute_quote)s(?P<value>.*?)%(attribute_quote)s''' % regex_attributes)
    
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
        if allow_invalid_markup: name = name.lower()
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
            new = getattr(html, name)(__invalid=allow_invalid_attributes, **kwargs)
            stack[-1] += new
            
            #Update value of preserve_whitespace
            if not new.is_pretty:
                preserve_whitespace += 1
            
            #If it is a single tag (or supposed to be) mark as such
            if match.group('isSingleTag') or (allow_invalid_markup and new.is_single):
                stack[-1].is_single = True
                if debug: print "  IS SINGLE TAG\n  ADDED TO: %s (%s)" % (type(stack[-1]).__name__, ','.join(type(x).__name__ for x in stack[:-1]))
            else:
                stack.append(new)
                if debug: print "  PUSHED: %s (%s)" % (name, ','.join(type(x).__name__ for x in stack[:-1]))
        
        #Move to after current tag
        start = match_end
    
    #If their were adjacent top-level tags return them in a dummy tag
    if len(stack[-1]) > 1:
        result = stack.pop()
    
    return result


def PageParse(data, start=0, allow_invalid=False, debug=False):
    r_xml = re.compile(r'''<\?xml version="(?P<version>\d\.\d)"(?: encoding="(?P<encoding>[\-a-zA-Z0-9]+)")?\?>''')
    r_doc = re.compile(r'''<!DOCTYPE\s+(?P<topelement>[a-zA-Z]+)(?:\s+(?P<availability>PUBLIC|SYSTEM)\s+"(?<registration>-|+)//(?P<organization>W3C|IETF)//(?<type>DTD) (?P<name>(?P<html>X?HTML) (?P<is_basic>Basic )?(?P<version>\d\.\d{1,2})(?: (?P<type>Strict|Transitional|Frameset|Final))?)//(?P<language>[A-Z]{2})"(?:\s+"(?P<url>http://www\.w3\.org/TR/(?P<id>[\-a-z0-9]+)/(?:DTD/)?(?P<file>[\-a-z0-9]+\.dtd))")?)?>''')
    
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
    page.html = XHTMLParse(data, allow_invalid=allow_invalid, debug=debug, start=start)
    
    return page


def parse(data):
    '''
    DEPRICATED: Use XHTMLParse
    '''
    return XHTMLParse(data, True)


def test(url='http://docs.python.org/library/re.html'):
    import urllib
    return XHTMLParse(urllib.urlopen(url).read(), debug=True, allow_invalid_attributes=True)