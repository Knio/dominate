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

import os, sys, re
from urllib import unquote_plus


class request:
    def __init__(self, data=''):
        self.env  = os.environ
        self.data = data
        
        #Parse cookies
        self.cookies = parse_semi(self.env.get('HTTP_COOKIE', ''))
        
        #Parse GET
        self.get = parse_query(self.env.get('QUERY_STRING', ''))
        
        #Parse POST
        self.post = {}
        if self.env.get('REQUEST_METHOD') == 'POST':
            if self.env.get('CONTENT_TYPE', '').startswith('multipart/form-data'):
                self._parse_multipart()
            if self.env.get('CONTENT_TYPE', '').startswith('application/x-www-form-urlencoded'):
                self.post.update(_parse_query(self.data))
        
        self._parse_user_agent()
        self._resolve_to_class()
        
        self.localfile = self.env.get('SCRIPT_FILENAME','')
        self.localroot = self.env.get('DOCUMENT_ROOT'  ,'')
        
        self.server = self.env.get('SERVER_NAME')
        if self.env.get('SERVER_PORT') and self.env.get('SERVER_PORT') != '80':
            self.server += ':' + self.env.get('SERVER_PORT')
        
        assert self.localfile.startswith(self.localroot)
        self.urlroot = '/'
        self.urlfile = self.localfile[len(self.localroot):]
        
        self.fullurlroot = 'http://' + self.server
        self.fullurlfile = self.fullurlroot + self.urlfile
        
        self.info  = filter(None, self.env.get('PATH_INFO', '/').split('/')[1:])
        self.infop = '/'.join(self.info)
    
    @staticmethod
    def read():
        return request(sys.stdin.read())
    
    def _parse_multipart(self):
        '''
        This method *MUST* be run with unbuffered input!
        python -u
        '''
        content_type = _parse_semi(self.env['CONTENT_TYPE'])
        boundary     = '--' + content_type['boundary']
        
        print 'BOUNDARY =', boundary
        
        string = self.data
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
            name = disposition.pop('name')
            for n, value in disposition.items():
                setattr(data, n, value)
            return name, data
        
        string = data[len(boundary + '\r\n'):]
        while True:
            print '<pre>' + string + '</pre>'
            n = string.find(boundary)
            if n == -1:
                raise ValueError('unexpected EOF while parsing form-data (ATTN: make sure this script is running with unbuffered stdin, as the default (text-mode on windows) will fail when reading certain non-text characters) (#python -u for unbuffered stdin/out)')
            name, value = make_part(string[:n])
            self.post[name] = value
            if string[n:-2] == boundary + '--':
                break
            string = string[len(boundary) + n + 2:]
    
    def _parse_query(string):
        d = {}
        string = string.split('&')
        for pair in filter(None, string):
            is_array = False
            try:
                key, value = map(unquote_plus, pair.split('=', 1))
                if key.endswith('[]'):
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
    
    def _parse_semi(string):
        d = {}
        for pair in filter(None, string.split('; ')):
            try:
                key, value = pair.split('=',1)
            except ValueError:
                key, value = '', pair
            d[key] = value
        return d
    
    
    BROWSER_IE      = 0
    BROWSER_FIREFOX = 1
    BROWSER_CHROME  = 2
    BROWSER_SAFARI  = 3
    BROWSER_OPERA   = 4
    
    USER_AGENT_REGEX = (
        (re.compile(r'MSIE (?P<version>(?P<major>\d+)(?:\.(?P<minor>\d+))?)'), BROWSER_IE, 'Windows CE'),
        (re.compile(r'Firefox/(?P<version>(?P<major>\d+)\.(?P<minor>\d+)(?:\.(?P<release>\d+)(?:\.(?P<build>\d+))?)?((a|b)(?P<beta>\d+))?)'), BROWSER_FIREFOX, 'Fennec'),
        (re.compile(r'Chrome/(?P<version>(?P<major>\d+)\.(?P<minor>\d+)(?:\.(?P<release>\d+)(?:\.(?P<build>\d+))?)?)'), BROWSER_CHROME, 'asdfadsfadsfadsf'),
        (re.compile(r'Version/(?P<version>(?P<major>\d+)\.(?P<minor>\d+)(?:\.(?P<release>\d+))?)'), BROWSER_SAFARI, 'iPhone'),
        (re.compile(r'Opera(/| )(?P<version>(?P<major>\d+)\.(?P<minor>\d+))'), BROWSER_OPERA, 'Mini'),
    )
    
    def _parse_user_agent(self):
        if not 'HTTP_USER_AGENT' in self.env:
            return
        
        user_agent = self.env['HTTP_USER_AGENT']
        for regex, browser, mobile_string in request.USER_AGENT_REGEX:
            match = re.search(regex, user_agent)
            if match:
                self.browser   = browser
                self.is_mobile = mobile_string in user_agent
                
                for name, value in match.groupdict().iteritems():
                    if value:
                        setattr(self, name, value)
                
                return
        
        # googlebot Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)
        self.is_googlebot = 'Googlebot/2.1' in user_agent
        
        self.is_robot = self.is_googlebot

    def _resolve_to_class(self):
        try:
            if 'SCRIPT_URL' not in self.env:
                return
            
            import urls
            
            for regex, pageclass in urls.urls:
                match = re.match(regex, self.env['SCRIPT_URL'])
                if match:
                    return pageclass, match.groupdict()
            raise ValueError("URI did not resolve to a class.")
        except ImportError:
            pass
    
    def path(self, *args):
        p = os.path.dirname(self.env.get('SCRIPT_NAME', ''))
        if p == '/': p = ''
        return os.path.join(*([p] + list(args))).replace('\\','/')
    
    def fpath(self, *args):
        return os.path.join(*([self.env.get('SCRIPT_NAME', '')] + list(args))).replace('\\','/')
