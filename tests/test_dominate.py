
def test_version():
  import dominate
  version = '3.0.0'
  assert dominate.version == version
  assert dominate.__version__ == version
