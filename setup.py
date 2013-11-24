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

# http://guide.python-distribute.org/creation.html
import dominate

from setuptools import setup

setup(
  name    = 'dominate',
  version = dominate.version,
  author  = 'Tom Flanagan and Jake Wharton',
  author_email = 'tom@zkpq.ca',
  license = 'LICENSE.txt',
  url     = 'http://github.com/Knio/dominate/',

  description      = 'Dominate is a Python library for creating and manipulating HTML documents using an elegant DOM API.',
  long_description = open('README.md').read(),
  keywords         = 'framework templating template html xhtml python html5',

  classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Text Processing :: Markup :: HTML',
  ],
  packages = ['dominate'],
  include_package_data = True,
)
