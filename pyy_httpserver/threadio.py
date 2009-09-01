import stackless
import threading

class threadio(object):
  def __init__(self, file):
    self.file = file   

  def __getattr__(self, attr):
    f = getattr(self.file, attr)
    def wrapper(*args):
      ch = stackless.channel()    
      def thread():
        try:
          r = f(*args)
          ch.send(r)
        except Exception, e:
          ch.send_exception(type(e), e)
      threading.Thread(target=thread).start()
      return ch.receive()
    return wrapper


