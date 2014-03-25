from dominate.tags import *

def test_dom():
  container = div()
  with container.add(div(id='base')) as dom:
    s1 = span('Hello', id='span1')
    s2 = span('World', id='span2')
  
  s3 = span('foobar', id='span3')
  dom.appendChild(s3)

  assert container.getElementById('base') is dom  
  assert container.getElementById('span1') is s1
  assert container.getElementById('span3') is s3
  assert container.getElementsByTagName('span') == [s1, s2, s3]
  assert container.getElementsByTagName('SPAN') == [s1, s2, s3]
