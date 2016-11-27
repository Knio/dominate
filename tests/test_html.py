from dominate.tags import *
import pytest

try:
  xrange = xrange
except NameError:
  xrange = range

def test_version():
  import dominate
  version = '2.3.1'
  assert dominate.version == version
  assert dominate.__version__ == version


def test_arguments():
  assert html(body(h1('Hello, pyy!'))).render() == \
'''<html>
  <body>
    <h1>Hello, pyy!</h1>
  </body>
</html>'''


def test_kwargs():
  assert div(
    id=4,
    checked=True,
    cls="mydiv",
    data_name='foo',
    onclick='alert(1);').render() == \
'''<div checked="checked" class="mydiv" data-name="foo" id="4" onclick="alert(1);"></div>'''


def test_repr():
  import re
  d = div()
  assert repr(d).startswith('<dominate.tags.div at ')
  assert repr(d).endswith(' 0 attributes, 0 children>')
  d += [1, {'id':'foo'}]
  assert repr(d).startswith('<dominate.tags.div at ')
  assert repr(d).endswith(' 1 attribute, 1 child>')


def test_add():
  d = div()
  with pytest.raises(ValueError):
    d += None
  d += 1
  d += xrange(2,3)
  d += {'id': 'foo'}
  assert d.render() == '<div id="foo">12</div>'
  assert len(d) == 2
  assert d
  with pytest.raises(IndexError):
    d[2]

  with pytest.raises(TypeError):
    d[None]

  del d[0]
  assert len(d) == 1


def test_iadd():
  list = ul()
  for item in range(4):
    list += li('Item #', item)

  # 2 children so doesn't render inline
  assert list.render() == \
'''<ul>
  <li>Item #0</li>
  <li>Item #1</li>
  <li>Item #2</li>
  <li>Item #3</li>
</ul>'''


# copy rest of examples here


def test_context_manager():
  h = ul()
  with h:
    li('One')
    li('Two')
    li('Three')

  assert h.render() == \
'''<ul>
  <li>One</li>
  <li>Two</li>
  <li>Three</li>
</ul>'''


def test_decorator():
  @div
  def f():
    p('Hello')

  assert f().render() == \
'''<div>
  <p>Hello</p>
</div>'''

  d = div()
  @d
  def f2():
    p('Hello')

  assert f2().render() == \
'''<div>
  <p>Hello</p>
</div>'''

  @div(cls='three')
  def f3():
    p('Hello')
  assert f3().render() == \
'''<div class="three">
  <p>Hello</p>
</div>'''


def test_nested_decorator():
  @div
  def f1():
    p('hello')

  d = div()
  with d:
    f1()

  assert d.render() == \
'''<div>
  <div>
    <p>hello</p>
  </div>
</div>'''

  @div()
  def f2():
    p('hello')

  d = div()
  with d:
    f2()

  assert d.render() == \
'''<div>
  <div>
    <p>hello</p>
  </div>
</div>'''


def test_text():
  from dominate.util import text
  d = div()
  with d:
    text('Hello World')

  assert d.render() == \
    '''<div>Hello World</div>'''

  assert div(text('<>', escape=False)).render() == \
    '''<div><></div>'''

  assert div(text('<>')).render() == \
    '''<div>&lt;&gt;</div>'''


def test_raw():
  from dominate.util import raw
  d = div()
  with d:
    raw('Hello World<br>')

  assert d.render() == '''<div>Hello World<br></div>'''


def test_escape():
  assert pre('<>').render() == '''\
<pre>&lt;&gt;</pre>'''


def test_attributes():
  d = div()
  d['id'] = 'foo'
  assert d['id'] == 'foo'
  del d['id']
  with pytest.raises(KeyError):
    del d['id']
  with pytest.raises(AttributeError):
    x = d['id']
  with d:
    attr(data_test=False)
  assert d['data-test'] == 'false'

  with pytest.raises(ValueError):
    attr(id='moo')


def test_lazy():
  from dominate import util
  executed = [False]
  def _lazy():
    executed[0] = True
    return span('Hi')

  d = div()
  s = util.lazy(_lazy)
  d += s

  assert executed[0] == False
  assert d.render() == '<div>\n  <span>Hi</span>\n</div>'
  assert executed[0] == True


def test_keyword_attributes():
  expected = '<div class="foo" for="bar"></div>'
  assert div(cls='foo', fr='bar').render() == expected
  assert div(_class='foo', _for='bar').render() == expected
  assert div(className='foo', htmlFor='bar').render() == expected
  assert div(class_name='foo', html_for='bar').render() == expected


def test_comment():
  d = comment('Hi there')
  assert d.render() == '<!--Hi there-->'
  assert div(d).render() == '<div>\n  <!--Hi there-->\n</div>'


def test_nested_decorator_2():
  @span
  def foo():
    @div(cls='bar')
    def bar(x):
      p(x)
    bar('a')
    bar('b')

  assert foo().render() == '''<span>
  <div class="bar">
    <p>a</p>
  </div>
  <div class="bar">
    <p>b</p>
  </div>
</span>'''


def test_pretty():
  assert head(script('foo'), style('bar')).render() == '''<head>
  <script>foo</script>
  <style>bar</style>
</head>'''

  assert div(pre('test')).render() == '''<div>
  <pre>test</pre>
</div>'''

  assert div(pre('test')).render(indent='\t') == '''<div>
\t<pre>test</pre>
</div>'''

  assert div(pre('test')).render(pretty=False) == \
      '''<div><pre>test</pre></div>'''

  assert div(span('hi'), span('there'), __pretty=False).render() == \
    '''<div><span>hi</span><span>there</span></div>'''

  assert span('hi', br(), 'there').render() == \
      '''<span>hi<br>there</span>'''

  assert span('hi', br(__inline=False), 'there').render() == \
      '''<span>hi\n  <br>there\n</span>'''


def test_xhtml():
  assert head(script('foo'), style('bar')).render(xhtml=True) == '''<head>
  <script>foo</script>
  <style>bar</style>
</head>'''

  assert span('hi', br(), 'there').render(xhtml=True) == \
         '''<span>hi<br />there</span>'''

  assert span('hi', br(), 'there').render() == \
         '''<span>hi<br>there</span>'''

  assert span('hi', br(), 'there').render(xhtml=False) == \
         '''<span>hi<br>there</span>'''

