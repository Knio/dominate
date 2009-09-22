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
import os
import test
from pyy_web.resolve import RegexResolver, FileHeirarchyResolver

class Request:
  def __init__(self, uri):
    self.uri = uri


path = os.path.join('pyy_web_tests', 'test')

class ResolverTests(unittest.TestCase):
  def testSelectIndexInFile(self):
    self.assertTrue(isinstance(FileHeirarchyResolver(path, Request('admin/a/'), None), test.admin.a.Index))
  
  def testSelectClassInFile(self):
    self.assertTrue(isinstance(FileHeirarchyResolver(path, Request('admin/a/test'), None), test.admin.a.Test))
  
  def testErrorWhenNoIndex(self):
    try:
      FileHeirarchyResolver(path, Request('admin/hi/'), None)
      self.fail()
    except ValueError:
      pass
