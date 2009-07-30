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

from request import request as req
import re

def resolve(urls, request=None):
    if not request:
        request = req.read()
    
    uri = request.env['SCRIPT_URL']
    for regex, pageclass in urls:
        match = re.match(regex, uri)
        if match:
            request.get.update(match.groupdict())
            return pageclass(request=request)
    raise ValueError("URI did not resolve to a class.")
