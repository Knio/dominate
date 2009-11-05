#!python

#Get documentation and repository directories
import os
docs_dir = os.path.dirname(os.path.realpath(__file__))
repo_dir = os.path.dirname(docs_dir)

#Ensure we are using the repository version of pyy
import sys
sys.path.insert(0, repo_dir)

#Import documentation generator
from pyy_doc.documenter import pyy_doc
from pyy_html.dtd       import html5
from pyy_html.html      import link

#Search for 'pyy_'-prefixed directories
for module in filter(lambda x: os.path.isdir(x) and x.startswith('pyy_'), os.listdir(repo_dir)):
    print 'Generating documentation for %s module...' % module
    doc = pyy_doc(module, doctype=html5)
    doc.head += link(type='text/css', rel='stylesheet', media='screen', href='docs.css')
    
    #Generate README.md files for GitHub
    print '  * README.md'
    f = open(os.path.join(repo_dir, module, 'README.md'), 'w')
    f.write(doc.description)
    f.close()
    
    #Print module overview file
    print '  * %s.html' % module
    f = open(os.path.join(docs_dir, '%s.html'%module), 'w')
    f.write(doc.render())
    f.close()
