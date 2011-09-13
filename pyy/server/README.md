pyy.server
==========

`pyy.server` is a lightweight, highly configurable web server written using
stackless python for ultimate effeciency.

__`pyy.server` is still considered highly experimental.__


Usage
=====

`pyy.server` allows you to serve files with different pluggable modules
based upon a variety of conditions.

The server is configured with a series of specifiers and handlers arranged in
a list:

    [ SPECIFIER, HANDLER, ... ]

`SPECIFIER` must be one of:

 * A regular expression string will match that hostname (or uri, in a
   sub-handler).
 * An HTTP error code matches that code.
 * `httperror` matches all errors.
 * `None` will match `None` or the empty string.
 * `True` will match everything.

If no specifiers match, an httperror(404) will be returned.

If multiple specifiers match, the last one will be used. If the last one
returns a 404 error, then the second last one will be used, etc.

*Note that if a leaf-node (final handler) raises a 404, that error will be
handled normally and will not cause the resolver to keep looking.*

`HANDLER` must be one of:

 * `[ SPECIFIER, HANDLER, ...]` to do further processing.
 * A function object will be called with `f(*args)` where `args` is a list of
   all regex matches that were encountered in the entire processing of this 
   request. The function's return value will then be used as a new `HANDLER`.
 * A handler object will be called with `.handle(httpserver, request, response,
   *args)` (or `.handle_error(..)` if this is an error match).
 * `None` to do nothing.
 * An `httperror` instance to raise that error.

You can see an example server configuration
[here](http://github.com/Knio/pyy/blob/master/docs/example/run.py).
