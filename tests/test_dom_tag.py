import pytest
import unittest.mock as mock

from dominate.tags import *


def test___get_thread_context(monkeypatch):
    from dominate import dom_tag as sut
    greenlet = mock.Mock()
    greenlet.getcurrent.return_value = 100
    monkeypatch.setattr(sut, 'greenlet', greenlet)

    threading = mock.Mock()
    threading.current_thread.return_value = 200
    monkeypatch.setattr(sut, 'threading', threading)

    assert sut._get_thread_context() is not None

def test_add_raw_string():
    container = div()
    container.add_raw_string('foo')
    assert container.children == ['foo']

def test_clear():
    container = div()
    child = div()
    container.add(child)

    assert container.children == [child]
    assert child.parent == container

    container.clear()

    assert container.children == []
    assert child.parent is None

def test_remove_child_clears_parent():
    child = span('content')
    sibling = span('sibling')
    container = div(child, sibling)

    assert container.remove(child) is None
    assert container.children == [sibling]
    assert child.parent is None
    assert child.parentNode is None
    assert sibling.parentNode is container

def test_remove_duplicate_child():
    child = span()
    container = div(child, child)

    container.remove(child)
    assert container.children == [child]
    assert child.parentNode is container

    container.remove(child)
    assert container.children == []
    assert child.parentNode is None

def test_remove_child_with_another_parent():
    child = span()
    container = div(child)
    other = div(child)

    container.remove(child)
    assert container.children == []
    assert other.children == [child]
    assert child.parentNode is other

def test_remove_text():
    container = div('text')
    container.remove('text')
    assert container.children == []

def test_remove_missing_child():
    child = span()
    parent = div(child)
    other = div()

    with pytest.raises(ValueError):
        other.remove(child)

    assert parent.children == [child]
    assert child.parentNode is parent
    assert other.children == []

def test_remove_equal_children_detaches_removed_instance():
    class EqualTag(div):
        def __eq__(self, other):
            return isinstance(other, EqualTag)

    first, second = EqualTag(), EqualTag()
    container = div(first, second)

    container.remove(second)
    assert len(container.children) == 1
    assert container.children[0] is second
    assert first.parentNode is None
    assert second.parentNode is container

def test_set_attribute():
    container = div()
    container.add_raw_string('foo')
    container.set_attribute(0, 'bar')

    assert container.children == ['bar']

def test_delete_attribute_child_index():
    container = div('foo', 'bar')

    container.delete_attribute(-1)
    assert container.children == ['foo']

    with pytest.raises(IndexError):
        container.delete_attribute(10)

def test_set_attribute_error():
    container = div()
    with pytest.raises(TypeError, match=(
            'Only integer and string types are valid for assigning '
            'child tags and attributes, respectively.'
        )):
        container.set_attribute(1.0, 'foo')

def test___get_item___child_index_error():
    d = div()
    with pytest.raises(IndexError, match='Child with index "10" does not exist.'):
        d[10]

def test___contains__():
    container = div()
    container.add(div())
    assert 'div' in container

def test_nested_context():
    def sub(*args):
        with div('B') as B:
            B.add(*args)

    with div('A') as A:
        sub(div('C'))

    assert str(A) == \
'''<div>A
  <div>B
    <div>C</div>
  </div>
</div>'''
