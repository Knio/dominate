Dominate
========

`Dominate` is a Python library for creating and manipulating HTML documents using an elegant DOM API.
It allows you to write HTML pages in pure Python very concisely, which eliminates the need to learn another template language, and lets you take advantage of the more powerful features of Python.

![Python version](https://img.shields.io/pypi/pyversions/dominate.svg?style=flat)
[![Build status](https://img.shields.io/travis/Knio/dominate/master.svg?style=flat)](https://travis-ci.org/Knio/dominate)
[![Coverage status](https://img.shields.io/coveralls/github/Knio/dominate/master.svg?style=flat)](https://coveralls.io/r/Knio/dominate?branch=master)

Python:

```python
import dominate
from dominate.tags import *

doc = dominate.document(title='Dominate your HTML')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='header').add(ol()):
        for i in ['home', 'about', 'contact']:
            li(a(i.title(), href='/%s.html' % i))

    with div():
        attr(cls='body')
        p('Lorem ipsum..')

print(doc)
```

Output:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Dominate your HTML</title>
    <link href="style.css" rel="stylesheet">
    <script src="script.js" type="text/javascript"></script>
  </head>
  <body>
    <div id="header">
      <ol>
        <li>
          <a href="/home.html">Home</a>
        </li>
        <li>
          <a href="/about.html">About</a>
        </li>
        <li>
          <a href="/contact.html">Contact</a>
        </li>
      </ol>
    </div>
    <div class="body">
      <p>Lorem ipsum..</p>
    </div>
  </body>
</html>
```


Installation
------------

The recommended way to install `dominate` is with
[`pip`](http://pypi.python.org/pypi/pip/):

    pip install dominate

[![PyPI version](https://img.shields.io/pypi/v/dominate.svg?style=flat)](https://pypi.org/project/dominate/)
[![PyPI downloads](https://img.shields.io/pypi/dm/dominate.svg?style=flat)](https://pypi.org/project/dominate/)



Developed By
------------

* Tom Flanagan - <tom@zkpq.ca>
* Jake Wharton - <jakewharton@gmail.com>
* [Brad Janke](//github.com/bradj)

Git repository located at
[github.com/Knio/dominate](//github.com/Knio/dominate)


Examples
========

All examples assume you have imported the appropriate tags or entire tag set:

```python
from dominate.tags import *
```


Hello, World!
-------------

The most basic feature of `dominate` exposes a class for each HTML element, where the constructor
accepts child elements, text, or keyword attributes. `dominate` nodes return their HTML representation
from the `__str__`, `__unicode__`, and `render()` methods.

```python
print(html(body(h1('Hello, World!'))))
```
```html
<html>
    <body>
        <h1>Hello, World!</h1>
    </body>
</html>
```

Attributes
----------

`Dominate` can also use keyword arguments to append attributes onto your tags. Most of the attributes are a direct copy from the HTML spec with a few variations.

For attributes `class` and `for` which conflict with Python's [reserved keywords](http://docs.python.org/2/reference/lexical_analysis.html#keywords "Reserved Keywords"), you can use the following aliases:

| class | for |
|-------|-----|
|_class | _for |
|cls | fr |
|className|htmlFor|
|class_name|html_for|


```python
test = label(cls='classname anothername', fr='someinput')
print(test)
```
```html
<label class="classname anothername" for="someinput"></label>
```

Use `data_*` for [custom HTML5 data attributes](http://www.w3.org/html/wg/drafts/html/master/dom.html#embedding-custom-non-visible-data-with-the-data-*-attributes "HTML5 Data Attributes").

```python
test = div(data_employee='101011')
print(test)
```
```html
<div data-employee="101011"></div>
```

You can also modify the attributes of tags through a dictionary-like interface:

```python
header = div()
header['id'] = 'header'
print(header)
```
```html
<div id="header"></div>
```

Complex Structures
------------------

Through the use of the `+=` operator and the `.add()` method you can easily create more advanced structures.

Create a simple list:

```python
list = ul()
for item in range(4):
    list += li('Item #', item)
print(list)
```
```html
<ul>
    <li>Item #0</li>
    <li>Item #1</li>
    <li>Item #2</li>
    <li>Item #3</li>
</ul>
```

`dominate` supports iterables to help streamline your code:

```python
print(ul(li(a(name, href=link), __pretty=False) for name, link in menu_items))
```
```html
<ul>
    <li><a href="/home/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li><a href="/downloads/">Downloads</a></li>
    <li><a href="/links/">Links</a></li>
</ul>
```

A simple document tree:

```python
_html = html()
_body = _html.add(body())
header  = _body.add(div(id='header'))
content = _body.add(div(id='content'))
footer  = _body.add(div(id='footer'))
print(_html)
```
```html
<html>
    <body>
        <div id="header"></div>
        <div id="content"></div>
        <div id="footer"></div>
    </body>
</html>
```

For clean code, the `.add()` method returns children in tuples. The above example can be cleaned up and expanded like this:

```python
_html = html()
_head, _body = _html.add(head(title('Simple Document Tree')), body())
names = ['header', 'content', 'footer']
header, content, footer = _body.add([div(id=name) for name in names])
print(_html)
```
```html
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
```

You can modify the attributes of tags through a dictionary-like interface:

```python
header = div()
header['id'] = 'header'
print(header)
```
```html
<div id="header"></div>
```

Or the children of a tag though an array-line interface:

```python
header = div('Test')
header[0] = 'Hello World'
print(header)
```
```html
<div>Hello World</div>
```

Comments can be created using objects too!

```python
print(comment('BEGIN HEADER'))
```
```html
<!--BEGIN HEADER-->
```

```python
print(comment(p('Upgrade to newer IE!'), condition='lt IE9'))
```
```html
<!--[if lt IE9]>
  <p>Upgrade to newer IE!</p>
<![endif]-->
```

Rendering
---------

By default, `render()` tries to make all output human readable, with one HTML
element per line and two spaces of indentation.

This behavior can be controlled by the `__pretty` (default: `True` except for
certain element types like `pre`) attribute when creating an element, and by
the `pretty` (default: `True`), `indent` (default: `  `) and `xhtml` (default: `False`)
 arguments to `render()`. Rendering options propagate to all descendant nodes.

```python
a = div(span('Hello World'))
print(a.render())
```
```html
<div>
  <span>Hello World</span>
</div>
```
```python
print(a.render(pretty=False))
```
```html
<div><span>Hello World</span></div>
```
```python
print(a.render(indent='\t'))
```
```html
<div>
	<span>Hello World</span>
</div>
```
```python
a = div(span('Hello World'), __pretty=False)
print(a.render())
```
```html
<div><span>Hello World</span></div>
```
```python
d = div()
with d:
    hr()
    p("Test")
    br()
print(d.render())
print(d.render(xhtml=True))
```
```html
<div>
  <hr>
  <p>Test</p><br>
</div>
<div>
  <hr />
  <p>Test</p><br />
</div>
```


Context Managers
----------------

You can also add child elements using Python's `with` statement:

```python
h = ul()
with h:
    li('One')
    li('Two')
    li('Three')

print(h)
```
```html
<ul>
    <li>One</li>
    <li>Two</li>
    <li>Three</li>
</ul>
```


You can use this along with the other mechanisms of adding children elements, including nesting `with` statements, and it works as expected:

```python
h = html()
with h.add(body()).add(div(id='content')):
    h1('Hello World!')
    p('Lorem ipsum ...')
    with table().add(tbody()):
        l = tr()
        l += td('One')
        l.add(td('Two'))
        with l:
            td('Three')

print(h)
```
```html
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
```

When the context is closed, any nodes that were not already added to something get added to the current context.

Attributes can be added to the current context with the `attr` function:

```python
d = div()
with d:
    attr(id='header')

 print(d)
 ```
 ```html
<div id="header"></div>
```

And text nodes can be added with the `dominate.util.text` function:

```python
from dominate.util import text
para = p(__pretty=False)
with para:
    text('Have a look at our ')
    a('other products', href='/products')

print(para)
```
```html
<p>Have a look at our <a href="/products">other products</a></p>
```


Decorators
----------

`Dominate` is great for creating reusable widgets for parts of your page. Consider this example:

```python
def greeting(name):
    with div() as d:
        p('Hello, %s' % name)
    return d

print(greeting('Bob'))
```
```html
<div>
    <p>Hello, Bob</p>
</div>
```

You can see the following pattern being repeated here:

```python
def widget(parameters):
    with tag() as t:
        ...
    return t
```

This boilerplate can be avoided by using tags (objects and instances) as decorators

```python
@div
def greeting(name):
    p('Hello %s' % name)
print(greeting('Bob'))
```
```html
<div>
    <p>Hello Bob</p>
</div>
```

The decorated function will return a new instance of the tag used to decorate it, and execute in a `with` context which will collect all the nodes created inside it.

You can also use instances of tags as decorators, if you need to add attributes or other data to the root node of the widget.
Each call to the decorated function will return a copy of the node used to decorate it.

```python
@div(h2('Welcome'), cls='greeting')
def greeting(name):
    p('Hello %s' % name)

print(greeting('Bob'))
```
```html

<div class="greeting">
    <h2>Welcome</h2>
    <p>Hello Bob</p>
</div>
```

Creating Documents
------------------

Since creating the common structure of an HTML document everytime would be excessively tedious dominate provides a class to create and manage them for you: `document`.

When you create a new document, the basic HTML tag structure is created for you.

```python
d = document()
print(d)
```
```html
<!DOCTYPE html>
<html>
    <head>
       <title>Dominate</title>
    </head>
    <body></body>
</html>
```

The `document` class accepts `title`, `doctype`, and `request` keyword arguments.
The default values for these arguments are `Dominate`, `<!DOCTYPE html>`, and `None` respectively.

The `document` class also provides helpers to allow you to access the `title`, `head`, and `body` nodes directly.

```python
d = document()
```

```python
>>> d.head
<dominate.tags.head: 0 attributes, 1 children>
>>> d.body
<dominate.tags.body: 0 attributes, 0 children>
>>> d.title
u'Dominate'
```


The `document` class also provides helpers to allow you to directly add nodes to the `body` tag.

```python
d = document()
d += h1('Hello, World!')
d += p('This is a paragraph.')
print(d)
```
```html
<!DOCTYPE html>
<html>
    <head>
       <title>Dominate</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a paragraph.</p>
    </body>
</html>
```

Embedding HTML
--------------

If you need to embed a node of pre-formed HTML coming from a library such as markdown or the like, you can avoid escaped HTML by using the raw method from the dominate.util package:

```
from dominate.util import raw
...
td(raw('<a href="example.html">Example</a>'))
```

Without the raw call, this code would render escaped HTML with lt, etc.


SVG
---

The `dominate.svg` module contains SVG tags similar to how `dominate.tags` contains HTML tags. SVG elements will automatically convert `_` to `-` for dashed elements. For example:

```python
from dominate.svg import *
print(circle(stroke_width=5))
```

```html
<circle stroke-width="5"></circle>
```

