import datetime

class cookie(object):
    def __init__(self, name, value, expires=None, duration=None, path='/',
                 domain=None, secure=False, httponly=False):
        
        if duration and expires:
            raise ValueError('cookie cannot have both expiry date and duration')
        
        self.name   = name.lower()
        self.value  = value
        self.path       = path
        self.expires    = expires
        self.duration   = duration
        self.domain     = domain
        self.secure     = secure
        self.httponly   = httponly
        

    def render(self, header=False):
        n = None
        if self.expires:
            if isinstance(self.expires, datetime.datetime):
                n = self.expires
            elif isinstance(self.expires, float) or \
                 isinstance(self.expires, int):
                n = datetime.datetime.utcfromtimestamp(self.expires)
            else:
                raise TypeError('invalid expiry time. implement me!')
        if self.duration:
            n = datetime.datetime.utcnow()
            if isinstance(self.duration, float) or \
               isinstance(self.duration, int):
                n +=  datetime.timedelta(seconds=self.duration)
            else:
                raise TypeError('invalid duration. implement me!')
        
        cookie = []
        cookie.append('%s=%s;' % (self.name, self.value))
        cookie.append('path=%s;' % self.path)
        if n:   cookie.append('expires=%s;' % n.strftime("%a, %d-%b-%Y %H:%M:%S GMT"))
        if self.domain:     cookie.append('domain=%s;' % self.domain)
        if self.secure:     cookie.append('secure;')
        if self.httponly:   cookie.append('httponly;')
        
        return (header and 'Set-Cookie: ' or '') + ' '.join(cookie)


if __name__ == '__main__':
    assert cookie('hi', 'abc').render() == 'hi=abc; path=/;'
    assert cookie('hi', '123', expires=10, secure=1, httponly=1).render(True) == 'Set-Cookie: hi=123; path=/; expires=Thu, 01-Jan-1970 00:00:10 GMT; secure; httponly;'


    

