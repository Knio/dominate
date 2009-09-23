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

from pyy_html.html  import *
from dtd            import *

#Attributes
CORE     = set(['class', 'id', 'style', 'title'])
I18N     = set(['lang', 'dir'])
EVENT    = set(['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup'])

COLORS   = set(['bgcolor', 'text', 'link', 'vlink', 'alink'])
RESERVED = set(['datasrc', 'datafld', 'dataformatas'])

ATTRS    = CORE | I18N | EVENT

#Children
FONT    = set([tt, i, b, u, s, strike, big, small])
PHRASE  = set([em, strong, dfn, code, samp, kbd, var, cite, abbr, acronym])
SPECIAL = set([a, img, applet, object, font, basefont, br, script, map, q, sub, sup, span, bdo, iframe])
FORM    = set([input, select, textarea, label, button])
INLINE  = FONT | PHRASE | SPECIAL | FORM | set([str])

HEADING = set([h1, h2, h3, h4, h5, h6])
LIST    = set([ul, ol, dir, menu])
PREFORM = set([pre])
BLOCK   = HEADING | LIST | PREFORM | set([p, dl, div, center, noscript, noframes, blockquote, form, isindex, hr, table, fieldset, address])

FLOW    = BLOCK | INLINE


class html4strict(dtd):
  docstring = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
  
  valid = {
  #NEW:
    
    #TEXT MARKUP
    tt      : {VALID: ATTRS, CHILDREN: INLINE},
    i       : {VALID: ATTRS, CHILDREN: INLINE},
    b       : {VALID: ATTRS, CHILDREN: INLINE},
    u       : {VALID: ATTRS, CHILDREN: INLINE},
    s       : {VALID: ATTRS, CHILDREN: INLINE},
    strike  : {VALID: ATTRS, CHILDREN: INLINE},
    big     : {VALID: ATTRS, CHILDREN: INLINE},
    small   : {VALID: ATTRS, CHILDREN: INLINE},
    em      : {VALID: ATTRS, CHILDREN: INLINE},
    strong  : {VALID: ATTRS, CHILDREN: INLINE},
    dfn     : {VALID: ATTRS, CHILDREN: INLINE},
    code    : {VALID: ATTRS, CHILDREN: INLINE},
    samp    : {VALID: ATTRS, CHILDREN: INLINE},
    kbd     : {VALID: ATTRS, CHILDREN: INLINE},
    var     : {VALID: ATTRS, CHILDREN: INLINE},
    cite    : {VALID: ATTRS, CHILDREN: INLINE},
    abbr    : {VALID: ATTRS, CHILDREN: INLINE},
    acronym : {VALID: ATTRS, CHILDREN: INLINE},
    sub     : {VALID: ATTRS, CHILDREN: INLINE},
    sup     : {VALID: ATTRS, CHILDREN: INLINE},
    span    : {VALID: ATTRS | RESERVED, CHILDREN: INLINE},
    bdo     : {VALID: CORE | set(['lang', 'dir']), CHILDREN: INLINE, REQUIRED: set(['dir'])},
    basefont: {VALID: set(['id', 'size', 'color', 'face']), REQUIRED: set(['size'])},
    font    : {VALID: CORE | I18N | set(['size', 'color', 'face']), CHILDREN: INLINE},
    br      : {VALID: CORE | set(['clear'])},
    
    #DOCUMENT BODY
    body   : {VALID: ATTRS | COLORS | set(['onload', 'onunload', 'background']), CHILDREN: FLOW | set([ins, del_])},
    address: {VALID: ATTRS, CHILDREN: INLINE | set([p])},
    div    : {VALID: ATTRS | RESERVED | set(['align']), CHILDREN: FLOW},
    center : {VALID: ATTRS, CHILDREN: FLOW},
    
    #ANCHOR
    a: {VALID   : ATTRS | set(['charset', 'type', 'name', 'href', 'hreflang', 'target', 'rel', 'rev', 'accesskey', 'shape', 'coords', 'tabindex', 'onfocus', 'onblur']),
        CHILDREN: INLINE ^ set([a])},
    
    #CLIENT-SIDE IMAGE MAPS
    map_: {VALID   : ATTRS | set(['name']),
           CHILDREN: BLOCK | set([area]),
           REQUIRED: set(['name'])},
    area: {VALID   : ATTRS | set(['shape', 'coords', 'href', 'target', 'nohref', 'alt', 'tabindex', 'accesskey', 'onfocus', 'onblur']),
           REQUIRED: set(['alt'])},
    
    #LINK
    link: {VALID: ATTRS | set(['charset', 'href', 'hreflang', 'type', 'rel', 'rev', 'media', 'target'])},
    
    #IMAGES
    img: {VALID   : ATTRS | set(['src', 'alt', 'longdesc', 'name', 'height', 'width', 'usemap', 'ismap', 'align', 'border', 'hspace', 'vspace']),
          REQUIRED: set(['alt', 'src'])},
    
    #OBJECT
    object_: {VALID   : ATTRS | RESERVED | set(['declare', 'classid', 'codebase', 'data', 'type', 'codetype', 'archive', 'standby', 'height', 'width', 'usemap', 'name', 'tabindex', 'align', 'border', 'hspace', 'vspace']),
             CHILDREN: FLOW | set([param])},
    param : {VALID   : set(['id', 'name', 'value', 'valuetype', 'type']),
             REQUIRED: set(['name'])},
    
    #JAVA APPLET
    applet: {VALID   : CORE | set(['codebase', 'archive', 'code', 'object', 'alt', 'name', 'width', 'height', 'align', 'hspace', 'vspace']),
             CHILDREN: FLOW | set([param]),
             REQUIRED: set(['height', 'width'])},
    
    #HORIZONTAL RULE
    hr: {VALID: ATTRS | set(['align', 'noshade', 'size', 'width'])},
    
    #PARAGRAPHS
    p: {VALID: ATTRS | set(['align']), CHILDREN: INLINE},
    
    #HEADINGS
    h1: {VALID: ATTRS | set(['align']), CHILDREN: INLINE},
    h2: {VALID: ATTRS | set(['align']), CHILDREN: INLINE},
    h3: {VALID: ATTRS | set(['align']), CHILDREN: INLINE},
    h4: {VALID: ATTRS | set(['align']), CHILDREN: INLINE},
    h5: {VALID: ATTRS | set(['align']), CHILDREN: INLINE},
    h6: {VALID: ATTRS | set(['align']), CHILDREN: INLINE},
    
    #PREFORMATTED TEXT
    pre: {VALID: ATTRS | set(['width']), CHILDREN: INLINE ^ set([img, object_, applet, big, small, sub, sup, font, basefont])},
    
    #INLINE QUOTES
    q: {VALID: ATTRS | set(['cite']), CHILDREN: INLINE},
    
    #BLOCK-LIKE QUOTES
    blockquote: {VALID: ATTRS | set(['cite']), CHILDREN: FLOW},
    
    #INSERTED/DELETED TEXT
    ins : {VALID: ATTRS | set(['cite', 'datetime']), CHILDREN: FLOW},
    del_: {VALID: ATTRS | set(['cite', 'datetime']), CHILDREN: FLOW},
    
    #LISTS
    dl  : {VALID: ATTRS | set(['compact']), CHILDREN: set([dt, dd])},
    dt  : {VALID: ATTRS, CHILDREN: INLINE},
    dd  : {VALID: ATTRS, CHILDREN: FLOW},
    ol  : {VALID: ATTRS | set(['type', 'compact', 'start']), CHILDREN: set([li])},
    ul  : {VALID: ATTRS | set(['type', 'compact']), CHILDREN: set([li])},
    dir : {VALID: ATTRS | set(['compact']), CHILDREN: set([li])},
    menu: {VALID: ATTRS | set(['compact']), CHILDREN: set([li])},
    li  : {VALID: ATTRS | set(['type', 'value']), CHILDREN: FLOW},
    
    #FORMS
    form    : {VALID   : ATTRS | set(['action', 'method', 'enctype', 'accept', 'name', 'onsubmit', 'onreset', 'target', 'accept-charset']),
               REQUIRED: set(['action']),
               CHILDREN: FLOW ^ set([form])},
    label   : {VALID   : ATTRS | set(['for', 'accesskey', 'onfocus', 'onblur']),
               CHILDREN: INLINE ^ set([label])},
    input   : {VALID   : ATTRS | RESERVED | set(['type', 'name', 'value', 'checked', 'disabled', 'readonly', 'size', 'maxlength', 'src', 'alt', 'usemap', 'ismap', 'tabindex', 'accesskey', 'onfocus', 'onblur', 'onselect', 'onchange', 'accept', 'align'])},
    select  : {VALID   : ATTRS | RESERVED | set(['name', 'size', 'multiple', 'disabled', 'tabindex', 'onfocus', 'onblur', 'onchange']),
               CHILDREN: set([optgroup, option])},
    option  : {VALID   : ATTRS | set(['selected', 'disabled', 'label', 'value']),
               CHILDREN: set([str])},
    textarea: {VALID   : ATTRS | RESERVED | set(['name', 'rows', 'cols', 'disabled', 'readonly', 'tabindex', 'accesskey', 'onfocus', 'onblur', 'onselect', 'onchange']),
               REQUIRED: set(['rows', 'cols']),
               CHILDREN: set([str])},
    fieldset: {VALID   : ATTRS,
               CHILDREN: FLOW | set([legend, str])},
    legend  : {VALID   : ATTRS | set(['accesskey', 'align']),
               CHILDREN: INLINE},
    button  : {VALID   : ATTRS | set(['name', 'value', 'type', 'disabled', 'tabindex', 'accesskey', 'onfocus', 'onblur']),
               CHILDREN: FLOW ^ (set([a, form, isindex, fieldset, iframe]) | FORM)},
    
    #TABLES
    table   : {VALID   : ATTRS | RESERVED | set(['summary', 'width', 'boder', 'frame', 'rules', 'cellspacing', 'cellpadding', 'align', 'bgcolor', 'datapagesize']),
               CHILDREN: set([caption, col, colgroup, thead, tfoot, tbody])},
    caption : {VALID   : ATTRS | set(['align']),
               CHILDREN: INLINE},
    thead   : {VALID   : ATTRS | set(['align', 'char', 'charoff', 'valign']),
               CHILDREN: set([tr])},
    tfoot   : {VALID   : ATTRS | set(['align', 'char', 'charoff', 'valign']),
               CHILDREN: set([tr])},
    tbody   : {VALID   : ATTRS | set(['align', 'char', 'charoff', 'valign']),
               CHILDREN: set([tr])},
    colgroup: {VALID   : ATTRS | set(['span', 'width', 'align', 'char', 'charoff', 'valign']),
               CHILDREN: set([col])},
    col     : {VALID   : ATTRS | set(['span', 'width', 'align', 'char', 'charoff', 'valign'])},
    tr      : {VALID   : ATTRS | set(['bgcolor', 'align', 'char', 'charoff', 'valign']),
               CHILDREN: set([th, td])},
    th      : {VALID   : ATTRS | set(['abbr', 'axis', 'headers', 'scope', 'rowspan', 'colspan', 'align', 'char', 'charoff', 'valign', 'nowrap', 'bgcolor', 'width', 'height']),
               CHILDREN: FLOW},
    td      : {VALID   : ATTRS | set(['abbr', 'axis', 'headers', 'scope', 'rowspan', 'colspan', 'align', 'char', 'charoff', 'valign', 'nowrap', 'bgcolor', 'width', 'height']),
               CHILDREN: FLOW},
    
    #DOCUMENT HEAD
    head    : {VALID: I18N | set(['profile']),
               CHILDREN: set([script, style, meta, link, object_, title, isindex, base])},
    title   : {VALID: I18N,
               CHILDREN: set([str])},
    isindex : {VALID: CORE | I18N | set(['prompt'])},
    base    : {VALID: set(['href', 'target'])},
    meta    : {VALID: I18N | set(['http-equiv', 'name', 'content', 'scheme'])},
    style   : {VALID: I18N | set(['type', 'media', 'title']),
               CHILDREN: set([str])},
    script  : {VALID: set(['charset', 'type', 'language', 'src', 'defer', 'event', 'for']),
               CHILDREN: set([str])},
    noscript: {VALID: ATTRS,
               CHILDREN: FLOW},
    
    #DOCUMENT STRUCTURE
    html: {VALID: I18N | set(['version']), CHILDREN: set([head, body])},
}
