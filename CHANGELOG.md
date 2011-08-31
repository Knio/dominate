Change Log
==========

Version 1.0.2 *(In Development)*
--------------------------------
* `pyy.cgi` is now directly importable to trigger functionality.
* Any instance representing a number is now accepted inside tags and converted to string.
* Fixed infinite recursion bug in the utilities when `__repr__` was invoked.


Version 1.0.1 *(2009-11-04)*
----------------------------
* Moved `httperror` to `pyy_web` to remove dependancy on `pyy.httpserver`.
* `document` DOCTYPE is now set via the `doctype` attribute or the `doctype` keyword argument only.
* `document` title is no longer stored seperately from the `<title>` tag.
* `pyy.cgi` is now properly usable when it is installed.


Version 1.0.0 *(2009-10-31)*
----------------------------
* Initial public release.
