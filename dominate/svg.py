'''
This module consists of classes specific to HTML5-SVG Elements. In general this module does not include
- Elements that are not specific to SVG (eg. <a>)
- Elements that are deprecated
'''
from dominate.tags import html_tag


__license__ = '''
This file is part of Dominate.

Dominate is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

Dominate is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with Dominate.  If not, see
<http://www.gnu.org/licenses/>.
'''
from .dom_tag  import dom_tag, attr
from .dom1core import dom1core

try:
  basestring = basestring
except NameError: # py3
  basestring = str
  unicode = str

  underscored_classes = set(['del', 'input', 'map', 'object', 'from'])

# Tag attributes
_ATTR_GLOBAL = set([
  'accesskey', 'class', 'class', 'contenteditable', 'contextmenu', 'dir',
  'draggable', 'id', 'item', 'hidden', 'lang', 'itemprop', 'spellcheck',
  'style', 'subject', 'tabindex', 'title'
])

# https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/Events#Attributes
_ATTR_EVENTS = set([
    'onbegin', 'onend', 'onrepeat',
    'onabort', 'onerror', 'onresize', 'onscroll', 'onunload',
    'oncopy', 'oncut', 'onpaste',
    'oncancel', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'onclose', 'oncuechange', 'ondblclick',
    'ondrag', 'ondragend', 'ondragenter', 'ondragexit', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop',
    'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress',
    'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata','onloadstart', 'onmousedown', 'onmouseenter',
    'onmouseleave', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onpause', 'onplay',
    'onplaying', 'onprogress', 'onratechange', 'onreset', 'onresize', 'onscroll', 'onseeked', 'onseeking', 'onselect',
    'onshow', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate', 'ontoggle', 'onvolumechange', 'onwaiting'
])


# https://developer.mozilla.org/en-US/docs/Web/SVG/Element/svg

# SVG

class svg(html_tag):
    pass


class animate(html_tag):
    '''
    The  animate SVG element is used to animate an attribute or property of an element over time.
    It's normally inserted inside the element or referenced by the href attribute of the target element.
    '''
    pass


class animateMotion(html_tag):
    '''
    The <animateMotion> element causes a referenced element to move along a motion path.
    '''
    pass


class animateTransform(html_tag):
    '''
    The animateTransform element animates a transformation attribute on its target element, thereby allowing
    animations to control translation, scaling, rotation, and/or skewing.
    '''
    is_single = True


class circle(html_tag):
    '''
    The <circle> SVG element is an SVG basic shape, used to draw circles based on a center point and a radius.
    '''
    is_single = True


class mpath(html_tag):
    '''
    The <mpath> sub-element for the <animateMotion> element provides the ability to reference an
    external <path> element as the definition of a motion path.
    '''
    pass


class text(html_tag):
    '''
    The SVG <text> element draws a graphics element consisting of text. It's possible to apply a gradient,
     pattern, clipping path, mask, or filter to <text>, like any other SVG graphics element.
    '''
    pass


class textPath(html_tag):
    '''
    To render text along the shape of a <path>, enclose the text in a <textPath> element that has an href
    attribute with a reference to the <path> element.
    '''
    pass


class tspan(html_tag):
    '''
    The SVG <tspan> element define a subtext within a <text> element or another <tspan> element.
    It allows to adjust the style and/or position of that subtext as needed.
    '''
    pass


class ellipse(html_tag):
  '''
  An ellipse element for svg containers
  '''
  pass

class line(html_tag):
  '''
  A line element for svg containers
  '''
  pass

class linearGradient(html_tag):
  '''
  Linear gradient element for svg containers
  '''
  pass

class path(html_tag):
  '''
  A path element for svg containers
  '''
  pass

class polygon(html_tag):
  '''
  A polygon element for svg containers
  '''
  pass

class polyline(html_tag):
  '''
  A polyline element for svg containers
  '''
  pass

class rectangle(html_tag):
  '''
  A rectangle element for svg containers
  '''
  pass


