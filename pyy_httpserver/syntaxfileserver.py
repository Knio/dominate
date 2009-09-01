import fileserver
import threadio
import os

class syntaxfileserver(fileserver.fileserver):
  def write_file(self, conn, req, res, path, type):
               
    cmd = r'Z:\Programs\GVimPortable\GVimPortable.exe'\
        r' -f +":let html_use_css = 1" +":let use_xhtml=1" +":TOhtml" +":wq!" +":q!" "'+path+'"'

    fin, fout = os.popen4(cmd, 't')
    threadio.threadio(fin).close()
    threadio.threadio(fout).read()
    path += '.html'
    
    res.headers['Content-Length'] = fsize = os.path.getsize(path)
    res.headers['Content-Type'] = 'text/html' # xhtml?
    
    return fileserver.fileserver.write_file(self, conn, req, res, path)


