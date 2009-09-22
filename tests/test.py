#!/usr/bin/env python

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

#Ensure we get the repository version and not an installed version
import sys
sys.path.insert(0, '..')

#Change tabs to tab character to simplify comparisons
from pyy_html.pyy_tag import pyy_tag
pyy_tag.TAB = '\t'

from unittest import defaultTestLoader, TestSuite, TextTestRunner
import pyy_cgi_tests, pyy_html_tests, pyy_httpserver_tests, pyy_web_tests

#Create individual module suites
suite_pyy_cgi        = defaultTestLoader.loadTestsFromModule(pyy_cgi_tests)
suite_pyy_html       = defaultTestLoader.loadTestsFromModule(pyy_html_tests)
suite_pyy_httpserver = defaultTestLoader.loadTestsFromModule(pyy_httpserver_tests)
suite_pyy_web        = defaultTestLoader.loadTestsFromModule(pyy_web_tests)

#Create entire package suite
suite_pyy = TestSuite([suite_pyy_cgi, suite_pyy_html, suite_pyy_httpserver, suite_pyy_web])

TextTestRunner(verbosity=2).run(suite_pyy)
