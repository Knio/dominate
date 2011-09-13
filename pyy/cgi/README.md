pyy.cgi
=======

`pyy.cgi` provides a common standardized interface between a web server and a
dynamic application being used to serve content.



Usage
=====

If you are working within a CGI environment, using `pyy.cgi` will allow your
application to fail somewhat gracefully and will provide you with an easy means
to access the request and response parameters.

Simply add `import pyy.cgi` as the first line in your file to activate the
module. Then define one or more functions that correspond with HTTP methods to
be called for a request.

    def get(handler, request, response):
        response.body = 'Hello, World!'

Be sure to designate a function for each HTTP method you would like to support
because an HTTP 405 error will be generated if no appropriate function is
found. If you do all your processing in the same place as your generation you
can simply add `post = get` to pass in all the POST requests.

Should your file have a syntax error or produce a run-time error `pyy.cgi` will
catch and display it rather than just causing the server to produce an HTTP 500
error.
