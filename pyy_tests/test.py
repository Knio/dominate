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
import os
import sys
sys.path.insert(0, os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

from unittest import defaultTestLoader, TestSuite, TextTestRunner
import pyy_cgi_tests, pyy_doc_tests, pyy_html_tests, pyy_httpserver_tests, pyy_web_tests

#Valid modules to test
VALID = {'pyy_cgi'       : 1,
         'pyy_doc'       : 2,
         'pyy_html'      : 4,
         'pyy_httpserver': 8,
         'pyy_web'       : 16,
         'all'           : 31}

#Default to all modules unless any arguments were passed in
tests = 0 if len(sys.argv[1:]) else VALID['all']

#Load modules from arguments
for arg in sys.argv[1:]:
  if arg not in VALID:
    print 'INVALID MODULE: %s.' % arg
  else:
    tests |= VALID[arg]

#Assemble individual module tests into array
suites = []
if tests & VALID['pyy_cgi']:        suites += defaultTestLoader.loadTestsFromModule(pyy_cgi_tests)
if tests & VALID['pyy_doc']:        suites += defaultTestLoader.loadTestsFromModule(pyy_doc_tests)
if tests & VALID['pyy_html']:       suites += defaultTestLoader.loadTestsFromModule(pyy_html_tests)
if tests & VALID['pyy_httpserver']: suites += defaultTestLoader.loadTestsFromModule(pyy_httpserver_tests)
if tests & VALID['pyy_web']:        suites += defaultTestLoader.loadTestsFromModule(pyy_web_tests)

#Run tests on each module in the array

def test()
  return TextTestRunner(verbosity=2).run(TestSuite(suites))

if __name__ == '__main__':
	test()
	
