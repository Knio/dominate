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

import datetime

class cookie(object):
    def __init__(self, name, value, expires=None, duration=None, path='/',
                 domain=None, secure=False, httponly=False):
        
        if duration and expires:
            raise ValueError('cookie cannot have both expiry date and duration')
        
        self.name     = name.lower()
        self.value    = value
        self.path     = path
        self.expires  = expires
        self.duration = duration
        self.domain   = domain
        self.secure   = secure
        self.httponly = httponly

    def render(self, header=False):
        timestamp = None
        if self.expires:
            if isinstance(self.expires, datetime.datetime):
                timestamp = self.expires
            elif isinstance(self.expires, float) or \
                 isinstance(self.expires, int):
                timestamp = datetime.datetime.utcfromtimestamp(self.expires)
            else:
                raise TypeError('Invalid expiry time. Implement me!')
        if self.duration:
            timestamp = datetime.datetime.utcnow()
            if isinstance(self.duration, float) or \
               isinstance(self.duration, int):
                timestamp += datetime.timedelta(seconds=self.duration)
            else:
                raise TypeError('Invalid duration. Implement me!')
        
        cookie = []
        cookie.append('%s=%s;' % (self.name, self.value))
        cookie.append('path=%s;' % self.path)
        if timestamp:     cookie.append('expires=%s;' % timestamp.strftime("%a, %d-%b-%Y %H:%M:%S GMT"))
        if self.domain:   cookie.append('domain=%s;' % self.domain)
        if self.secure:   cookie.append('secure;')
        if self.httponly: cookie.append('httponly;')
        
        return ('Set-Cookie: ' if header else '') + ' '.join(cookie)


if __name__ == '__main__':
    assert cookie('hi', 'abc').render() == 'hi=abc; path=/;'
    assert cookie('hi', '123', expires=10, secure=1, httponly=1).render(True) == 'Set-Cookie: hi=123; path=/; expires=Thu, 01-Jan-1970 00:00:10 GMT; secure; httponly;'
