pyy.html
========

`pyy.html` allows for creating HTML5 markup through the use of objects.
This allows you to tightly integrate HTML generation into your backend
without the need of using an intermediate templating language.



Usage
=====

All these examples assume you have imported the appropriate tags or entire tag
set (i.e. `from pyy.html.tags import *`).


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
    ...   list += li('Item #', item)
    ...
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

Or the children of a tag though an array-line interface:

    >>> header = div('Test')
    >>> header[0] = 'Hello World'
    >>> print header
    <div>Hello World</div>


Comments can be created using objects too!

    >>> print comment('BEGIN HEADER')
    <!--BEGIN HEADER-->
    >>> print comment(p('Upgrade to newer IE!'), condition='lt IE9')
    <!--[if lt IE9]>
    <p>Upgrade to newer IE!</p>
    <![endif]-->


Context Managers
----------------

You can also add child elements using python's `with` statement:

    >>> h = ul()
    >>> with h:
    ...   li('One')
    ...   li('Two')
    ...   li('Three')
    ...
    >>>
    >>> print h
    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
    </ul>


You can use this along with the other mechanisms of adding children elements,
including nesting `with` statements, and it works as expected:

    >>> h = html()
    >>> with h.add(body()).add(div(id='content')):
    >>>   h1('Hello World!')
    >>>   p('Lorem ipsum ...')
    >>>   with table().add(tbody()):
    ...     l = tr()
    ...     l += td('One')
    ...     l.add(td('Two'))
    ...     with l:
    ...       td('Three')
    ...
    >>>
    >>> print h
    <html>
      <body>
        <div id="content">
          <h1>Hello World!</h1>
          <p>Lorem ipsum ...</p>
          <table>
            <tbody>
              <tr>
                <td>One</td>
                <td>Two</td>
                <td>Three</td>
              </tr>
            </tbody>
          </table>
        </div>
      </body>
    </html>


When the context is closed, any elements that were not already added to
something get added to the current context.

Attributes can be added to the current context with the `attr` function:

    >>> d = div()
    >>> with d:
    ...   attr(id='header')
    ...
    >>>
    >>> print d
    <div id="header"></div>


Creating Documents
------------------

Since creating the common structure of an HTML document everytime would be
excessively tedious pyy.html provides a class to create an manage them for
you, `document`.

When you create a new document, the basic HTML tag structure is created for
you.

    >>> d = document()
    >>> print d
    <!DOCTYPE html>
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
    <pyy.html.tags.html: 0 attributes, 2 children>
    >>> d.head
    <pyy.html.tags.head: 0 attributes, 0 children>
    >>> d.body
    <pyy.html.tags.body: 0 attributes, 0 children>

You should notice that here the `head` tag contains zero children. This is
because the default `title` tag is only added when the document is rendered
and the `head` element already does not explicitly contain one.

The `document` class also provides helpers to allow you to directly add
elements to the `body` tag.

    >>> d = document()
    >>> d += h1('Hello, World!')
    >>> p += p('This is a paragraph.')
    >>> print d
    <!DOCTYPE html>
    <html>
      <head>
        <title>PYY Page</title>
      </head>
      <body>
        <h1>Hello, World!</h1>
        <p>This is a paragraph.</p>
      </body>
    </html>

