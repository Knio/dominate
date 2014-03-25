from dominate import document
from dominate.tags import *

def test_doc():
  d = document()
  assert d.render() == \
'''<!DOCTYPE html>
<html>
  <head>
    <title>Dominate</title>
  </head>
  <body></body>
</html>'''


def test_decorator():
  @document()
  def foo():
    p('Hello World')

  f = foo()
  assert f.render() == \
'''<!DOCTYPE html>
<html>
  <head>
    <title>Dominate</title>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>'''


def test_bare_decorator():
  @document
  def foo():
    p('Hello World')

  assert foo().render() == \
'''<!DOCTYPE html>
<html>
  <head>
    <title>Dominate</title>
  </head>
  <body>
    <p>Hello World</p>
  </body>
</html>'''


def test_title():
  d = document()
  assert d.title == 'Dominate'

  d = document(title='foobar')
  assert d.title == 'foobar'

  d.title = 'baz'
  assert d.title == 'baz'

  d.title = title('bar')
  assert d.title == 'bar'

  assert d.render() == \
'''<!DOCTYPE html>
<html>
  <head>
    <title>bar</title>
  </head>
  <body></body>
</html>'''


if __name__ == '__main__':
  # test_doc()
  test_decorator()
