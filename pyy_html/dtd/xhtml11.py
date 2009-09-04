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

from pyy_html.html     import *
from pyy_html.document import document

COMMON_CORE  = ['class', 'id', 'title']
COMMON_I18N  = ['xml:lang', 'dir']
COMMON_EVENT = ['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup']
COMMON_STYLE = ['style']
COMMON       = COMMON_CORE + COMMON_I18N + COMMON_EVENT + COMMON_STYLE

valid = {
    #Structure & Header
    base:   {'valid'   : ['href'],
             'required': ['href']},
    body:   {'valid'   : COMMON + ['onload', 'onunload']},
    head:   {'valid'   : COMMON_I18N + ['profile']},
    html:   {'valid'   : COMMON_I18N + ['xmlns', 'xml:lang', 'xmlns:xsi', 'xsi:schemaLocation', 'version'],
             'required': ['xmlns'],
             'default' : {'xmlns': 'http://www.w3.org/1999/xhtml'}},
    link:   {'valid'   : COMMON + ['href', 'media', 'type', 'charset', 'hreflang', 'rel', 'rev']},
    meta:   {'valid'   : COMMON_I18N + ['content', 'name', 'http-equiv', 'scheme'],
             'required': ['name']},
    script: {'valid'   : COMMON + ['src', 'type', 'charset', 'defer', 'xml:space'],
             'required': ['type']},
    style:  {'valid'   : COMMON_I18N + ['media', 'title', 'type', 'xml:space'],
             'required': ['type']},
    title:  {'valid'   : COMMON_I18N},

    #Block elements
    address   : {'valid': COMMON},
    blockquote: {'valid': COMMON + ['cite']},
    _del      : {'valid': COMMON + ['cite', 'datetime']},
    div       : {'valid': COMMON},
    dl        : {'valid': COMMON},
    fieldset  : {'valid': COMMON},
    form      : {'valid': COMMON + ['action', 'method', 'accept', 'accept-charsets', 'enctype', 'onreset', 'onsubmit']},
    h1        : {'valid': COMMON},
    h2        : {'valid': COMMON},
    h3        : {'valid': COMMON},
    h4        : {'valid': COMMON},
    h5        : {'valid': COMMON},
    h6        : {'valid': COMMON},
    hr        : {'valid': COMMON},
    ins       : {'valid': COMMON + ['cite', 'datetime']},
    noscript  : {'valid': COMMON},
    ol        : {'valid': COMMON},
    p         : {'valid': COMMON},
    pre       : {'valid': COMMON + ['xml:space']},
    table     : {'valid': COMMON + ['border', 'cellpadding', 'cellspacing', 'summary', 'width', 'frame', 'rules']},
    ul        : {'valid': COMMON},
    
    #Inline elements
    a:        {'valid'   : COMMON + ['href', 'accesskey', 'charset', 'coords', 'hreflang', 'onblur', 'onfocus', 'rel', 'rev', 'shape', 'tabindex', 'type']},
    abbr:     {'valid'   : COMMON},
    acronym:  {'valid'   : COMMON},
    b:        {'valid'   : COMMON},
    bdo:      {'valid'   : COMMON + ['dir']},
    big:      {'valid'   : COMMON},
    br:       {'valid'   : COMMON},
    button:   {'valid'   : COMMON + ['name', 'type', 'value', 'accesskey', 'disabled', 'onblur', 'onfocus', 'tabindex']},
    cite:     {'valid'   : COMMON},
    code:     {'valid'   : COMMON},
    dfn:      {'valid'   : COMMON},
    em:       {'valid'   : COMMON},
    i:        {'valid'   : COMMON},
    img:      {'valid'   : COMMON + ['alt', 'height', 'src', 'width', 'ismap', 'longdesc', 'usemap'],
               'required': ['alt', 'src'],
               'default' : {'alt': ''}},
    _input:   {'valid'   : COMMON + ['alt', 'checked', 'maxlength', 'name', 'size', 'type', 'value', 'accept', 'accesskey', 'disabled', 'ismap', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'src', 'tabindex', 'usemap']},
    kbd:      {'valid'   : COMMON},
    label:    {'valid'   : COMMON + ['for', 'accesskey', 'onblur', 'onfocus']},
    _map:     {'valid'   : COMMON},
    _object:  {'valid'   : COMMON + ['classid', 'codebase', 'height', 'name', 'type', 'width', 'archive', 'codetype', 'data', 'declare', 'standby', 'tabindex', 'usemap']},
    q:        {'valid'   : COMMON + ['cite']},
    ruby:     {'valid'   : COMMON},
    samp:     {'valid'   : COMMON},
    select:   {'valid'   : COMMON + ['multiple', 'name', 'size', 'disabled', 'onblur', 'onchange', 'onfocus', 'tabindex']},
    small:    {'valid'   : COMMON},
    span:     {'valid'   : COMMON},
    strong:   {'valid'   : COMMON},
    sub:      {'valid'   : COMMON},
    sup:      {'valid'   : COMMON},
    textarea: {'valid'   : CPMMON + ['cols', 'name', 'rows', 'accesskey', 'disabled', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'tabindex']},
    tt:       {'valid'   : COMMON},
    var:      {'valid'   : COMMON},
    
    #List item elements
    dd: {'valid': COMMON},
    dt: {'valid': COMMON},
    li: {'valid': COMMON},
    
    #Table content elements
    caption:  {'valid': COMMON},
    col:      {'valid': COMMON + ['align', 'span', 'valign', 'width', 'char', 'charoff']},
    colgroup: {'valid': COMMON + ['align', 'span', 'valign', 'width', 'char', 'charoff']},
    tbody:    {'valid': COMMON + ['align', 'valign', 'char', 'charoff']},
    td:       {'valid': COMMON + ['align', 'colspan', 'headers', 'rowspan', 'valign', 'axis', 'char', 'charoff']},
    tfoot:    {'valid': COMMON + ['align', 'valign', 'char', 'charoff']},
    th:       {'valid': COMMON + ['abbr', 'align', 'colspan', 'rowspan', 'valign', 'axis', 'char', 'charoff', 'scope']},
    thead:    {'valid': COMMON + ['align', 'valign', 'char', 'charoff']},
    tr:       {'valid': COMMON + ['align', 'valign', 'char', 'charoff']},
    
    #Form fieldset legends
    legend: {'valid': ['accesskey'] + COMMON},
    
    #Form menu options
    optgroup: {'valid': ['label', 'disabled'] + COMMON},
    option:   {'valid': ['selected', 'value', 'disabled', 'label'] + COMMON},
    
    #Map areas
    area: {'valid'   : COMMON + ['alt', 'coords', 'href', 'shape', 'accesskey', 'onblur', 'onfocus', 'nohref', 'tabindex'],
           'required': ['alt'],
           'default' : {'alt': ''}},
    
    #Object parameters
    param: {'valid'   : ['name', 'value', 'id', 'type', 'valuetype'],
            'required': ['name']},
    
    #Ruby annotations
    rb : {'valid': COMMON},
    rbc: {'valid': COMMON},
    rp : {'valid': COMMON},
    rt : {'valid': COMMON + ['rbspan']},
    rtc: {'valid': COMMON},
}
