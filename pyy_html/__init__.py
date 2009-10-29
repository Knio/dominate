'''
About
=====
`pyy_html` allows for creating (X)HTML markup through the use of objects.
This allows you to tightly integrate (X)HTML generation into your backend
without the need of using an intermediate templating language.

`pyy_html` also provides you with helper classes for generating and parsing
(X)HTML documents.

--DESCRIBE TAGS AND SUCH HERE--

The `parser` class contains two methods: `parse` and `pageparse`. `parse` will
take valid and mostly-valid (X)HTML input and return a tag tree. `pageparse`
will take an entire document and return a `document` instance complete with
the DOCTYPE (if present) and a tag tree using the (X)HTML version specified
by the DOCTYPE.


Usage
=====
All these examples assume you have imported the appropriate tags or entire tag
set (i.e. `from pyy_html.html import *`).

Hello, pyy!
-----------
Constructing a "Hello, World!"-style example is as easy as this:
    >>> print html(body(h1('Hello, pyy!')))
    <html>
      <body>
        <h1>Hello, pyy!</h1>
      </body>
    </html>


Complex Structures
------------------
Through the use of the `+=` operator and the `.add()` method you can easily
create more advanced structures.

Create a simple list:
    >>> list = ul()
    >>> for item in range(4):
    >>>   list += li('Item #', item)
    >>> print list
    <ul>
      <li>Item #0</li>
      <li>Item #1</li>
      <li>Item #2</li>
      <li>Item #3</li>
    </ul>

If you are using a database or other backend to fetch data, `pyy_html` supports
iterables to help streamline your code:
    >>> print ul(li(a(name, href=link), __inline=True) for name, link in menu_items)
    <ul>
      <li><a href="/home/">Home</a></li>
      <li><a href="/about/">About</a></li>
      <li><a href="/downloads/">Downloads</a></li>
      <li><a href="/links/">Links</a></li>
    </ul>

A simple document tree:
    >>> _html = html()
    >>> _body = _html.add(body())
    >>> header  = _body.add(div(id='header'))
    >>> content = _body.add(div(id='content'))
    >>> footer  = _body.add(div(id='footer'))
    >>> print _html
    <html>
      <body>
        <div id="header"></div>
        <div id="content"></div>
        <div id="footer"></div>
      </body>
    </html>

For clean code, the `.add()` method returns children in tuples. The above
example can be cleaned up and expanded like this:
    >>> _html = html()
    >>> _head, _body = _html.add(head(title('Simple Document Tree')), body())
    >>> names = ['header', 'content', 'footer']
    >>> header, content, footer = _body.add(div(id=name) for name in names)
    >>> print _html
    <html>
      <head>
        <title>Simple Document Tree</title>
      </head>
      <body>
        <div id="header"></div>
        <div id="content"></div>
        <div id="footer"></div>
      </body>
    </html>

You can modify the attributes of tags through a dictionary-like interface:
    >>> header = div()
    >>> header['id'] = 'header'
    >>> print header
    <div id="header"></div>

Comments can be created using objects too!
    >>> print comment('BEGIN HEADER')
    <!--BEGIN HEADER-->
    >>> print comment(p('Stop using IE5!'), condition='lt IE6')
    <!--[if lt IE6]>
    <p>Stop using IE5!</p>
    <![endif]-->

Creating Documents
------------------
...


Markup Validation
-----------------
Once you have created a document validating its tags is extremely easy.

Import the DTD specification that you wish to validate against and set it as
the desired doctype in your document. This will automatically trigger
the validation.
    >>> d = document()
    
    ... add tags to d ...
    
    >>> from pyy_html.dtd import xhtml11
    >>> d.setdoctype(xhtml11)

If nothing happens when you call `setdoctype` then everything passed the
validation! However, if you received an error then your document did not pass
and the error will contain relevant information as to what the problem was.

You can also pass a doctype on your document object creation as a keyword
argument and validation testing will occur when the document is rendered.
    >>> from pyy_html.dtd import html5
    >>> d = document(doctype=html5)


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

from html     import *
from document import document
from parser   import parse, pageparse
import dtd