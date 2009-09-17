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

from pyy_web.httpmessage import httprequest
import re

def resolve(urls, request=None):
    if request is None:
        request = httprequest.read()
    
    for regex, pageclass in urls:
        match = re.match(regex, request.uri)
        if match:
            request.get.update(match.groupdict())
            return pageclass(request=request)
    raise ValueError("URI did not resolve to a class.")
