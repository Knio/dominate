__license__ = '''
This file is part of Dominate.

Dominate is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

Dominate is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with dominate.  If not, see
<http://www.gnu.org/licenses/>.
'''
# pylint: disable=bad-whitespace

from setuptools import setup

import imp
_version = imp.load_source("dominate._version", "dominate/_version.py")

long_description = open('README.md').read()

setup(
  name    = 'dominate',
  version = _version.__version__,
  author  = 'Tom Flanagan and Jake Wharton',
  author_email = 'tom@zkpq.ca',
  license = 'LGPLv3',
  url     = 'https://github.com/Knio/dominate/',
  description      = 'Dominate is a Python library for creating and manipulating HTML documents using an elegant DOM API.',
  long_description = long_description,
  long_description_content_type='text/markdown',
  keywords         = 'framework templating template html xhtml python html5',

  classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Markup :: HTML',
  ],

  packages = ['dominate'],
  include_package_data = True,
)
