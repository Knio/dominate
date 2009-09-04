#!/usr/bin/env python

#Ensure we get the repository version and not an installed version
import sys
sys.path.insert(0, '..')

#Change tabs to tab character to simplify comparisons
from pyy_html.pyy_tag import pyy_tag
pyy_tag.TAB = '\t'

from unittest import defaultTestLoader, TestSuite, TextTestRunner
import pyy_cgi_tests, pyy_html_tests, pyy_httpserver_tests, pyy_web_tests

#Create individual module suites
suite_pyy_cgi        = defaultTestLoader.loadTestsFromModule(pyy_cgi_tests)
suite_pyy_html       = defaultTestLoader.loadTestsFromModule(pyy_html_tests)
suite_pyy_httpserver = defaultTestLoader.loadTestsFromModule(pyy_httpserver_tests)
suite_pyy_web        = defaultTestLoader.loadTestsFromModule(pyy_web_tests)

#Create entire package suite
suite_pyy = TestSuite([suite_pyy_cgi, suite_pyy_html, suite_pyy_httpserver, suite_pyy_web])

TextTestRunner().run(suite_pyy)
