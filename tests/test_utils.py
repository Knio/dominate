import dominate
from dominate.tags import *
from dominate import util


def test_context():
  id1 = dominate.dom_tag._get_thread_context()
  id2 = dominate.dom_tag._get_thread_context()
  assert id1 == id2

def test_include():
  import os
  try:
    f = open('_test_include.deleteme', 'w')
    f.write('Hello World')
    f.close()

    d = div()
    d += util.include('_test_include.deleteme')
    assert d.render() == '<div>Hello World</div>'

  finally:
    try:
      os.remove('_test_include.deleteme')
    except:
      pass


def test_system():
  d = div()
  d += util.system('echo Hello World')
  assert d.render().replace('\r\n', '\n') == '<div>Hello World\n</div>'


def test_unescape():
  assert util.unescape('&amp;&lt;&gt;&#32;') == '&<> '


def test_unescape_edge_cases():
  # Empty input
  assert util.unescape('') == ''

  # No entities
  assert util.unescape('hello world') == 'hello world'

  # Largest valid Unicode code point (U+10FFFF)
  assert util.unescape('&#1114111;') == '\U0010ffff'

  # Beyond valid Unicode range (U+110000) should not crash
  assert util.unescape('&#1114112;') == '�'

  # Unknown named entity replaced with question mark
  assert util.unescape('&unknown;') == '?'

  # Multiple entities in one string
  assert util.unescape('&amp;&lt;&gt;') == '&<>'


def test_url():
  assert util.url_escape('hi there?') == 'hi%20there%3F'
  assert util.url_unescape('hi%20there%3f') == 'hi there?'


def test_container():
  d = div()
  with d:
    with util.container():
      pass
  assert d.render() == '<div></div>'


  d = div()
  with d:
    with util.container():
      h1('a')
  assert d.render() == \
'''<div>
  <h1>a</h1>
</div>'''
