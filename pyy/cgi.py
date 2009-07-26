# cgi.py - pyy GCI gateway
#
# WARNING: Edit this file very carefully, a bug will crash your site!

__license__ = '''
This file is part of pyy.

pyy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

pyy is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with pyy.  If not, see
<http://www.gnu.org/licenses/>.
'''

if __name__ == '__main__':
    import os
    import sys
    import imp
    
    fname = sys.argv[1]
    mname = os.path.basename(fname).split('.')[0]
    dname = os.path.dirname(fname)
    sys.path.append(dname)
    
    f = open(fname, 'U')
    
    try:
        imp.load_module(mname, f, fname, ('.py', 'U', 1))
        
    except SystemExit:
        pass
        
    except Exception, e:
        import traceback
        print 'Content-Type: text/html'
        print
        print '<html><head><title>Error</title></head><body><pre>'
        print 'An error occured while generating this page:'
        print
        print traceback.format_exc()
        print '</pre></body></html>'
        
    f.close()
    sys.exit(0)
