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
from pyy_html.dtd  import dtd

COMMON_MAIN   = ['class', 'contenteditable', 'contextmenu', 'dir', 'draggable', 'id', 'hidden', 'lang', 'spellcheck', 'style', 'tabindex', 'title']
COMMON_EVENTS = ['onabort', 'onblur', 'onchange', 'onclick', 'oncontextmenu', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'onerror', 'onfocus', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onscroll', 'onselect', 'onsubmit']
COMMON        = COMMON_MAIN + COMMON_EVENTS

class html5(dtd):
  docstring = '<!DOCTYPE html>'
  
  valid = {
    #Root element
    html: {'valid': COMMON + ['manifest']},
    
    #Document metadata
    head : {'valid'   : COMMON},
    title: {'valid'   : COMMON},
    base : {'valid'   : COMMON + ['href', 'target'],
            'custom'  : lambda x: 'href' in x or 'target' in x},
    link : {'valid'   : COMMON + ['href', 'rel', 'media', 'hreflang', 'type', 'sizes'],
            'required': ['href', 'rel']},
    meta : {'valid'   : COMMON + ['name', 'http-equiv', 'content', 'charset'],
            'custom'  : lambda x: 'name' in x or 'http-equiv' in x or 'content' in x or 'charset' in x},
    style: {'valid'   : COMMON + ['media', 'type', 'scoped']},
    
    #Scripting
    script  : {'valid': COMMON + ['src', 'async', 'defer', 'type', 'charset']},
    noscript: {'valid': COMMON},

    #Sections
    body   : {'valid': COMMON + ['onafterprint', 'onbeforeprint', 'onbeforeunload', 'onhashchange', 'onmessage', 'ononline', 'onoffline', 'onpopstate', 'onredo', 'onresize', 'onstorage', 'onundo', 'onunload']},
    section: {'valid': COMMON + ['cite']},
    nav    : {'valid': COMMON},
    article: {'valid': COMMON + ['cite', 'pubdate']},
    aside  : {'valid': COMMON},
    h1     : {'valid': COMMON},
    h2     : {'valid': COMMON},
    h3     : {'valid': COMMON},
    h4     : {'valid': COMMON},
    h5     : {'valid': COMMON},
    h6     : {'valid': COMMON},
    hgroup : {'valid': COMMON},
    header : {'valid': COMMON},
    footer : {'valid': COMMON},
    address: {'valid': COMMON},

    #Grouping content
    p         : {'valid': COMMON},
    hr        : {'valid': COMMON},
    br        : {'valid': COMMON},
    pre       : {'valid': COMMON},
    dialog    : {'valid': COMMON},
    blockquote: {'valid': COMMON + ['cite']},
    ol        : {'valid': COMMON + ['reversed', 'start']},
    ul        : {'valid': COMMON},
    li        : {'valid': COMMON},
    dl        : {'valid': COMMON},
    dt        : {'valid': COMMON},
    dd        : {'valid': COMMON},

    #Text-level semantics
    a       : {'valid': COMMON + ['href', 'target', 'ping', 'rel', 'media', 'hreflang', 'type']},
    q       : {'valid': COMMON + ['cite']},
    cite    : {'valid': COMMON},
    em      : {'valid': COMMON},
    strong  : {'valid': COMMON},
    small   : {'valid': COMMON},
    mark    : {'valid': COMMON},
    dfn     : {'valid': COMMON},
    abbr    : {'valid': COMMON},
    time    : {'valid': COMMON + ['datetime']},
    progress: {'valid': COMMON + ['value', 'max']},
    meter   : {'valid': COMMON + ['value', 'min', 'low', 'high', 'max', 'optimum']},
    code    : {'valid': COMMON},
    var     : {'valid': COMMON},
    samp    : {'valid': COMMON},
    kbd     : {'valid': COMMON},
    sub     : {'valid': COMMON},
    sup     : {'valid': COMMON},
    span    : {'valid': COMMON},
    i       : {'valid': COMMON},
    b       : {'valid': COMMON},
    bdo     : {'valid': COMMON},
    ruby    : {'valid': COMMON},
    rt      : {'valid': COMMON},
    rp      : {'valid': COMMON},

    #Edits
    ins : {'valid': COMMON + ['cite', 'datetime']},
    del_: {'valid': COMMON + ['cite', 'datetime']},

    #Embedded content
    figure : {'valid'   : COMMON},
    img    : {'valid'   : COMMON + ['alt', 'src', 'usemap', 'ismap', 'width', 'height'],
              'required': ['src']},
    iframe : {'valid'   : COMMON + ['src', 'name', 'sandbox', 'seamless', 'width', 'height']},
    embed  : {'valid'   : COMMON + ['src', 'type', 'width', 'height']},
    object_: {'valid'   : COMMON + ['data', 'type', 'name', 'usemap', 'form', 'width', 'height']},
    param  : {'valid'   : COMMON + ['name', 'value']},
    video  : {'valid'   : COMMON + ['src', 'poster', 'autobuffer', 'autoplay', 'loop', 'controls', 'width', 'height']},
    audio  : {'valid'   : COMMON + ['src', 'autobuffer', 'autoplay', 'loop', 'controls']},
    source : {'valid'   : COMMON + ['src', 'type', 'media']},
    canvas : {'valid'   : COMMON + ['width', 'height']},
    map_   : {'valid'   : COMMON + ['name']},
    area   : {'valid'   : COMMON + ['alt', 'coords', 'shape', 'href', 'target', 'ping', 'rel', 'media', 'hreflang', 'type']},

    #Tabular data
    table   : {'valid': COMMON},
    caption : {'valid': COMMON},
    colgroup: {'valid': COMMON + ['span']},
    tbody   : {'valid': COMMON},
    thead   : {'valid': COMMON},
    tfoot   : {'valid': COMMON},
    tr      : {'valid': COMMON},
    td      : {'valid': COMMON + ['colspan', 'rowspan', 'headers']},
    th      : {'valid': COMMON + ['colspan', 'rowspan', 'headers', 'scope']},

    #Forms
    form    : {'valid': COMMON + ['accept-charset', 'action', 'autocomplete', 'enctype', 'method', 'name', 'novalidate', 'target']},
    fieldset: {'valid': COMMON + ['disabled', 'form', 'name']},
    label   : {'valid': COMMON + ['form', 'for']},
    input_  : {'valid': COMMON + ['accept', 'alt', 'autocomplete', 'autofocus', 'checked', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'height', 'list', 'max', 'maxlength', 'min', 'multiple', 'name', 'pattern', 'placeholder', 'readonly', 'required', 'size', 'src', 'step', 'type', 'value', 'width']},
    button  : {'valid': COMMON + ['autofocus', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'name', 'type', 'value']},
    select  : {'valid': COMMON + ['autofocus', 'disabled', 'form', 'multiple', 'name', 'size']},
    datalist: {'valid': COMMON},
    optgroup: {'valid': COMMON + ['disabled', 'label']},
    option  : {'valid': COMMON + ['disabled', 'label', 'selected', 'value']},
    textarea: {'valid': COMMON + ['autofocus', 'cols', 'disabled', 'form', 'maxlength', 'name', 'placeholder', 'readonly', 'required', 'rows', 'wrap']},
    keygen  : {'valid': COMMON + ['autofocus', 'challenge', 'disabled', 'form', 'keytype', 'name']},
    output  : {'valid': COMMON + ['for', 'form', 'name']},

    #Interactive elements
    details : {'valid': COMMON + ['open']},
    datagrid: {'valid': COMMON + ['disabled']},
    command : {'valid': COMMON + ['type', 'label', 'icon', 'disabled', 'checked', 'radiogroup']},
    bb      : {'valid': COMMON + ['type']},
    menu    : {'valid': COMMON + ['type', 'label']},

    #Miscellaneous elements
    legend: {'valid': COMMON},
    div   : {'valid': COMMON},
}
