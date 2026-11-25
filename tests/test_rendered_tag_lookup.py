import pytest

from dominate.tags import del_, div, input_, map_, object_


@pytest.mark.parametrize('tag_cls, name', [(input_, 'input'), (del_, 'del'),
                                         (map_, 'map'), (object_, 'object')])
def test_lookup_uses_html_name_for_underscored_tags(tag_cls, name):
  child = tag_cls(id='target')
  root = div(div(child), 'text')
  assert root.getElementsByTagName(name.upper()) == [child]
  assert root.get(name, id='target') == [child]
  assert root.get(name, id='other') == []
  assert root.get(tag_cls.__name__) == [child]
  assert root.get(tag_cls) == [child]


def test_lookup_respects_explicit_tagname():
  class StatusCard(div):
    tagname = 'status-card'

  child = StatusCard('Ready')
  root = div(child, 'plain text')
  assert '<status-card>' in root.render()
  assert root.getElementsByTagName('status-card') == [child]
  assert root.get('StatusCard') == [child]
  assert root.get('div') == []
