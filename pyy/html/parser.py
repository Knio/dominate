'''
Functions to parse XHTML and XHTML documents.
'''

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
import tags
import dtd
from document import document

def tag(x):
  return type(x).__name__

def parse(data, start=0, debug=False, allow_invalid=False, allow_invalid_attributes=False, allow_invalid_markup=False):
  '''
  This method will take a string of XHTML and 
  attempt to parse it into a valid tag tree.
  
  There are a variety of options which you can modify via keyword arguments
  which affect various aspects of the parsing process:
  
  * `debug` - Boolean value. If set to True debugging information about 
              parsing will be printed to standard out.
  * `start` - Integer value. Index of a point in the string to start parsing.  
  * `allow_invalid`
            - Boolean value. If True this will set both 
              `allow_invalid_attributes` and `allow_invalid_markup` to True.
  * `allow_invalid_markup` 
            - Boolean value. If True the parser will accept tag names in
              uppercase and attempt to resolve missing end tags or out-of-
              order end tags.
  * `allow_invalid_attributes`
            - Boolean value. If True the `__invalid` special keyword will
              be passed to every tag so that you can set a DOCTYPE even
              though the tags might not be fully compliant.
  
  This method will return a the root tag if there is only one or a list of all
  the adjacent top-level tags.
  '''
  if allow_invalid:
    allow_invalid_attributes = allow_invalid_markup = allow_invalid
  
  #Change comments to fake tags for easy parsing
  data = tags.comment.comments2tags(data)
  
  if allow_invalid_markup:
    regex_attributes = {
      'name': 'a-zA-Z0-9', 
      'attribute_name': r'\-a-zA-Z0-9:', 
      'attribute_quote': '"?'}
  else:
    regex_attributes = {
      'name': 'a-z0-9',
      'attribute_name': r'\-a-z0-9:',
      'attribute_quote': '"' }
  
  r_tag = re.compile(r'''<(?P<isEndTag>/)?(?P<name>[%(name)s]+)(?(isEndTag)|(?P<attributes>(\s+([%(attribute_name)s]+)\s?=\s?(%(attribute_quote)s.*?%(attribute_quote)s)\s*)*)[ ]*(?P<isSingleTag>/)?)>''' % regex_attributes)
  r_att = re.compile(r'''(?P<name>[%(attribute_name)s]+)\s?=\s?%(attribute_quote)s(?P<value>.*?)%(attribute_quote)s''' % regex_attributes)
  
  #Used to group top-level adjacent elements
  class dummy(tags.html_tag): pass
  
  #Initialize tag tree stack with dummy element
  result = dummy()
  stack  = [result]
  preserve_whitespace = 0
  in_normal_comment   = False
  
  data_length = len(data)
  while start < data_length:
    #Attempt to get next match
    match = r_tag.search(data, start)
    if not match: break
    match_start, match_end = match.span()
    
    #If match ahead of start point, add plain text
    if start < match_start:
      text = data[start:match_start]
      #Only add text if it is not all whitespace (what about pretty?)
      if len(text.strip()) > 0 or preserve_whitespace:
        if '\n' in text and not preserve_whitespace:
          text = text.strip()
        
        stack[-1] += text
        
        if debug: print "  ADDED TEXT (1): %r" % text
    
    name = match.group('name')
    if allow_invalid_markup: name = name.lower()
    
    #Check if it is a special, underscored class
    if name in tags.underscored_classes:
      name += '_'
    
    #If we are inside a <!--regular--> comment just add tags as text
    if in_normal_comment and name != tags.comment.__name__:
      text = data[match_start:match_end]
      stack[-1] += text
      if debug: print "  ADDED TEXT (2): %r" % text
      start = match_end
      continue
    
    if debug: print "\n%s\n  MATCHED: %s" % (data[match_start:match_end], name)
    
    if match.group('isEndTag'):
      if debug: print "  IS END TAG"
      
      #Pop last tag off the stack
      result = stack.pop()
      if debug: print "  POPPED: %s (%s)" % (tag(result), ','.join(tag(x) for x in stack))
      
      #Update value of preserve_whitespace
      if not result.is_pretty:
        preserve_whitespace -= 1
      
      #If we are popping out of a comment indicate such so tag parsing resumes
      if type(result) == tags.comment:
        in_normal_comment = False
        preserve_whitespace -= 1
      
      #Check if the tag we are popping off the stack is matching tag
      if tag(result) != name:
        if allow_invalid_markup:
          if debug: print "  BACK-CHECKING FOR <%s> IN (%s)" % (name, ','.join(tag(x) for x in stack))
          
          #Traverse down the stack looking for a match
          resolved = False
          for i in xrange(-1, -len(stack), -1):
            if tag(stack[i]) == name:
              #Discard all tags above it
              del stack[i:]
              
              resolved = True
              break
          
          #If we did not find a match then restore the popped tag
          if not resolved:
            if debug: print "  RE-PUSHED: %s (%s)" % (tag(result), ','.join(tag(x) for x in stack))
            stack.append(result)
          
        else:
          raise TypeError('Tag mismatch. %s != %s' % (tag(result), name))
    else:
      #Assemble attributes (if exist) into a dictionary
      kwargs = dict(r_att.findall(match.group('attributes') or ''))
      
      #Create new object
      new = getattr(tags, name)(__invalid=allow_invalid_attributes, **kwargs)
      stack[-1] += new
      
      #Update value of preserve_whitespace
      if not new.is_pretty:
        preserve_whitespace += 1
      
      #If it is a single tag (or supposed to be) mark as such
      if match.group('isSingleTag') or (allow_invalid_markup and new.is_single):
        stack[-1][-1].is_single = True
        
        if debug: print "  IS SINGLE TAG\n  ADDED TO: %s (%s)" % (tag(stack[-1]), ','.join(tag(x) for x in stack[:-1]))
      else:
        stack.append(new)
        if debug: print "  PUSHED: %s (%s)" % (name, ','.join(tag(x) for x in stack[:-1]))
        
        #If we are in a <!--regular--> comment indicate such so tag parsing ceases
        if type(new) == tags.comment and tags.comment.ATTRIBUTE_CONDITION not in new:
          in_normal_comment = True
          preserve_whitespace += 1
    
    #Move to after current tag
    start = match_end
  
  #Add any trailing text
  if start < data_length:
    stack[-1] += data[start:]
    if debug: print "  ADDED TEXT (3): %r" % data[start:]
  
  #If dummy is not the only item on the stack then there are unclosed tags
  if not allow_invalid_markup and len(stack) > 1:
    raise ValueError('Unclosed tags: %s', ', '.join(tag(x) for x in stack[1:]))
  
  #Return the only child or top-level adjancent children
  if len(stack[0]) != 1:
    return stack[0].children
  else:
    return stack[0][0]


