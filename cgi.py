
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
        print 'Content-Type: text/html'
        print
        print '<pre>'
        print 'An error occured while generating this page:'
        print
        import traceback
        print traceback.format_exc()
        print '</pre>'
        
    f.close()
    sys.exit(0)
    
