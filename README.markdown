About
=====
`pyy` is a python library for creating XHTML pages through the use of objects.
This allows you to tightly integrate your XHTML generation with your backend
without the need of using an intermediate templating language.

`pyy` also provides you with two helper classes: `htmlparser` and `htmlpage`.

`htmlpage` allows for the creation of all aspects needed to respond to an
HTTP request. Your XHTML tree you created can be packaged with a DOCTYPE, XML
declaration, and any cookies you wish to send. When rendered, this class will
automatically format all of the contained information.

`htmlparser` will take valid and mostly-valid XHTML input and return a pyy
object tree.

Usage
=====
All these examples assume you have executed `from html import *` previously.

Hello, pyy!
-----------
Constructing a "Hello, World!" style example is as easy as this:
    >>> print html(body(h1("Hello, pyy!")))
    &lt;html xmlns="http://www.w3.org/1999/xhtml">
      &lt;body>
        &lt;h1>Hello, pyy!&lt;/h1>
      &lt;/body>
    &lt;/html>

Complex Structures
------------------
Through the use of the `+=` operator and the `.add()` method you can easily create more advanced structures.

Create a simple list:
    >>> list = ul()
    >>> for item in range(4):
    >>>   list += li("Item #", item)
    >>> print list
    &lt;ul>
      &lt;li>Item #0&lt;/li>
      &lt;li>Item #1&lt;/li>
      &lt;li>Item #2&lt;/li>
      &lt;li>Item #3&lt;/li>
    &lt;/ul>

A simple document tree:
    >>> _html = html()
    >>> _body = _html.add(body())
    >>> header  = _body.add(div(id='header'))
    >>> content = _body.add(div(id='content'))
    >>> footer  = _body.add(div(id='footer'))
    >>> print _html
    &lt;html xmlns="http://www.w3.org/1999/xhtml">
      &lt;body>
        &lt;div id='header'>&lt;/div>
        &lt;div id='content'>&lt;/div>
        &lt;div id='footer'>&lt;/div>
      &lt;/body>
    &lt;/html>

You can modify the attributes of tags through a dictionary-like interface:
    >>> header = div()
    >>> header['id'] = 'header'
    >>> print header
    &lt;div id='header'>&lt;/div>

Comments can be created using objects too!
    >>> print comment("BEGIN HEADER")
    &lt;!--BEGIN HEADER-->
    >>> print comment(p("Stop using IE5!"), condition='lt IE6')
    &lt;!--[if lt IE6]>&lt;p>Stop using IE5!&lt;/p>&lt;![endif]-->

More usage examples to come...

Developed By
============
* Tom Flanagan <theknio@gmail.com>
* Jake Wharton <jakewharton@gmail.com>

http://github.com/JakeWharton/pyy