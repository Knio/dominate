Welcome to pyy!
===============

`pyy`_ is a python library designed to allow for rapid creation of HTML5
applications through tight integration with your server-side code.

    >>> print html(body(div('Forget templates and binding.')))
    <html>
      <body>
        <div>Forget templates and binding.</div>
      </body>
    </html>

The foundation of the library is in eliminating the need for an intermediate
templating language as well as the weak and often redundant bindings that come
with it. By coupling the HTML generation as simple object creation within your
code you can seamlessly create the necessary HTML for your application using
the expressive python syntax.

.. _pyy: http://pyy.im/


Contents:

.. toctree::
   :maxdepth: 2

   getting_started
   features

Modules:

.. toctree::
    :maxdepth: 2

    module_cgi
    module_html
    module_server
    module_web
