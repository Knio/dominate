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

import stackless
import threading

class threadio(object):
  def __init__(self, file):
    self.file = file

  def __getattr__(self, attr):
    f = getattr(self.file, attr)
    if not callable(f):
      return f
    def wrapper(*args, **kwargs):
      ch = stackless.channel()
      def thread():
        try:
          r = f(*args, **kwargs)
          ch.send(r)
        except Exception, e:
          ch.send_exception(type(e), e)
      threading.Thread(target=thread).start()
      return ch.receive()
    return wrapper


