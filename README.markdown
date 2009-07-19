About
=====
`pyy` is a python library for creating (X)HTML pages with the use of objects.
This allows you to tightly integrate (X)HTML generation into your backend
without the need of using an intermediate templating language.

`pyy` also provides you with helper classes for generating and parsing (X)HTML
documents.

Each specification includes an `htmlpage` class that aids in the creation of
all aspects needed to respond to an HTTP request. The (X)HTML tree you created
can be packaged with a DOCTYPE, XML declaration, and any cookies you wish to
send. When rendered, this class will automatically format all of the contained
information properly.

The `parser` class contains two methods: `parse` and `pageparse`. `parse` will
take valid and mostly-valid (X)HTML input and return a tag tree. `pageparse`
will take an entire document and return an `htmlpage` instance complete with
the XML declaration and DOCTYPE (if present) and a tag tree using the (X)HTML
version specified by the DOCTYPE.


Usage
=====
All these examples assume you have imported the appropriate classes from one of
the (X)HTML specification files (i.e. `from xhtml11 import *`).

Hello, pyy!
-----------
Constructing a "Hello, World!"-style example is as easy as this:
    >>> print html(body(h1("Hello, pyy!")))
    <html xmlns="http://www.w3.org/1999/xhtml">
      <body>
        <h1>Hello, pyy!</h1>
      </body>
    </html>

Notice how the class automatically adds the XHTML 1.1 required `<html>`
attribute `xmlns`.

Complex Structures
------------------
Through the use of the `+=` operator and the `.add()` method you can easily
create more advanced structures.

Create a simple list:
    >>> list = ul()
    >>> for item in range(4):
    >>>   list += li("Item #", item)
    >>> print list
    <ul>
      <li>Item #0</li>
      <li>Item #1</li>
      <li>Item #2</li>
      <li>Item #3</li>
    </ul>

If you are using a database or other backend to fetch data, `pyy` supports
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
    <html xmlns="http://www.w3.org/1999/xhtml">
      <body>
        <div id='header'></div>
        <div id='content'></div>
        <div id='footer'></div>
      </body>
    </html>

For clean code, the `.add()` method returns children in tuples. The above
example can be cleaned up and expanded like this:
    >>> _html = html()
    >>> _head, _body = _html.add(head(title('Simple Document Tree')), body())
    >>> names = ['header', 'content', 'footer']
    >>> header, content, footer = _body.add(div(id=name) for name in names)
    >>> print _html
    <html xmlns="http://www.w3.org/1999/xhtml">
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
    <div id='header'></div>

Comments can be created using objects too!
    >>> print comment("BEGIN HEADER")
    <!--BEGIN HEADER-->
    >>> print comment(p("Stop using IE5!"), condition='lt IE6')
    <!--[if lt IE6]><p>Stop using IE5!</p><![endif]-->

More usage examples to come. Check out the files in the `examples` folder too.


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
