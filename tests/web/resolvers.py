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
from pyy.web         import httperror
from pyy.web.resolve import RegexResolver, FileHeirarchyResolver

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test')


class Request:
  def __init__(self, uri):
    self.uri = uri


class ResolverTests(unittest.TestCase):
  def testSelectIndexInFolder(self):
    p = FileHeirarchyResolver(path, Request('admin/'))
    self.assertEqual(str(p.__class__), "<class '__init__.Index'>")
  
  def testSelectIndexInFile(self):
    p = FileHeirarchyResolver(path, Request('admin/a/'))
    self.assertEqual(str(p.__class__), "<class 'a.Index'>")
  
  def testSelectClassInFile(self):
    p = FileHeirarchyResolver(path, Request('admin/a/test'))
    self.assertEqual(str(p.__class__), "<class 'a.Test'>")
  
  def testErrorWhenNoIndex(self):
    try:
      FileHeirarchyResolver(path, Request('admin/hi/'))
      self.fail()
    except httperror:
      pass
