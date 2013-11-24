from dominate.tags import *

def test_arguments():
  assert html(body(h1('Hello, pyy!'))).render() == \
'''<html>
  <body>
    <h1>Hello, pyy!</h1>
  </body>
</html>'''


def test_kwargs():
  assert div(id=4, checked=True, cls="mydiv", data_name='foo', onclick='alert(1);').render() == \
'''<div checked="checked" class="mydiv" data-name="foo" id="4" onclick="alert(1);"></div>'''

def test_iadd():
  list = ul()
  for item in range(4):
    list += li('Item #', item)

  # 2 children so doesn't render inline
  assert list.render() == \
'''<ul>
  <li>Item #0
  </li>
  <li>Item #1
  </li>
  <li>Item #2
  </li>
  <li>Item #3
  </li>
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

