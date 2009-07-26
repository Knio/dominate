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

import os
import sys
from urllib import unquote_plus


def get_multipart(data):
    '''
    This method *MUST* be run with unbuffered input!
    python -u
    '''
    content_type = parse_semi(env['CONTENT_TYPE'])
    
    boundary = '--'+content_type['boundary']
    
    print 'BOUNDARY =',boundary
    
    string = data
    if not string.startswith(boundary):
        raise ValueError('form-data boundary does not match')
        
    class part(str):
        pass
        
    def make_part(string):
        headers     = {}
        disposition = {}
        data        = ''
        
        while 1:
            n = string.find('\r\n')
            if n == -1:
                raise ValueError('unexpected EOF while parsing form part')
            if n == 0:
                string = string[2:-2]
                break
            header, value = string[:n].split(': ', 1)
            headers[header] = value
            string = string[n+2:]
        data        = part(string)
        disposition = parse_semi(headers['Content-Disposition'])
        name = disposition.pop('name')
        for n, v in disposition.items():
            setattr(data, n, v)
        return name, data
    
    string  = data[len(boundary+'\r\n'):]
    parts   = {}
    while 1:
        print '<pre>'+string+'</pre>'
        n = string.find(boundary)
        if n == -1:
            raise ValueError('unexpected EOF while parsing form-data (ATTN: make sure this script is running with unbuffered stdin, as the default (text-mode on windows) will fail when reading certain non-text characters) (#python -u for unbuffered stdin/out)')
        name, value = make_part(string[:n])
        parts[name] = value
        if string[n:-2] == boundary+'--':
            break
        string = string[len(boundary)+n+2:]
    return parts

def parse_semi(string):
    d = {}
    for i in string.split('; '):
        try:
            k, v = i.split('=',1)
        except ValueError:
            k, v = '', i
        d[k] = v
    return d

def parse_query(string):
    d = {}
    string = string.split('&')
    for i in filter(None, string):
        array = False
        try:
            key, value = map(unquote_plus, i.split('=', 1))
            if key.endswith('[]'):
                key = key[:-2]
                array = True
        except ValueError:
            key, value = unquote_plus(i), ''
        if array:
            if key in d:
                d[key].append(value)
            else:
                d[key] = [value]
        else:
            d[key] = value
    return d

def get_post(data):
    if not env['REQUEST_METHOD'] == 'POST':
        return {}
    if env['CONTENT_TYPE'].startswith('multipart/form-data'):
        return get_multipart(data)
    if env['CONTENT_TYPE'].startswith('application/x-www-form-urlencoded'):
        return parse_query(data)
    return {'_error':'unknown content type %s' % env['CONTENT_TYPE']}

def get_get(uri):
    try:
        from urls import urls
        import re
        for regex, pageclass in urls:
            match = re.match(regex, uri)
            if match:
                return pageclass, match.groupdict()
    except ImportError:
        pass
    return None, None

def get_cookie():
    if 'HTTP_COOKIE' not in env:
        return {}
    return parse_semi(env['HTTP_COOKIE'])


env = os.environ

localfile = env.get('SCRIPT_FILENAME','')
localroot = env.get('DOCUMENT_ROOT'  ,'')

server = env.get('SERVER_NAME')
if env.get('SERVER_PORT') and env.get('SERVER_PORT') != '80':
    server += ':' + env.get('SERVER_PORT')

assert localfile.startswith(localroot)
urlroot = '/'
urlfile = localfile[len(localroot):]
    
fullurlroot = 'http://%s' % server
fullurlfile = fullurlroot + urlfile

data = sys.stdin.read()
post = get_post(data)

get = parse_query(env.get('QUERY_STRING',''))
pageclass, uri_get = get_get(env.get('SCRIPT_URL',''))
if pageclass:
    get.update(uri_get)
    page = pageclass()
    page.get  = get
    page.post = post

if 'PATH_INFO' in env:
    info = env['PATH_INFO'].split('/')[1:]
else:
    info = []
infop = '/'.join(info)


# browser information
user_agent = env.get('HTTP_USER_AGENT', '')

is_internetexplorer5 = 'MSIE 5.'  in env.get('HTTP_USER_AGENT', '')
is_internetexplorer6 = 'MSIE 6.0' in env.get('HTTP_USER_AGENT', '')
is_internetexplorer7 = 'MSIE 7.0' in env.get('HTTP_USER_AGENT', '')
is_internetexplorer8 = 'MSIE 8.0' in env.get('HTTP_USER_AGENT', '')
is_internetexplorermobile = 'Windows CE' in env.get('HTTP_USER_AGENT', '')
is_internetexplorer = is_internetexplorer6 or is_internetexplorer7 or is_internetexplorer8 or is_internetexplorermobile

# chrome  Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13
is_chrome = ('Chrome' in env.get('HTTP_USER_AGENT', ''))

# safari2 Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/XX (KHTML, like Gecko) Safari/YY
# safari3 Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/XX (KHTML, like Gecko) Version/ZZ Safari/YY
is_safari = 'AppleWebKit' in env.get('HTTP_USER_AGENT', '') and not is_chrome
is_safari2 = is_safari and not 'Version' in env.get('HTTP_USER_AGENT', '')
is_safari3 = is_safari and     'Version' in env.get('HTTP_USER_AGENT', '')
is_safarimobile = is_safari and 'iPhone' in env.get('HTTP_USER_AGENT', '')

is_firefoxmobile = 'Fennec' in env.get('HTTP_USER_AGENT', '')

is_opera = 'Opera' in env.get('HTTP_USER_AGENT', '')
is_operamobile = is_opera and 'Mini' in env.get('HTTP_USER_AGENT', '')

is_mobile = is_internetexplorermobile or is_safarimobile or is_firefoxmobile or is_operamobile

# googlebot Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)              
is_googlebot = 'Googlebot/2.1' in user_agent


def path(*args):
    p = os.path.dirname(env['SCRIPT_NAME'])
    if p == '/': p = ''
    return os.path.join(*([p] + list(args))).replace('\\','/')
    
def fpath(*args):
    p = env['SCRIPT_NAME']
    return os.path.join(*([p] + list(args))).replace('\\','/')
