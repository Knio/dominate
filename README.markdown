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
    <html xmlns="http://www.w3.org/1999/xhtml">
      <body>
        <h1>Hello, pyy!</h1>
      </body>
    </html>

Complex Structures
------------------
Through the use of the `+=` operator and the `.add()` method you can easily create more advanced structures.

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

More usage examples to come...


Developed By
============
* Tom Flanagan - theknio@gmail.com
* Jake Wharton - jakewharton@gmail.com

http://github.com/JakeWharton/pyy


License
=======
Copyright 2009 Tom Flanagan, Jake Wharton

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.