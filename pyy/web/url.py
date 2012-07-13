import re
from collections import defaultdict

URL_REGEX = ('^('
    '((?P<protocol>\w+)://)?'
    '(?P<host>[^\\/\\\\?]+)?'
    # TODO add ports
    '(?P<path>[^?]+)?'
    '(\?(?P<args>[^#]*))?'
    '(#(?P<anchor>.+))?'
    ')$')


FORM_URLENCODING_REGEX = ('^('
    '(?P<var>[^=]+=[^&]*(&[^=]+=[^&]*)*)?'
    ')$')


class url(object):
    def __init__(self, data=None, **kwargs):
        self.protocol = None
        self.host = None
        self.path = '/'
        self.args = {}
        self.anchor = None
        if data is None:
            pass
        elif isinstance(data, basestring):
            m = re.match(URL_REGEX, data)
            if m:
                self.update(**dict(i for i in m.groupdict().items() if i[1]))
        elif isinstance(data, url):
            self.protocol = data.protocol
            self.host = data.host
            self.path = data.path
            self.args = data.args
            self.anchor = data.anchor
            if isinstance(self.args, dict):
                self.args = dict(self.args)
        else:
            raise ValueError

        self.update(**kwargs)

        a = self.parse_arguments(self.args)
        if a:
            self.args = a

    def update(self, **args):
        # TODO check args are only proto, host, path, etc
        for k, v in args.iteritems():
            setattr(self, k, v)
        return self

    def update_args(self, *a, **kw):
        # TODO whaf if args isnt a dict?
        self.args.update(*a, **kw)
        return self

    @staticmethod
    def parse_arguments(data):
        if not isinstance(data, basestring):
            return None
        match = re.match(FORM_URLENCODING_REGEX, data)
        if not match:
            return None
        argstring = match.group('var')
        if not argstring:
            return None

        args = defaultdict(list)
        for j in argstring.split('&'):
            k, x = j.split('=', 1)
            args[k].append(x)

        argsf = {}
        for k, v in args.items():
            if len(v) == 1:
                argsf[k] = v[0]
            else:
                argsf[k] = v

        return argsf

    def get_arg(self, arg, default=None):
        return self.args and self.args.get(arg, default)

    def get_args(self, arg):
        if not isinstance(self.args, dict):
            return None
        v = self.args.get(arg, [])
        if not isinstance(v, (list, tuple)):
            return [v]
        return v

    __getitem__ = get_arg

    def __setitem__(self, arg, val):
        if not isinstance(self.args, dict):
            raise ValueError('url arguments are not form encoded')
        self.args[arg] = val

    def __str__(self):
        ret = []
        host = self.host
        if self.protocol is not None:
            ret.append('%s://' % self.protocol)
            host = host or ''

        if host is not None:
            ret.append(host)

        if self.path is not None:
            ret.append(unicode(self.path))

        if self.args is None:
            pass
        elif isinstance(self.args, basestring):
            ret.append('?%s' % self.args)
        elif isinstance(self.args, dict):
            a = []
            for k, v in self.args.iteritems():
                if isinstance(v, (basestring, int, long, float)):
                    a.append('%s=%s' % (unicode(k), unicode(v)))
                if isinstance(v, (list, tuple)):
                    for j in v:
                        a.append('%s=%s' % (unicode(k), unicode(j)))
            if a:
                ret.append('?' + '&'.join(a))
        else:
            ret.append('?' + unicode(self.args))

        if self.anchor is not None:
            ret.append('#' + unicode(self.anchor))

        return ''.join(ret)

    __unicode__ = __str__


if __name__ == '__main__':
    print url()
    print url('/moo')
    print url('http://moo')
    print url('http:///moo')
    print url('http://moo.com')
    print url('http://moo.com/')
    print url('http://moo.com/foo')
    print url('http://moo.com/foo/bar/')
    print url('http://moo.com/foo/bar?')
    print url('http://moo.com/foo/bar/?var=1')
    print url('http://moo.com/foo/bar/?var=1&baz=dog')
    print url('http://moo.com/foo/bar/?var=1&baz=dog&var=3')
    print url('http://moo.com/foo/bar/?var=1&baz=dog&var=3#here')
    assert url('?moo=1')['moo'] == '1'
    print url(url('?moo=1'))
    print url(url('?moo=1')).update_args(bar=2)
