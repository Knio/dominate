from dominate.tags import *

def test_arguments():
  assert html(body(h1('Hello, pyy!'))).render() == \
'''<html>
  <body>
    <h1>Hello, pyy!</h1>
  </body>
</html>'''

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
