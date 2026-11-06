
from dominate import tags

def test_hx():
  d = tags.div(hx_foo=1)
  assert d.render() == '<div hx-foo="1"></div>'
