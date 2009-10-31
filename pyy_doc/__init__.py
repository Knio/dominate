'''
About
=====
`pyy_doc` uses reflection to generate documentation for modules based on the
docstrings that they contain.

This documentation is presented as a description for the module as well as
multiple dictionaries for the submodules, classes, functions, and constants.
The documentation is also formatted into a `pyy_html.document` which allows
for easy exporting to static HTML or serving via `pyy_httpserver` (or web
server of your choice).


Usage
=====
`pyy_doc` takes only the module name as a string and will return a
`pyy_html.document` that has be preformatted for output but that also
contains the module's description and four dictionaries which hold the
documentation for its submodules, classes, functions, and constants.

Run `pyy_doc` on the `os` module to grab all its documentation and show
some of what it parsed:
    >>> d = pyy_doc('os')
    >>> d.description[:50]
    'OS routines for Mac, NT, or Posix depending on wha'
    >>> len(d.submodules)
    4
    >>> len(d.classes)
    3
    >>> len(d.functions)
    23
    >>> len(d.constants)
    172

Remember `d` is also a `pyy_html.document` instance so we can output static
HTML of the documentation for easier browsing.
    >>> d
    <pyy_html.document.document "os - Documentation">
    >>> f = open('os.html', 'w')
    >>> f.write(d.render())
    >>> f.close()

These HTML documents do not contain any CSS styling rules but the sections do
have classes and ids assigned for formatting. You can add a style by adding a
`link` or `style` tag into `d.head` before you call `render()`.


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