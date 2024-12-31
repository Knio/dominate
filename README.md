Dominate
========

`Dominate` is a Python library for creating and manipulating HTML documents using an elegant DOM API.
It allows you to write HTML pages in pure Python very concisely, which eliminates the need to learn another template language, and lets you take advantage of the more powerful features of Python.

![Python version](https://img.shields.io/pypi/pyversions/dominate.svg?style=flat)
[![Build status](https://github.com/Knio/dominate/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/Knio/dominate/actions/workflows/ci.yml?query=branch%3Amaster+)
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
* [Nikalexis Nikos](//github.com/nikalexis)

Git repository located at
[github.com/Knio/dominate](//github.com/Knio/dominate)

Current fork (with directives feature and more) located at
[github.com/nikalexis/dominate](//github.com/nikalexis/dominate)

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
|klass|phor|


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

When you don't want to auto-include a specific element you can use the `.orphan()` command on an element.

```python
from dominate.tags import p, span
from dominate.util import text

with p() as para:
    text('This text will be included only.')
    one_orphaned_span = span('This span will not be included in the parent paragraph.').orphan()
    # you can use `one_orphaned_span` variable below but it will not be added in the dom
    # except you decide to include it by using e.g. `any_elememt.add(one_orphaned_span)`

print(para)
```
Paragraph contents:
```html
<p>This text will be included only.</p>
```

You can also use the `orphan` context manager. All tags inside that context will not be included anywhere in the dom tree.

```python
from dominate.tags import p, span
from dominate.util import text, orphan

with p() as para:
    text('This text will be included only.')
    with orphan() as my_orphans:
        one_orphaned_span = span('This span will not be included in the parent paragraph.')
        # you can use `one_orphaned_span` variable below but it will not be added in the dom
        # except you decide to include it by using e.g. `any_elememt.add(one_orphaned_span)`
        with span() as second_orphaned_span:
            text('Neither this text will be included in the paragraph.')
        # you can use `second_orphaned_span` variable below but it will not be added in the dom
        # except you decide to include it by using e.g. `any_elememt.add(second_orphaned_span)`

print('Paragraph contents:')
print(para)
print('My orphans:')
print(my_orphans)

# Orphans acts as `container`s, but they are not included anywhere
# except you decide to include them by using e.g. `any_elememt.add(my_orphans)`

```
Paragraph contents:
```html
<p>This text will be included only.</p>
```
Orphans contents:
```html
<span>This span will not be included in the parent paragraph.</span>
<span>Neither this text will be included in the paragraph.</span>
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

Modifiers
---------

Another useful utility is the `util.modifier` decorator object.
You can decorate any function of your code that applies changes on another dom object.
To apply the modifier you can use `&` operator or `.add()` it as an item or just calling the function withing a context manager.

```python
from dominate.util import modifier

@modifier
def add_ids_in_children(prefix):
    for i, child in enumerate(this().children):
        child['id'] = f'{prefix}-{i}'

@div()
def two_paragraphs():
    p('First paragraph')
    p('Second paragraph')

# You can also chain operators, like `dom_object & modifier_one() & modifier_two()`
two_paragraphs_with_ids = two_paragraphs() & add_ids_in_children(prefix='paragraph')
print(two_paragraphs_with_ids)
```
```html
<div>
  <p id="paragraph-0">First paragraph</p>
  <p id="paragraph-1">Second paragraph</p>
</div>
```

They also work by adding them as items.

```python
# be careful about the order, modifier are applied in the order specified in the *args list.

three_paragraphs = div(
    p('First paragraph'),
    p('Second paragraph'),
    add_ids_in_children(prefix='paragraph-a'),
    p('Third paragraph without id'),
)

four_paragraphs = div(
    p('First paragraph'),
    p('Second paragraph'),
    p('Third paragraph'),
)
four_paragraphs.add(
    add_ids_in_children(prefix='paragraph-b'), # adding ids on every child present
    p('Forth paragraph without id'), # adding another child after the modifier
) 

print(three_paragraphs)
print(four_paragraphs)
```

```html
<div>
  <p id="paragraph-a-0">First paragraph</p>
  <p id="paragraph-a-1">Second paragraph</p>
  <p>Third paragraph without id</p>
</div>

<div>
  <p id="paragraph-b-0">First paragraph</p>
  <p id="paragraph-b-1">Second paragraph</p>
  <p id="paragraph-b-2">Third paragraph</p>
  <p>Forth paragraph without id</p>
</div>
```

They also work in context managers.

```python
with two_paragraphs() as tp:
    # will apply when `with` __exit__
    add_ids_in_children(prefix='paragraph')

    # won't apply until explicitly call to_be_added.apply()
    to_be_added = add_ids_in_children(prefix='paragraph').orphan()

    # will apply immediately
    add_ids_in_children(prefix='paragraph').apply()
```

There is also a function `util.apply` that can be useful inside context managers, to mass deploy modifiers (with immidiate apply).

```python
from dominate.util import apply

with div():
    apply(
        modifier_one(),
        modifier_two(),
        modifier_three(),
    )
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

If you need to embed a node of pre-formed HTML coming from a library such as markdown or the like you can avoid escaped HTML by using the raw method from the dominate.util package:

```
from dominate.util import raw
...
td(raw('<a href="example.html">Example</a>'))
```

Without the raw call, this code would render escaped HTML with lt, etc. The behavior of the previous block of code is the same as `td_element.innerHTML="<a href="example.html">Example</a>"` in JavaScript.


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

Using directives
----------------

Directives act as helpers to build a specific attribute of a DOM tag.

Currently the following directives are available:

* HTML tag attributes
  * `class`
  * `style`
  * `data`
  * `aria`
* Javascript magic libraries
  * [Alpine.js](https://alpinejs.dev/start-here)
  * [HTMX](https://htmx.org/docs/)
  * [_Hyperscript](https://hyperscript.org/docs/)

### HTML `class` attribute examples

```python
from dominate.all import *

with div('mx-3') as my_div:

    # this() is a special function alias to get_current()
    # returning always the object declared in the closest `with` clause above
    
    # Add / remove / reset class(es) attribute
    my_div.klass += 'my-5' # add
    my_div.klass('row') # reset
    this().klass = 'row' # reset
    this().klass.add('align-items-start') # add
    this().klass.replace('align-items-start', 'align-items-end') # replace
    this().klass.exists('align-items-end') # returns True
    this().klass += 'another-class' # add
    this().klass += ('one', 'two', 'three', 'four') # add
    this().klass -= 'another-class' # remove
    # you can use .class_
    this().class_.remove('one', 'two') # remove
    # you can use .cls
    this().cls -= ('three', 'four') # remove
```

### HTML `style` attribute examples

```python
from dominate.all import *

with div('mx-3') as my_div:

    # Add / remove / replace / reset style(s) attribute
    # all underscore (_) chars are converted to hyphen (-) chars ONLY when python dict keys are used
    # e.g. below background_color will be converted to background-color
    this().style.add(background_color='pink', font_style='italic') # add or replace existing
    this().style.add(color='white') # add or replace existing
    this().style.add_extra(color='black') # add
    this().style['font-weight'] = ('bold', '!important') # add or replace existing
    this().style += dict(font_weight='normal') # add or replace existing
    this().style -= 'font-weight' # remove
    this().style.reset(font_weight='normal') # reset
    del this().style['font-weight'] # remove
    this().style = dict(background_color='lime') # reset
    # underscore will not be replaced to a hyphen when is passed as a string
    this().style['font_weight'] = 'wrong_css_hyphen' # add or replace existing
    this().style(**{'font_weight': 'normal'}) # add or replace existing

    # css property is using the ccsutils library for advanced methods
    css = this().style.css
    # you can do any kind of magic using this library and then set back the final css
    css.setProperty('font-style', 'italic', 'important')
    this().style.css = css
```

### HTML `data` and `aria` attribute examples

```python
from dominate.all import *

with div('mx-3') as my_div:

    # Set data attribute
    this().data['key-with-hyphen'] = 'value' # sets data-key-with-hyphen="value"
    # dataset is an alias of data
    this().dataset['key-with-hyphen'] = 'value' # sets data-key-with-hyphen="value"
    # Set aria attribute
    this().aria['label'] = 'value' # sets aria-label="value"

    # delete attributes
    del this().data['key-with-hyphen'] # remove
    del this().aria['label'] # remove

    # prepend and append values
    this().data['key'] = 'value' # sets data-key="value"
    this().data['key'].prepend('prefix-') # updates to data-key="prefix-value"
    this().data['key'].append('-suffix') # updates to data-key="prefix-value-suffix"
    this().data['key'] += '-suffixmore' # updates to data-key="prefix-value-suffix-suffixmore"

    # get all data keys declared
    this().data.keys() # returns ['key']
```

### Javascript `Alpine.js` library examples

```python
from dominate.all import *

with div('mx-3') as my_div:

    # Alpine.js directives
    this().x.init = 'console.log("Testing alpine directive");'
    # x directive is an alias to alpine
    # you also use it as a callable
    alpine.init('console.log("Testing alpine directive");')

    with button('Click me to create an alert'):
        # using this(). is optional for x / alpine directive
        x.on['click'] = 'alert("Alert!");'
        # x directive is an alias to alpine
        alpine.on['click'] = 'alert("Alert!");'
    
    # all Alpine.js directives supported:
    x.data = '...'
    x.init = '...'
    x.show = '...'
    x.bind['...'] = '...'
    x.on['...'] = '...'
    x.text = '...'
    x.html = '...'
    x.model = '...'
    x.modelable = '...'
    x.for_ = '...'
    x.transition = '...'
    x.effect = '...'
    x.ignore = '...'
    x.ref = '...'
    x.cloak = '...'
    x.teleport = '...'
    x.if_ = '...'
    x.id = '...'
```

### Javascript `HTMX` library examples

```python
from dominate.all import *

with div('mx-3') as my_div:

    # HTMX directives
    with button('Click me to replace a div using htmx'):
        # set multiple htmx attributes together
        this().hx.get('/replace_div/').trigger('click').target('closest .div').swap('innerHTML')
        # hx directive is an alias to htmx
        this().htmx.get('/replace_div_2/') # reset hx-get attribute
        # using this(). is optional for hx / htmx directive
        hx.swap = 'outerHTML' # reset swap

    # all HTMX directives supported:
    hx.get = '...'
    hx.post = '...'
    hx.on['...'] = '...'
    hx.push_url = '...'
    hx.select = '...'
    hx.select_oob = '...'
    hx.swap = '...'
    hx.swap_oob = '...'
    hx.target = '...'
    hx.trigger = '...'
    hx.vals = '...'

    hx.boost = '...'
    hx.confirm = '...'
    hx.delete = '...'
    hx.disable = '...'
    hx.disabled_elt = '...'
    hx.disinherit = '...'
    hx.encoding = '...'
    hx.ext = '...'
    hx.headers = '...'
    hx.history = '...'
    hx.history_elt = '...'
    hx.include = '...'
    hx.indicator = '...'
    hx.inherit = '...'
    hx.params = '...'
    hx.patch = '...'
    hx.preserve = '...'
    hx.prompt = '...'
    hx.put = '...'
    hx.replace_url = '...'
    hx.request = '...'
    hx.sync = '...'
    hx.validate = '...'
    hx.vars = '...'
```

### Javascript `_Hyperscript` library examples

```python
from dominate.all import *

# Set a _Hyperscript script within a `with` statement
with button():
    this().hyperscript.script = 'on click toggle .red on me'
    # hs directive is an alias to htmx
    this().hs.script = 'on click toggle .red on me'
    # using this(). is optional for hx / htmx directive
    hs.script = 'on click toggle .red on me'

# Set a _Hyperscript script as an element attribute
button(
    hyperscript='on click wait 3s then log "Clicked before 3 seconds!"'
    # hs shortcut also works
    hs='on click wait 3s then log "Clicked before 3 seconds!"'
)

# Please note: Under the surface, a script="..." html attribute will be set.
# Of course, you can set it directly on the element, but you cannot have the
# goodies provided by the directive usage, here is a direct example:

button(
    script='on click wait 3s then log "Clicked before 3 seconds!"'
    # Also, data-script works in the same way
    data_script='on click wait 3s then log "Clicked before 3 seconds!"'
)

```

### Bonus: Inline directives and the `C` helper

All directives and their attributes / functions / modifiers can be used as inline parameters directly on the component function, using a two-dashed (`__`) separator. This way, you can set almost every property during the creation of the dom object, avoding complex code and `with` statements.

```python
from dominate.all import *

button(
    'Click me to create an alert',
    x__on__click='alert("This is another way to create directives inline!");',
    # Also more complicated, using the `C` helper class
    # to pass any *args and/or **kwargs on functions
    klass__add=C('text-center', 'text-danger'), # passed as *args
    style__add=C(font_style='italic'), # passed as *kwargs
)
```

Quick imports
-------------

If you want an easy way to import all available tags, document and directives you can use the following:

```python
from dominate.all import *
```