def pageparse(data, start=0, allow_invalid=False, allow_invalid_attributes=False, allow_invalid_markup=False, debug=False):
  '''
  Will parse an entire page source into a document including the DOCTYPE and
  tag tree.
  
  There are a variety of options which you can modify via keyword arguments which affect
  various aspects of the parsing process:
  
  * `debug` - Boolean value. If set to True debugging information about parsing will be
              printed to standard out.
  * `start` - Integer value. Index of a point in the string to start parsing.
  * `allow_invalid` - Boolean value. If True this will set both `allow_invalid_attributes`
                      and `allow_invalid_markup` to True.
  * `allow_invalid_markup` - Boolean value. If True the parser will accept tag names in
                             uppercase and attempt to resolve missing end tags or out-of-
                             order end tags.
  * `allow_invalid_attributes` - Boolean value. If True the `__invalid` special keyword will
                                 be passed to every tag so that you can set a DOCTYPE even
                                 though the tags might not be fully compliant.
  '''
  r_xml = re.compile(r'''<\?xml version="(?P<version>\d\.\d)"(?: encoding="(?P<encoding>[\-a-zA-Z0-9]+)")?\?>''')
  r_doc = re.compile(r'''<!DOCTYPE\s+(?P<topelement>[a-zA-Z]+)(?:\s+(?P<availability>PUBLIC|SYSTEM)\s+"(?P<registration>-|\+)//(?P<organization>W3C|IETF)//(?P<type>DTD) (?P<name>(?P<html>X?HTML) (?P<is_basic>Basic )?(?P<version>\d\.\d{1,2})(?: (?P<strength>Strict|Transitional|Frameset|Final))?)//(?P<language>[A-Z]{2})"(?:\s+"(?P<url>http://www\.w3\.org/TR/[\-a-z0-9]+/(?:DTD/)?[\-a-z0-9]+\.dtd)")?)?>''')
  
  def remove_spaces(data):
    spaces = re.compile(r'\s+', re.S)
    return spaces.sub(' ', data)
  
  #Locate possible XML declaration and add it to page
  xml = r_xml.search(data, start)
  if xml:
    start, end = xml.span()
    if debug: print "GOT XML: %s" % remove_spaces(data[start:end])
    start = end
  
  #Locate possible DOCTYPE declaration and add it to page
  doctype = r_doc.search(data, start)
  spec = None
  if doctype:
    start, end = doctype.span()
    doctype_text = remove_spaces(data[start:end])
    if debug: print "GOT DOCTYPE: %s" % doctype
    start = end
    
    #Determine which spec to use
    if doctype.group('html') == 'XHTML':
      #XHTML
      version = doctype.group('version')
      if version == '1.0':
        #XHTML 1.0
        strength = doctype.group('strength')
        if strength == 'Strict':
          spec = dtd.xhtml10strict
        elif strength == 'Frameset':
          spec = dtd.xhtml10frameset
        elif strength == 'Transitional':
          raise ValueError('No class set for XHTML 1.0 Transitional.')
        else:
          raise ValueError('Invalid XHTML 1.0 strength "%s".' % strength)
      elif version == '1.1':
        spec = dtd.xhtml11
      else:
        raise ValueError('Unknown XHTML version "%s".' % version)
    elif doctype.group('html') == 'HTML':
      #HTML
      version = doctype.group('version')
      if version == '4.01':
        strength = doctype.group('strength')
        if not strength or strength == 'Strict':
          spec = dtd.html4strict
        elif strength == 'Frameset':
          spec = dtd.html4frameset
        elif strength == 'Transitional':
          raise ValueError('No class set for HTML 4.01 Transitional')
        else:
          raise ValueError('Invalid HTML 4.01 strength "%s".' % strength)
      elif version == '3' or version == '2':
        raise ValueError('No class set for HTML version %s.' % version)
      else:
        raise ValueError('Unknown HTML version "%s".' % version)
    elif not doctype.group('html') and doctype.group('topelement') == 'html':
      #HTML 5
      spec = dtd.html5
    else:
      raise ValueError('Unknown doctype "%s".' % doctype_text)
  
  page = document(doctype=spec)
  page.html = parse(data, start=start, debug=debug, allow_invalid=allow_invalid, allow_invalid_attributes=allow_invalid_attributes, allow_invalid_markup=allow_invalid_markup)
  
  return page
