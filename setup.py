__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy.  If not, see
<http://www.gnu.org/licenses/>.
'''

# http://guide.python-distribute.org/creation.html
from setuptools import setup, find_packages

version = '1.1.13'


setup(
  name    = 'pyy',
  version = version,
  author  = 'Tom Flanagan and Jake Wharton',
  author_email = 'theknio@gmail.com',
  license = 'LICENSE.txt',

  url          = 'http://github.com/Knio/pyy/',
  # download_url = 'http://github.com/Knio/pyy/tarball/' + version,

  description      = 'Python library for creating (X)HTML pages with the use of objects.',
  long_description = 'Python library for creating (X)HTML pages with the use of objects. This allows you to tightly integrate (X)HTML generation into your backend without the need of using an intermediate templating language.',
  keywords         = 'framework templating template html xhtml python html5',

  classifiers = [
    'Programming Language :: Python',
    'Operating System :: OS Independent',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Intended Audience :: Developers',
  ],
  packages   = find_packages(),
  install_requires = [],
  include_package_data = True,
)
