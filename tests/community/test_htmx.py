
from dominate import tags
import dominate.community.htmx

def test_hx():
  d = tags.div(hx_foo=1)
  assert d.render() == '<div hx-foo="1"></div>'
