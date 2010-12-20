import os.path as p
from html import script
__all__ = ['source','script']
source = open(p.join(p.dirname(__file__), 'html.js'), 'rb').read()
script = script(source)


