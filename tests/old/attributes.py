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
from pyy.html.tags import *
from pyy.html.util import *


class AttributeTests(unittest.TestCase):
  def testAddViaDict(self):
    i = img()
    i['src'] = 'test.png'
    self.assertEqual(str(i), '<img src="test.png">')

  def testAddViaKeywordArg(self):
    i = img(src='test.png')
    self.assertEqual(str(i), '<img src="test.png">')

  def testBooleanAttribute(self):
    i = img(test=True)
    self.assertEqual(str(i), '<img test="test">')

  def testUtils(self):
    d = div()
    d += system('echo hi')
    self.assertEqual(str(d), '<div>hi\n</div>')

