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

import unittest
from pyy.web.cookie import *

class CookieTests(unittest.TestCase):
  def testSimpleCookie(self):
    self.assertEqual(cookie('hi', 'abc').render(), 'hi=abc; path=/;')
  
  def testComplexCookie(self):
    self.assertEqual(cookie('hi', '123', expires=10, secure=1, httponly=1).render(True), 'Set-Cookie: hi=123; path=/; expires=Thu, 01-Jan-1970 00:00:10 GMT; secure; httponly;')
