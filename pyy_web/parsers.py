__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy. If not, see
<http://www.gnu.org/licenses/>.
'''

import re
from urllib import unquote_plus

def parse_query(string):
  d = {}
  string = string.split('&')
  for pair in filter(None, string):
    is_array = False
    try:
      key, value = map(unquote_plus, pair.split('=', 1))
      if key.endswith('[]'): # TODO: why the hell is this a magic string? wtf?
        key   = key[:-2]
        is_array = True
    except ValueError:
      key, value = unquote_plus(pair), ''
    if is_array:
      if key in d:
        d[key].append(value)
      else:
        d[key] = [value]
    else:
      d[key] = value
  return d


def parse_semi(string):
  d = {}
  for pair in filter(None, string.split('; ')):
    try:
      key, value = pair.split('=',1)
    except ValueError:
      key, value = '', pair
    d[key] = value
  return d



def parse_user_agent(user_agent):
  USER_AGENT_REGEX = (
    ('ie',        re.compile(r'MSIE (?P<version>(?P<major>\d+)(?:\.(?P<minor>\d+))?)'), 'Windows CE'),
    ('firefox',   re.compile(r'Firefox/(?P<version>(?P<major>\d+)\.(?P<minor>\d+)(?:\.(?P<release>\d+)(?:\.(?P<build>\d+))?)?((a|b)(?P<beta>\d+))?)'), 'Fennec'),
    ('chrome',    re.compile(r'Chrome/(?P<version>(?P<major>\d+)\.(?P<minor>\d+)(?:\.(?P<release>\d+)(?:\.(?P<build>\d+))?)?)'), None),
    ('safari',    re.compile(r'Version/(?P<version>(?P<major>\d+)\.(?P<minor>\d+)(?:\.(?P<release>\d+))?)'), 'iPhone'),
    ('opera',     re.compile(r'Opera(?:/| )(?P<version>(?P<major>\d+)\.(?P<minor>\d+))'), 'Mini'),
    ('googlebot', re.compile(r'Googlebot/(?P<version>(?P<major>\d+)\.(?P<minor>\d+))'), None), # googlebot Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
  )
  
  class browser(object): pass
  b = browser()
  
  for browser, regex, mobile in USER_AGENT_REGEX:
    match = re.search(regex, user_agent)
    if match:
      b.name   = browser
      b.mobile = mobile and mobile in user_agent
      
      for name, value in match.groupdict().iteritems():
        if value:
          setattr(b, name, value)
      
      setattr(b, browser, float(b.major + '.' + b.minor))
    else:
      setattr(b, browser, None)
  
  return b



def parse_multipart(content_type, data):
  '''
  This method *MUST* be run with unbuffered input!
  python -u
  '''
  multipart = {}

  content_type = parse_semi(content_type)
  boundary     = '--' + content_type['boundary']
  
  string = data
  if not string.startswith(boundary):
    raise ValueError('form-data boundary does not match')
  
  class part(str): pass
  
  def make_part(string):
    headers     = {}
    disposition = {}
    data        = ''
    
    while True:
      n = string.find('\r\n')
      if n == -1:
        raise ValueError('Unexpected EOF while parsing form parts.')
      if n == 0:
        string = string[2:-2]
        break
      
      header, value = string[:n].split(': ', 1)
      headers[header] = value
      string = string[n+2:]
  
    data        = part(string)
    disposition = parse_semi(headers['Content-Disposition'])
    name        = disposition.pop('name')
    for n, value in disposition.items():
        setattr(data, n, value)
    return name, data
  
  string = data[len(boundary + '\r\n'):]
  
  while True:
    n = string.find(boundary)
    if n == -1:
      raise ValueError('unexpected EOF while parsing form-data (ATTN: make sure this script is running with unbuffered stdin, as the default (text-mode on windows) will fail when reading certain non-text characters) (#python -u for unbuffered stdin/out)')
    name, value = make_part(string[:n])
    multipart[name] = value
    if string[n:-2] == boundary + '--':
        break
    string = string[len(boundary) + n + 2:]

  return multipart
  
