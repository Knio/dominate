from dominate import document
from dominate.tags import title


def test_untitled_document_can_receive_a_title():
  doc = document(title=None)
  assert doc.title is None
  assert repr(doc) == '<dominate.document "None">'
  doc.title = 'Report'
  assert doc.title == 'Report'
  assert '<title>Report</title>' in doc.render()
  doc.title = 'Updated report'
  assert doc.title == 'Updated report'


def test_title_node_can_be_assigned_to_untitled_document():
  doc = document(title=None)
  node = title('Report')
  doc.title = node
  assert doc.head.get(title) == [node]
  assert doc.title == 'Report'


def test_title_can_be_removed_and_restored():
  doc = document('Report')
  doc.title = None
  assert doc.title is None
  assert doc.head.get(title) == []
  doc.title = None
  doc.title = title('Restored')
  assert doc.title == 'Restored'
  assert '<title>Restored</title>' in doc.render()
