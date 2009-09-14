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

from pyy_html.html import *
from pyy_html.dtd  import *

COMMON_CORE  = ['class', 'id', 'style', 'title']
COMMON_I18N  = ['lang', 'dir']
COMMON_EVENT = ['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup']
COMMON       = COMMON_CORE + COMMON_I18N + COMMON_EVENT


class html4strict(dtd):
  docstring = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
  
  valid = {
    html : {'valid'   : COMMON_I18N},
    head : {'valid'   : ['profile'] + COMMON_I18N},
    title: {'valid'   : COMMON_I18N},
    meta : {'valid'   : ['http-equiv', 'name', 'content', 'scheme'] + COMMON_I18N,
            'required': ['content']},
    body : {'valid'   : ['onload', 'onunload'] + COMMON},

    bdo: {'valid'   : ['lang', 'dir'] + COMMON_CORE,
          'required': ['dir']},

    div : {'valid': COMMON},
    span: {'valid': COMMON},

    h1: {'valid': COMMON},
    h2: {'valid': COMMON},
    h3: {'valid': COMMON},
    h4: {'valid': COMMON},
    h5: {'valid': COMMON},
    h6: {'valid': COMMON},

    address: {'valid': COMMON},

    em     : {'valid': COMMON},
    strong : {'valid': COMMON},
    dfn    : {'valid': COMMON},
    code   : {'valid': COMMON},
    samp   : {'valid': COMMON},
    kbd    : {'valid': COMMON},
    var    : {'valid': COMMON},
    cite   : {'valid': COMMON},
    abbr   : {'valid': COMMON},
    acronym: {'valid': COMMON},

    blockquote: {'valid': ['cite'] + COMMON},
    q         : {'valid': ['cite'] + COMMON},

    sub: {'valid': COMMON},
    sup: {'valid': COMMON},

    p: {'valid': COMMON},

    br: {'valid': COMMON_CORE},

    pre: {'valid': COMMON},

    ins : {'valid': ['cite', 'datetime'] + COMMON},
    del_: {'valid': ['cite', 'datetime'] + COMMON},

    ul: {'valid': COMMON},
    ol: {'valid': COMMON},
    li: {'valid': COMMON},
    dl: {'valid': COMMON},
    dt: {'valid': COMMON},
    dd: {'valid': COMMON},

    table   : {'valid': ['summary', 'width', 'border', 'frame', 'rules', 'cellspacing', 'cellpadding'] + COMMON},
    caption : {'valid': COMMON},
    thead   : {'valid': ['align', 'char', 'charoff', 'valign'] + COMMON},
    tbody   : {'valid': ['align', 'char', 'charoff', 'valign'] + COMMON},
    tfoot   : {'valid': ['align', 'char', 'charoff', 'valign'] + COMMON},
    colgroup: {'valid': ['span', 'width', 'align', 'char', 'charoff', 'valign'] + COMMON},
    col     : {'valid': ['span', 'width', 'align', 'char', 'charoff', 'valign'] + COMMON},
    tr      : {'valid': ['align', 'char', 'charoff', 'valign'] + COMMON},
    td      : {'valid': ['abbr', 'axis', 'headers', 'scope', 'rowspan', 'colspan', 'align', 'char', 'charoff', 'valign'] + COMMON},
    th      : {'valid': ['abbr', 'axis', 'headers', 'scope', 'rowspan', 'colspan', 'align', 'char', 'charoff', 'valign'] + COMMON},

    a   : {'valid'   : ['charset', 'type', 'name', 'href', 'hreflang', 'rel', 'rev', 'accesskey', 'shape', 'coords', 'tabindex', 'onfocus', 'onblur'] + COMMON},
    link: {'valid'   : ['charset', 'href', 'hreflang', 'type', 'rel', 'rev', 'media'] + COMMON},
    base: {'valid'   : ['href'],
           'required': ['href']},

    img    : {'valid'   : ['src', 'alt', 'longdesc', 'name', 'height', 'width', 'usemap', 'ismap'] + COMMON,
              'required': ['src', 'alt'],
              'default' : {'alt': ''}},
    object_: {'valid'   : ['declare', 'classid', 'codebase', 'data', 'type', 'codetype', 'archive', 'standby', 'height', 'width', 'usemap', 'name', 'tabindex'] + COMMON},
    param  : {'valid'   : ['id', 'name', 'value', 'valuetype', 'type'],
              'required': ['name']},
    map_   : {'valid'   : ['name'] + COMMON,
              'required': ['name']},
    area   : {'valid'   : ['shape', 'coords', 'href', 'nohref', 'alt', 'tabindex', 'accesskey', 'onfocus', 'onblur'] + COMMON,
              'required': ['alt'],
              'default' : {'alt': ''}},

    style: {'valid'   : ['type', 'media', 'title'] + COMMON,
            'required': ['type']},

    tt    : {'valid': COMMON},
    i     : {'valid': COMMON},
    b     : {'valid': COMMON},
    big   : {'valid': COMMON},
    small : {'valid': COMMON},
    strike: {'valid': COMMON},
    s     : {'valid': COMMON},
    u     : {'valid': COMMON},
    hr    : {'valid': COMMON},

    form    : {'valid'   : ['action', 'method', 'enctype', 'accept', 'name', 'onsubmit', 'onreset', 'accept-charset'] + COMMON,
               'required': ['action']},
    _input  : {'valid'   : ['type', 'name', 'value', 'checked', 'disabled', 'readonly', 'size', 'maxlength', 'src', 'alt', 'usemap', 'ismap', 'tabindex', 'accesskey', 'onfocus', 'onblur', 'onselect', 'onchange', 'accept'] + COMMON},
    button  : {'valid'   : ['name', 'value', 'type', 'disabled', 'tabindex', 'accesskey', 'onfocus', 'onblur'] + COMMON},
    select  : {'valid'   : ['name', 'size', 'multiple', 'disabled', 'tabindex', 'onfocus', 'onblur', 'onchange'] + COMMON},
    optgroup: {'valid'   : ['disabled', 'label'] + COMMON},
    option  : {'valid'   : ['selected', 'disabled', 'label', 'value'] + COMMON},
    textarea: {'valid'   : ['name', 'rows', 'cols', 'disabled', 'readonly', 'tabindex', 'accesskey', 'onfocus', 'onblur', 'onselect', 'onchange'] + COMMON,
               'required': ['rows', 'cols']},
    label   : {'valid'   : ['for', 'accesskey', 'onfocus', 'onblur'] + COMMON},
    fieldset: {'valid'   : COMMON},
    legend  : {'valid'   : ['accesskey'] + COMMON},

    script  : {'valid'   : ['charset', 'type', 'src', 'defer'],
               'required': ['type']},
    noscript: {'valid': COMMON},
}
