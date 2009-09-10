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

COMMON_CHILDREN = [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]
valid = {
    #Structure & Header
    base:   {'valid'   : ['href'],
             'required': ['href']},
    body:   {'valid'   : COMMON + ['onload', 'onunload']
             'children': [address, blockquote, del_, div, fieldset, form, hr, ins, noscript, p, pre, script, table, h1, h2, h3, h4, h5, h6, dl, ol, ul]},
    head:   {'valid'   : COMMON_I18N + ['profile']
             'children': [base, link, meta, object_, script, style, title]},
    html:   {'valid'   : COMMON_I18N + ['xmlns', 'xml:lang', 'xmlns:xsi', 'xsi:schemaLocation', 'version'],
             'required': ['xmlns'],
             'default' : {'xmlns': 'http://www.w3.org/1999/xhtml'}
             'children': [head, body]},
    link:   {'valid'   : COMMON + ['href', 'media', 'type', 'charset', 'hreflang', 'rel', 'rev']},
    meta:   {'valid'   : COMMON_I18N + ['content', 'name', 'http-equiv', 'scheme'],
             'required': ['name']},
    script: {'valid'   : COMMON + ['src', 'type', 'charset', 'defer', 'xml:space'],
             'required': ['type']},
    style:  {'valid'   : COMMON_I18N + ['media', 'title', 'type', 'xml:space'],
             'required': ['type']},
    title:  {'valid'   : COMMON_I18N},

    #Block elements
    address   : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    blockquote: {'valid'   : COMMON + ['cite']
                 'children': [address, blockquote, del_, div, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    _del      : {'valid'   : COMMON + ['cite', 'datetime']
                 'children': [a, abbr, acronym, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    div       : {'valid'   : COMMON
                 'children': [a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, map, textarea, tt, ul, var]},
    dl        : {'valid'   : COMMON
                 'children': [dd, dt]},
    fieldset  : {'valid'   : COMMON
                 'children': [a, abbr, acronym, address, b, bdo, big, button, caption, cite, code, dd, del_, dfn, div, dt, em, fieldset, form, h1, h2, h3, h4, h5, h6, i, ins, kdb, label, legend, li, object_, p, pre, q, samp, small, span, strong, sub, sup, td, th, tt, var]},
    form      : {'valid'   : COMMON + ['action', 'method', 'accept', 'accept-charsets', 'enctype', 'onreset', 'onsubmit']
                 'children': [address, blockquote, del_, div, dl, fieldset, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    h1        : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    h2        : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    h3        : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    h4        : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    h5        : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    h6        : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    hr        : {'valid'   : COMMON},
    ins       : {'valid'   : COMMON + ['cite', 'datetime']
                 'children': [a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, ul, var]},
    noscript  : {'valid'   : COMMON
                 'children': [address, blockquote, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    ol        : {'valid'   : COMMON
                 'children': [li]},
    p         : {'valid'   : COMMON
                 'children': COMMON_CHILDREN},
    pre       : {'valid'   : COMMON + ['xml:space']
                 'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, input_, ins, kdb, label, map_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    table     : {'valid'   : COMMON + ['border', 'cellpadding', 'cellspacing', 'summary', 'width', 'frame', 'rules']
                 'children': [caption, col, colgroup, tbody, tfoot, thead, tr]},
    ul        : {'valid'   : COMMON
                 'children': [li]},
    
    #Inline elements
    a:        {'valid'   : COMMON + ['href', 'accesskey', 'charset', 'coords', 'hreflang', 'onblur', 'onfocus', 'rel', 'rev', 'shape', 'tabindex', 'type']
               'children': [abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    abbr:     {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    acronym:  {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    b:        {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    bdo:      {'valid'   : COMMON + ['dir']
               'children': COMMON_CHILDREN},
    big:      {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    br:       {'valid'   : COMMON},
    button:   {'valid'   : COMMON + ['name', 'type', 'value', 'accesskey', 'disabled', 'onblur', 'onfocus', 'tabindex']
               'children': [abbr, acronym, address, b, bdo, big, blockquote, br, cite, code, dd, del_, dfn, div, dl, em, h1, h2, h3, h4, h5, h6, hr, i, img, ins, kbd, map_, noscript, object_, ol, p, pre, q, samp, script, small, span, strong, sub, sup, table, tt, ul, var]},
    cite:     {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    code:     {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    dfn:      {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    em:       {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    i:        {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    img:      {'valid'   : COMMON + ['alt', 'height', 'src', 'width', 'ismap', 'longdesc', 'usemap'],
               'required': ['alt', 'src'],
               'default' : {'alt': ''}},
    _input:   {'valid'   : COMMON + ['alt', 'checked', 'maxlength', 'name', 'size', 'type', 'value', 'accept', 'accesskey', 'disabled', 'ismap', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'src', 'tabindex', 'usemap']},
    kbd:      {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    label:    {'valid'   : COMMON + ['for', 'accesskey', 'onblur', 'onfocus']
               'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    _map:     {'valid'   : COMMON
               'children': [address, area, blockquote, del_, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    _object:  {'valid'   : COMMON + ['classid', 'codebase', 'height', 'name', 'type', 'width', 'archive', 'codetype', 'data', 'declare', 'standby', 'tabindex', 'usemap']
               'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kdb, label, map_, object_, param, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    q:        {'valid'   : COMMON + ['cite']
               'children': COMMON_CHILDREN},
    ruby:     {'valid'   : COMMON
               'children': [rbc, rtc, rb, rt, rp]},
    samp:     {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    select:   {'valid'   : COMMON + ['multiple', 'name', 'size', 'disabled', 'onblur', 'onchange', 'onfocus', 'tabindex']
               'children': [optgroup, option]},
    small:    {'valid'   : COMMON
               'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kdb, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    span:     {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    strong:   {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    sub:      {'valid'   : COMMON
               'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kdb, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    sup:      {'valid'   : COMMON
               'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kdb, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    textarea: {'valid'   : CPMMON + ['cols', 'name', 'rows', 'accesskey', 'disabled', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'tabindex']
               'children': COMMON_CHILDREN},
    tt:       {'valid'   : COMMON
               'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kdb, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    var:      {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    
    #List item elements
    dd: {'valid'   : COMMON
         'children': [a, abbr, acronym, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    dt: {'valid'   : COMMON
         'children': COMMON_CHILDREN},
    li: {'valid'   : COMMON
         'children': [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, map, noscript, ul, var]},
    
    #Table content elements
    caption:  {'valid'   : COMMON
               'children': COMMON_CHILDREN},
    col:      {'valid'   : COMMON + ['align', 'span', 'valign', 'width', 'char', 'charoff']},
    colgroup: {'valid'   : COMMON + ['align', 'span', 'valign', 'width', 'char', 'charoff']
               'children': [col]},
    tbody:    {'valid'   : COMMON + ['align', 'valign', 'char', 'charoff']
               'children': [tr]},
    td:       {'valid'   : COMMON + ['align', 'colspan', 'headers', 'rowspan', 'valign', 'axis', 'char', 'charoff']
               'children': [abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kdb, label, map_, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    tfoot:    {'valid'   : COMMON + ['align', 'valign', 'char', 'charoff']
               'children': [tr]},
    th:       {'valid'   : COMMON + ['abbr', 'align', 'colspan', 'rowspan', 'valign', 'axis', 'char', 'charoff', 'scope']
               'children': [abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kdb, label, map_, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    thead:    {'valid'   : COMMON + ['align', 'valign', 'char', 'charoff']
               'children': [tr]},
    tr:       {'valid'   : COMMON + ['align', 'valign', 'char', 'charoff']
               'children': [td, th]},
    
    #Form fieldset legends
    legend: {'valid'   : ['accesskey'] + COMMON
             'children': COMMON_CHILDREN},
    
    #Form menu options
    optgroup: {'valid'   : ['label', 'disabled'] + COMMON
               'children': [option]},
    option:   {'valid'   : ['selected', 'value', 'disabled', 'label'] + COMMON},
    
    #Map areas
    area: {'valid'   : COMMON + ['alt', 'coords', 'href', 'shape', 'accesskey', 'onblur', 'onfocus', 'nohref', 'tabindex'],
           'required': ['alt'],
           'default' : {'alt': ''}},
    
    #Object parameters
    param: {'valid'   : ['name', 'value', 'id', 'type', 'valuetype'],
            'required': ['name']},
    
    #Ruby annotations
    rb : {'valid'   : COMMON
          'children': [rt]},
    rbc: {'valid'   : COMMON
          'children': [rb]},
    rp : {'valid'   : COMMON
          'children': [rt]},
    rt : {'valid'   : COMMON + ['rbspan']
          'children': [rt]},
    rtc: {'valid'   : COMMON
          'children': [rt]},
}
