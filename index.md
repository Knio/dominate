---
title: Dominate — Python HTML Generation Library
layout: default
---

# Dominate

**Python HTML Generation Library** · v2.9.1

> Write HTML pages in pure Python using an elegant DOM API — no template language needed.

[![Build](https://github.com/Knio/dominate/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/Knio/dominate/actions/workflows/ci.yml)
[![Coverage](https://img.shields.io/coveralls/github/Knio/dominate/master.svg?style=flat)](https://coveralls.io/r/Knio/dominate?branch=master)
[![PyPI](https://img.shields.io/pypi/v/dominate.svg?style=flat)](https://pypi.org/project/dominate/)
[![Python](https://img.shields.io/pypi/pyversions/dominate.svg?style=flat)](https://pypi.org/project/dominate/)

```
pip install dominate
```

---

## Contents

- [Getting Started](#getting-started)
- [Attributes](#attributes)
- [Building Structure](#building-structure)
- [Rendering](#rendering)
- [Context Managers](#context-managers)
- [Decorators](#decorators)
- [Creating Documents](#creating-documents)
- [Embedding HTML](#embedding-html)
- [SVG Support](#svg-support)
- [API — dom_tag](#api--dom_tag)
- [API — document](#api--document)
- [API — dominate.util](#api--dominateutil)
- [API — tags & svg](#api--tags--svg)

---

## Getting Started

`dominate` exposes a class for each HTML element. The constructor accepts child elements, text, or keyword attributes. Nodes return their HTML from `__str__`, `__unicode__`, and `render()`.

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

**Output:**

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
        <li><a href="/home.html">Home</a></li>
        <li><a href="/about.html">About</a></li>
        <li><a href="/contact.html">Contact</a></li>
      </ol>
    </div>
    <div class="body">
      <p>Lorem ipsum..</p>
    </div>
  </body>
</html>
```

The simplest possible example:

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

---

## Attributes

`dominate` uses keyword arguments to append attributes. Most match the HTML spec directly.

For `class` and `for`, which conflict with Python reserved keywords, use any of these aliases:

| `class` aliases | `for` aliases |
|---|---|
| `_class` | `_for` |
| `cls` | `fr` |
| `className` | `htmlFor` |
| `class_name` | `html_for` |

```python
test = label(cls='classname anothername', fr='someinput')
print(test)
```

```html
<label class="classname anothername" for="someinput"></label>
```

Use `data_*` for custom HTML5 data attributes:

```python
test = div(data_employee='101011')
print(test)
```

```html
<div data-employee="101011"></div>
```

Modify attributes through a dictionary-like interface:

```python
header = div()
header['id'] = 'header'
print(header)
```

```html
<div id="header"></div>
```

---

## Building Structure

Use `+=` and `.add()` to compose complex trees.

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

`dominate` supports iterables:

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

`.add()` returns children in tuples for clean multi-assignment:

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

Comments are supported too:

```python
print(comment('BEGIN HEADER'))
# <!--BEGIN HEADER-->

print(comment(p('Upgrade to newer IE!'), condition='lt IE9'))
```

```html
<!--[if lt IE9]>
  <p>Upgrade to newer IE!</p>
<![endif]-->
```

---

## Rendering

By default, `render()` produces human-readable output — one element per line, two-space indent.

```python
a = div(span('Hello World'))
print(a.render())
```

```html
<div>
  <span>Hello World</span>
</div>
```

Control formatting with `pretty`, `indent`, and `xhtml` arguments:

```python
print(a.render(pretty=False))
# <div><span>Hello World</span></div>

print(a.render(indent='\t'))
# <div>
# 	<span>Hello World</span>
# </div>
```

XHTML self-closing tags:

```python
d = div()
with d:
    hr()
    p("Test")
    br()

print(d.render())         # HTML mode
print(d.render(xhtml=True))  # XHTML mode
```

```html
<!-- HTML -->
<div>
  <hr>
  <p>Test</p><br>
</div>

<!-- XHTML -->
<div>
  <hr />
  <p>Test</p><br />
</div>
```

> **Tip:** Rendering options propagate to all descendant nodes. Setting `pretty=False` on a parent suppresses formatting for the entire subtree.

---

## Context Managers

Use Python's `with` statement to add children to a tag:

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

Nest `with` blocks and combine with other child-adding patterns freely:

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

Set attributes on the current context with `attr()`:

```python
d = div()
with d:
    attr(id='header')
print(d)
# <div id="header"></div>
```

Add mixed text and tag content using `dominate.util.text`:

```python
from dominate.util import text

para = p(__pretty=False)
with para:
    text('Have a look at our ')
    a('other products', href='/products')

print(para)
# <p>Have a look at our <a href="/products">other products</a></p>
```

---

## Decorators

Use tag classes or instances as decorators to eliminate boilerplate widget code.

**Without decorator:**

```python
def greeting(name):
    with div() as d:
        p('Hello, %s' % name)
    return d
```

**With decorator:**

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

Use a tag **instance** as a decorator to add attributes or preset children. Each call returns a fresh copy:

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

---

## Creating Documents

The `document` class manages the full HTML boilerplate automatically.

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

| Parameter | Type | Default | Description |
|---|---|---|---|
| `title` | `str` | `'Dominate'` | Sets the `<title>` element in `<head>` |
| `doctype` | `str` | `'<!DOCTYPE html>'` | Doctype declaration prepended to output |
| `request` | `object` | `None` | Optional request object for context |

> **Tip:** Nodes added directly to a `document` via `+=` or `with doc:` are appended to `<body>`. Access `doc.head`, `doc.body`, and `doc.title` as properties.

---

## Embedding HTML

Use `raw()` to inject pre-formed HTML strings without escaping:

```python
from dominate.util import raw

td(raw('<a href="example.html">Example</a>'))
```

Without `raw()`, the string would render as escaped HTML entities. This behaves identically to `td_element.innerHTML = "..."` in JavaScript.

> **Warning:** Only use `raw()` with trusted input. Passing untrusted user content will expose you to XSS vulnerabilities.

---

## SVG Support

The `dominate.svg` module mirrors `dominate.tags` for SVG elements. Attribute underscores are automatically converted to dashes:

```python
from dominate.svg import *

print(circle(stroke_width=5))
```

```html
<circle stroke-width="5"></circle>
```

---

## API — dom_tag

Base class for all HTML and SVG elements. Every tag class inherits from `dom_tag`.

| Method / Attribute | Signature | Returns | Description |
|---|---|---|---|
| `__init__` | `(*args, **kwargs)` | `dom_tag` | Children as positional args; attributes as keyword args |
| `render` | `(pretty=True, indent='  ', xhtml=False)` | `str` | Render the node and all descendants to an HTML string |
| `add` | `(*args)` | `dom_tag \| tuple` | Add children. Returns single child or tuple when multiple passed |
| `__iadd__` | `(other)` | `dom_tag` | Append a child via `+=` operator |
| `__getitem__` | `(key: str)` | `str` | Get attribute value by name |
| `__setitem__` | `(key: str, value: str)` | `None` | Set attribute by name |
| `__enter__ / __exit__` | `()` | `dom_tag` | Context manager support for `with` statement |
| `__str__` | `()` | `str` | Equivalent to `render()` with defaults |

---

## API — document

Subclass of `html` that manages a complete HTML document structure.

| Member | Type | Description |
|---|---|---|
| `document(title, doctype, request)` | constructor | Create document. Keyword args set title, doctype declaration, and optional request. |
| `.head` | `head` (dom_tag) | The `<head>` element — use as context manager to add stylesheets, scripts, meta tags |
| `.body` | `body` (dom_tag) | The `<body>` element — nodes added to the document directly are appended here |
| `.title` | `str` | Get or set the document title string |

---

## API — dominate.util

Utility classes for text nodes, raw HTML injection, and context attribute setting.

| Name | Signature | Description |
|---|---|---|
| `text` | `(content: str, escape: bool = True)` | A plain text node. Use inside `with` blocks for mixed text+tag content. Set `escape=False` for pre-escaped content. |
| `raw` | `(content: str)` | Inject a raw, unescaped HTML string. Equivalent to `text(content, escape=False)`. Use only with trusted input. |
| `attr` | `(**kwargs)` | Set attributes on the currently active context node (the innermost `with` block target). |

---

## API — tags & svg

Every standard HTML5 and SVG element is available as a Python class.

Import all HTML tags with `from dominate.tags import *` or import individually. All tags inherit from `dom_tag` and share the same constructor signature.

| Module | Examples | Notes |
|---|---|---|
| `dominate.tags` | `div, span, p, a, ul, li, ol, table, tr, td, th, form, input_, button, h1…h6, img, script, link, meta, head, body, html, br, hr, pre, code, em, strong, label, select, option, textarea` … | All standard HTML5 elements. Note: `input` is `input_` to avoid Python keyword conflict. |
| `dominate.svg` | `svg, circle, rect, path, line, polyline, polygon, ellipse, g, text, tspan, defs, use, symbol` … | Attribute underscores auto-converted to dashes (e.g. `stroke_width` → `stroke-width`) |

> **Note:** `from dominate.tags import *` imports all ~110 HTML element classes into the current namespace. For larger projects, consider importing only what you need to avoid namespace pollution.

---

*Dominate is maintained by [Knio](https://github.com/Knio/dominate) · Licensed under LGPL-3.0*
