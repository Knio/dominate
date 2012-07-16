'''
About
=====
`pyy.web` contains useful classes and functions to aid in dealing with the HTTP
protocol and serving websites.


Usage
=====
Cookies
-------
`pyy.web.cookie` allows for easy creation of properly formatted cookies.

The cookie name and value are the only two required fields for its simplest
form:
    >>> cookie('test', 'cookie')
    <pyy.web.cookie.cookie test=cookie; path=/;>

You can also pass any number of the following arguments:
* `expires` - Expiration date (mutually exclusive with `duration`).
* `duration` - Length of cookie (mutually exclusive with `expires`).
* `path` - The URL path of the cookie (default: `/`).
* `domain` - The cookie's domain.
* `secure` - Whether or not the cookie is secure (default: `False`).
* `httponly` - If the cookie applies to only HTTP (default: `False`).

While the string and `__repr__` outputs contain the rendered cookie you can
also call `render()` directly which takes an optional `is_header` boolean.
    >>> cookie('test', 'cookie').render()
    'test=cookie; path=/;'
    >>> cookie('test', 'cookie').render(True)
    'Set-Cookie: test=cookie; path=/;'


HTTP Messages
-------------
`pyy.web.httpmessage` contains the classes for the `httprequest` and
`httpresponse` objects. These two classes hold information on the HTTP requests
and the HTTP responses, respectively, that the other modules pass between
themselves.


Parsers
-------
The `pyy.web.parsers` class contains four functions which aid in parsing common
formats of the HTTP protocol into a more friendly and usable format.

*   `parse_query(string)` - Parses `a=b&c=d` format into a dictionary. Also
    supports arrays.
*   `parse_semi(string)` - Parses `a=b; c=d` format into a dictionary.
*   `parse_user_agent(string)` - Parses a user agent string and returns a
    browser object containing vendor and version.
*   `parse_multipart(content_type, data)` - Parses multipart encoded form data
    into a dictionary.


Resolvers
---------
When serving dynamic web applications it is sometimes useful to obfuscate your
URLs or simple clean them up to be "pretty". The `resolvers` class allows you
to create logical rules or patterns for your URLs and have them easily be
mapped back to approprite classes.

There are currently two methods of dynamic URL resolving: Regex-based and file
heirarchy-based.

Regex-based resolving takes a list of tuples which associate a regular
expression to a class. When a request is resolved in this way the tuples are
iterated over and the first match is taken and returned.
    urls = [
      (r'^/photos/', pages.photos),
      (r'^/videos/', pages.videos),
    ]
If a match is not found, an `httperror` is raised with a 404 code.

You can also use named match groups in your regular expressions to help parse
the URL which will be copied into the request's `GET` mapping.
    urls = [
      (r'^/photos/((?P<id>\d+)/)?$', pages.photos)
    ]
Here an optional ID can be specified after the `/photos/` qualifier and the
`pages.photos` class can react accordingly.

--------
The other type of resolver uses a file system-based heirarchy to determine
which class to associate a URL with.

When you create a directory like the following:
    pages/
          __init__.py
          home.py
          admin/
                __init__.py
                users.py
you can use corresponding URLs to access those classes:
    /             (would match in __init__.py)
    /home/        (would match home.py)
    /home/page2/  (would match home.py with 'page2' put into the request's GET)
    /admin/       (would match admin/__init__.py)
    /admin/users/ (would match admin/users.py)
    /admin/other/ (would match admin/__init.py with 'other' put into the request's GET)

In each of those files should be an Index class which is the default one
selected in a file. If in the case of the `/admin/other/` URL the
`admin/__init__.py` file had an `Other` class it would be the one that was
selected.


Developed By
============
* Tom Flanagan - <theknio@gmail.com>
* Jake Wharton - <jakewharton@gmail.com>

Git repository located at
[github.com/Knio/pyy](http://github.com/Knio/pyy)


License
=======
    Copyright 2009 Tom Flanagan, Jake Wharton

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

from httpmessage import *
from page import page
from url import url
