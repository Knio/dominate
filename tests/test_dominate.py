
def test_version():
  import dominate
  version = '3.1.0'
  assert dominate.version == version
  assert dominate.__version__ == version
