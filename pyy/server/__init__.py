'''
About
=====
`pyy.httpserver` is a lightweight, highly configurable web server written using
stackless python for ultimate effeciency.

__`pyy.httpserver` is still considered highly experimental.__


Usage
=====
`pyy.httpserver` allows you to serve files with different pluggable modules
based upon a variety of conditions.

The server is configured with a series of specifiers and handlers arranged in
a list:
    [ SPECIFIER, HANDLER, ... ]

`SPECIFIER` must be one of:

* A regular expression string will match that hostname (or uri, in a sub-handler).
* An HTTP error code matches that code.
* `httperror` matches all errors.
* `None` will match `None` or the empty string.
* `True` will match everything.

If no specifiers match, an httperror(404) will be returned.

If multiple specifiers match, the last one will be used. If the last one
returns a 404 error, then the second last one will be used, etc.

*Note that if a leaf-node (final handler) raises a 404, that error will be
handled normally and will not cause the resolver to keep looking.*

`HANDLER` must be one of:

* `[ SPECIFIER, HANDLER, ...]` to do further processing.
* A function object will be called with `f(*args)` where `args` is a list of all regex matches that were encountered in the entire processing of this request. The function's return value will then be used as a new `HANDLER`.
* A handler object will be called with `.handle(httpserver, request, response, *args)` (or `.handle_error(..)` if this is an error match).
* `None` to do nothing.
* An `httperror` instance to raise that error.

You can see an example server configuration [here](http://github.com/Knio/pyy/blob/master/docs/example/run.py).


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
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy.  If not, see
<http://www.gnu.org/licenses/>.
'''

# from server             import server
from httpserver         import httpserver
from fileserver         import *
from filterserver       import *
from pyyserver          import *
from syntaxfileserver   import *
