'''
About
=====
`pyy.cgi` provides a common standardized interface between a web server and a
dynamic application being used to serve content.


Usage
=====
If you are working within a CGI environment using `pyy_cgi` will allow your
application to fail somewhat gracefully and will provide you with an easy means
to access the request and response parameters.

Simply add `import pyy_cgi` as the first line in your file to activate the
module. Then define one or more functions that correspond with HTTP methods to
be called for a request.
    def get(handler, request, response):
        response.body = 'Hello, World!'

Be sure to designate a function for each HTTP method you would like to support
because an HTTP 405 error will be generated if no appropriate function is
found. If you do all your processing in the same place as your generation you
can simply add `post = get` to pass in all the POST requests.

Should your file have a syntax error or produce a run-time error `pyy_cgi` will
catch and display it rather than just causing the server to produce an HTTP 500
error.


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

import cgi
