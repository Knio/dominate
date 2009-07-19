__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy.  If not, see
<http://www.gnu.org/licenses/>.
'''

import re
import html, xhtml11, html5

def parse(data, spec=xhtml11, start=0, debug=False, allow_invalid=False, allow_invalid_attributes=False, allow_invalid_markup=False):
    if allow_invalid:
        allow_invalid_attributes = allow_invalid_markup = allow_invalid
    
    #Change comments to fake tags for easy parsing
    data = html.comment.comments2tags(data)
    
    if allow_invalid_markup:
        regex_attributes = {'name': 'a-zA-Z0-9', 'attribute_name': r'\-a-zA-Z0-9:', 'attribute_quote': '"?'}
    else:
        regex_attributes = {'name': 'a-z0-9'   , 'attribute_name': r'\-a-z0-9:'   , 'attribute_quote': '"' }
    
    r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[%(name)s]+)(?(isEndTag)|(?P<attributes>(\s+([%(attribute_name)s]+)\s?=\s?(%(attribute_quote)s.*?%(attribute_quote)s)\s*)*)(?P<isSingleTag>/)?)>''' % regex_attributes)
    r_att = re.compile(r'''(?P<name>[%(attribute_name)s]+)\s?=\s?%(attribute_quote)s(?P<value>.*?)%(attribute_quote)s''' % regex_attributes)
    
    #Initialize tag tree stack with dummy element
    result = []
    stack = [result]
    preserve_whitespace = 0
    in_normal_comment = False
    
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
                
                stack[-1].append(text)
                
                if debug: print "  ADDED TEXT: %s" % text
        
        name = match.group('name')
        if allow_invalid_markup: name = name.lower()
        
        #If we are inside a <!--regular--> comment just add tags as text
        if in_normal_comment and name != html.comment.__name__:
            stack[-1].append(data[match_start:match_end])
            start = match_end
            continue
        
        if debug: print "\n%s\n  MATCHED: %s" % (data[match_start:match_end], name)
        
        if match.group('isEndTag'):
            if debug: print "  IS END TAG"
            
            #Pop last tag off the stack
            result = stack.pop()
            if debug: print "  POPPED: %s (%s)" % (type(result).__name__, ','.join(type(x).__name__ for x in stack))
            
            #Update value of preserve_whitespace
            if not result.is_pretty:
                preserve_whitespace -= 1
            
            #If we are popping out of a comment indicate such so tag parsing resumes
            if type(result) == html.comment:
                in_normal_comment = False
            
            #Check if the tag we are popping off the stack is matching tag
            if type(result).__name__ != name:
                raise TypeError('Tag mismatch. %s != %s' % (type(result).__name__, name))
        else:
            #Assemble attributes (if exist) into a dictionary
            kwargs = dict(r_att.findall(match.group('attributes') or ''))
            
            #Create new object and push onto the stack
            new = getattr(spec, name)(__invalid=allow_invalid_attributes, **kwargs)
            stack[-1].append(new)
            
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
                
                #If we are in a <!--regular--> comment indicate such so tag parsing ceases
                if type(new) == html.comment and comment.ATTRIBUTE_CONDITION not in new:
                    in_normal_comment = True
        
        #Move to after current tag
        start = match_end
    
    #Return the top of the stack
    if len(stack) > 1:
        return stack[-1]
    else:
        return result


def pageparse(data, start=0, allow_invalid=False, allow_invalid_attributes=False, allow_invalid_markup=False, debug=False):
    r_xml = re.compile(r'''<\?xml version="(?P<version>\d\.\d)"(?: encoding="(?P<encoding>[\-a-zA-Z0-9]+)")?\?>''')
    r_doc = re.compile(r'''<!DOCTYPE\s+(?P<topelement>[a-zA-Z]+)(?:\s+(?P<availability>PUBLIC|SYSTEM)\s+"(?P<registration>-|\+)//(?P<organization>W3C|IETF)//(?P<type>DTD) (?P<name>(?P<html>X?HTML) (?P<is_basic>Basic )?(?P<version>\d\.\d{1,2})(?: (?P<strength>Strict|Transitional|Frameset|Final))?)//(?P<language>[A-Z]{2})"(?:\s+"(?P<url>http://www\.w3\.org/TR/[\-a-z0-9]+/(?:DTD/)?[\-a-z0-9]+\.dtd)")?)?>''')
    
    def remove_spaces(data):
        spaces = re.compile(r'\s+', re.S)
        return spaces.sub(' ', data)
    
    #Locate possible XML declaration and add it to page
    xml = r_xml.search(data, start)
    if xml:
        start, end = xml.span()
        xml = remove_spaces(data[start:end])
        if debug: print "GOT XML: %s" % xml
        start = end
    
    #Locate possible DOCTYPE declaration and add it to page
    doctype = r_doc.search(data, start)
    if doctype:
        start, end = doctype.span()
        doctype = remove_spaces(data[start:end])
        if debug: print "GOT DOCTYPE: %s" % doctype
        start = end
    
    #Determine which spec to use
    spec = xhtml11 ##FIXME!
    #Create spec's htmlpage
    page = spec.htmlpage()
    #Add doctype and xml to it
    page.doctype = doctype
    page.xml     = xml
    
    #Parse main XHTML data
    page.html = XHTMLParse(data, allow_invalid=allow_invalid, allow_invalid_attributes=allow_invalid_attributes, allow_invalid_markup=allow_invalid_markup, debug=debug, start=start)
    
    return page
