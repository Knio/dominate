import tornado.web
import tornado

import logging

log = logging.getLogger('server')

__all__ = ['Server', 'get', 'post', 'add_route', 'server']

class Server(object):
    def __init__(self):
        self.routes = [];
        self.port = 8888

    def make_handler(self, method, func):
        class TornadoHandler(tornado.web.RequestHandler):
            SUPPORTED_METHODS = (method,)

            def _handle(handler, *args, **kwargs):
                r = func(handler, *args, **kwargs)
                # TODO func might do its own writing
                handler.write(unicode(r))
                handler.finish()

            if method == 'GET':
                get = _handle
            if method == 'POST':
                post = _handle

        return TornadoHandler

    def add_route(self, *args):
        self.routes.append(args)

    def get(self, url):
        def f(func):
            handler = self.make_handler(method='GET', func=func)
            self.routes.append((url, handler))
            return func
        return f

    def post(self, url):
        def f(func):
            handler = self.make_handler(method='POST', func=func)
            self.routes.append((url, handler))
            return func
        return f

    def start(self):
        self.application = tornado.web.Application(
            self.routes,
            gzip=True, debug=False,
            cookie_secret='asddfsdfs',
        )

        self.application.listen(self.port)
        log.info('Server started')

    def run(self):
        self.start()
        tornado.ioloop.IOLoop.instance().start()

    def add_static_route(self, route, path):
        self.add_route(route,
            tornado.web.StaticFileHandler,
            dict(path=path))


server  = Server()
get     = server.get
post    = server.post
add_route = server.add_route

if __name__ == '__main__':
    # Example usage
    @get('^/$')
    def index(request):
        return 'Hello World'

    @get('^/u/([a-z0-9]+)$')
    def user(request, username):
        return 'Hi, %s' % username

    run()

