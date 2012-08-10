import re
import os
import imp

'''
Recursive routing utility

A config object is a list of (key, handler) tuples

If multiple handlers would match, the last one is chosen

A key can be:

  1) A regex
      The key matches if the regex matches the URL given

  2) An httperror instance



A handler object can be:

  1) An array
      The part of the URL that matches the regex will be stripped off,
      and the router will search recursively on the rest using the array
      as the new config object



'''


route = [
  ('^/')

]

def route(config, url):
  pass

