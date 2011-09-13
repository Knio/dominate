'''
About
=====
`pyy.html` allows for creating (X)HTML markup through the use of objects.
This allows you to tightly integrate (X)HTML generation into your backend
without the need of using an intermediate templating language.

`pyy.html` also provides you with helper classes for generating and parsing
(X)HTML documents.


Usage
=====
All these examples assume you have imported the appropriate tags or entire tag
set (i.e. `from pyy.html.html import *`).

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

If you are using a database or other backend to fetch data, `pyy.html` supports
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
Since creating the common structure of an HTML document everytime would be
excessively tedious pyy.html provides a class to create an manage them for
you, `document`.

When you create a new document, the basic HTML tag structure is created for
you.
    >>> d = document()
    >>> print d
    <html>
      <head>
        <title>PYY Page</title>
      </head>
      <body></body>
    </html>

The `document` class also provides helpers to allow you to access the `html`,
`head`, and `body` elements directly.
    >>> d = document()
    >>> d.html
    <pyy.html.html.html: 0 attributes, 2 children>
    >>> d.head
    <pyy.html.html.head: 0 attributes, 0 children>
    >>> d.body
    <pyy.html.html.body: 0 attributes, 0 children>

You should notice that here the `head` tag contains zero children. This is
because the default `title` tag is only added when the document is rendered
and the `head` element already does not explicitly contain one.

The `document` class also provides helpers to allow you to directly add
elements to the `body` tag.
    >>> d = document()
    >>> d += h1('Hello, World!')
    >>> p += p('This is a paragraph.')
    >>> print d
    <html>
      <head>
        <title>PYY Page</title>
      </head>
      <body>
        <h1>Hello, World!</h1>
        <p>This is a paragraph.</p>
      </body>
    </html>

Markup Validation
-----------------
You can also set the DOCTYPE of the `document` which will validate the tag tree
when it is rendered.
    >>> d = document()
    >>> d.doctype = dtd.xhtml11
    >>> print d
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
      <head>
        <title>PYY Page</title>
      </head>
      <body></body>
    </html>

Notice how the required XHTML 1.1 attribute `xmlns` is automatically added to
the `<html>` tag.

If there are any errors in the tag tree a `ValueError` will be thrown which
describes the offending tag. You can check the validity of your document at
any time by calling `validate()` explicity.

You may also set a `document`'s DOCTYPE with the keyword argument `doctype`.
    >>> d = document(doctype=dtd.html5)
However, doing so will cause the entire document to be validated with every
added tag. For production environments it is best to set the DOCTYPE after the
entire tag tree has been created so it all is only validated once.

Parsing Documents
-----------------
The `parser` class contains two methods: `parse` and `pageparse`. `parse` will
take valid and mostly-valid (X)HTML input and return a tag tree. `pageparse`
will take an entire document and return a `document` instance complete with
the DOCTYPE (if present) and a tag tree using the (X)HTML version specified
by the DOCTYPE.

`parse` will simply return a heirarchy of all the tags and their content that
it can recognize in a string.
    >>> parse('<p>Hello.</p>')
    <pyy.html.html.p: 0 attributes, 1 child>
    >>> parse('<html><head><title>test</title></head><body><h1>Hi.</h1></body></html>')
    <pyy.html.html.html: 0 attributes, 2 children>
    >>> parse('<div id="first"></div><div id="second"></div>')
    [<pyy.html.html.div: 1 attribute, 0 children>, <pyy.html.html.div: 1 attribute, 0 children>]

Notice that if multiple top-level tags exist in the string `parse` will return
them as an array.

`pageparse` also takes a string of tags and optionally a DOCTYPE and returns a
`document` object.
    >>> pageparse('<!DOCTYPE html><html><head><title>Test</title></head><body></body></html>')
    <pyy.html.document.document html5 "Test">


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

from document import document
