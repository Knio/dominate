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
import tests.html, tests.server, tests.web

#Valid modules to test
VALID = {'html'  : 1,
         'server': 2,
         'web'   : 4,
         'all'   : 7}

#Default to all modules unless any arguments were passed in
pkgs = 0 if len(sys.argv[1:]) else VALID['all']

#Load modules from arguments
for arg in sys.argv[1:]:
  if arg not in VALID:
    print 'INVALID MODULE: %s.' % arg
  else:
    tests |= VALID[arg]

#Assemble individual module tests into array
suites = []
if pkgs & VALID['html']:   suites += defaultTestLoader.loadTestsFromModule(tests.html)
if pkgs & VALID['server']: suites += defaultTestLoader.loadTestsFromModule(tests.server)
if pkgs & VALID['web']:    suites += defaultTestLoader.loadTestsFromModule(tests.web)

#Run tests on each module in the array

def test(verbosity=2):
  return TextTestRunner(verbosity=verbosity).run(TestSuite(suites))

if __name__ == '__main__':
	test()

