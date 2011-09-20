import re

_routes = []

def get(regex):
  def inner(func):
    _routes.append(regex_router(func, regex, 'GET'))
    return func
  return inner

def post(regex):
  def inner(func):
    _routes.append(regex_router(func, regex, 'POST'))
    return func
  return inner

def put(regex):
  def inner(func):
    _routes.append(regex_router(func, regex, 'PUT'))
    return func
  return inner

def delete(regex):
  def inner(func):
    _routes.append(regex_router(func, regex, 'DELETE'))
    return func
  return inner

def directory(root):
  def inner(func):
    _routes.append(directory_router(func, root))
    return func
  return inner


class router(object):
  def match(self, uri, method):
    return False

class regex_router(router):
  def __init__(self, func, regex, method=None):
    self.func = func
    self.regex = re.compile(regex)
    self.method = method

  def match(self, uri, method):
    if self.method is None or method is self.method:
      return bool(self.regex.match(uri))
    return False

class directory_router(router):
  def __init__(self, func, root):
    self.func = func
    self.root = root


def match(uri, method):
  for route in _routes:
    #TODO handle non-router instances
    if route.match(uri, method) and route.func:
        return route.func
  return _default


def _default(*args):
  return 'No routes specified'