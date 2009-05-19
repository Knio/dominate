# cgi.py - pyy GCI gateway
#
# Edit this file very carefully, a bug will crash your site.

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
        print '<pre>'
        print 'An error occured while generating this page:'
        print
        print traceback.format_exc()
        print '</pre>'
        
    f.close()
    sys.exit(0)
