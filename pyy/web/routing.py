import re

routes = []

def get(regex):
  routes.append(regex_router(regex, 'GET'))
  return lambda x: x

def post(regex):
  routes.append(regex_router(regex, 'POST'))
  return lambda x: x

def directory(root):
  routes.append(directory_router(root))
  return lambda x: x


class router(object):
  def match(self, uri, method):
    return False

class regex_router(router):
  def __init__(self, regex, method=None):
    self.regex = re.compile(regex)
    self.method = method

  def match(self, uri, method):
    if self.method is None or method is self.method:
      return bool(self.regex.match(uri))
    return False

class directory_router(router):
  def __init__(self, root):
    pass

def match(uri, method):
  for route in routes:
    #TODO handle non-router instances
    if route.match(uri, method):
      print('what now?')
  return _default


def _default(*args):
  return 'No routes specified'