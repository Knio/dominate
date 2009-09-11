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

from pyy_html.dtd  import *
from pyy_html.html import *

COMMON_CORE  = ['class', 'id', 'title']
COMMON_I18N  = ['xml:lang', 'dir']
COMMON_EVENT = ['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup']
COMMON_STYLE = ['style']
COMMON       = COMMON_CORE + COMMON_I18N + COMMON_EVENT + COMMON_STYLE

COMMON_CHILDREN = [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]

# TODO: is there any way to check if a tag is only allowed 1 child? ie <html> <body></body> <body></body> </html>. does the spec say anything about this?

class xhtml11(dtd):
  def render(self):
    return '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN' \
           '    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'


  valid = {
    #Structure & Header
    base:   {VALID   : ['href'],
             REQUIRED: ['href']},
    body:   {VALID   : COMMON + ['onload', 'onunload'],
             CHILDREN: [address, blockquote, del_, div, fieldset, form, hr, ins, noscript, p, pre, script, table, h1, h2, h3, h4, h5, h6, dl, ol, ul]},
    head:   {VALID   : COMMON_I18N + ['profile'],
             CHILDREN: [base, link, meta, object_, script, style, title]},
    html:   {VALID   : COMMON_I18N + ['xmlns', 'xml:lang', 'xmlns:xsi', 'xsi:schemaLocation', 'version'],
             REQUIRED: ['xmlns'],
             DEFAULT : {'xmlns': 'http://www.w3.org/1999/xhtml'},
             CHILDREN: [head, body]},
    link:   {VALID   : COMMON + ['href', 'media', 'type', 'charset', 'hreflang', 'rel', 'rev']},
    meta:   {VALID   : COMMON_I18N + ['content', 'name', 'http-equiv', 'scheme'],
             REQUIRED: ['name']},
    script: {VALID   : COMMON + ['src', 'type', 'charset', 'defer', 'xml:space'],
             REQUIRED: ['type']},
    style:  {VALID   : COMMON_I18N + ['media', 'title', 'type', 'xml:space'],
             REQUIRED: ['type']},
    title:  {VALID   : COMMON_I18N,
             CHILDREN: [str]},

    #Block elements
    address   : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    blockquote: {VALID   : COMMON + ['cite'],
                 CHILDREN: [address, blockquote, del_, div, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    del_      : {VALID   : COMMON + ['cite', 'datetime'],
                 CHILDREN: [a, abbr, acronym, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    div       : {VALID   : COMMON,
                 CHILDREN: [str, a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, map, textarea, tt, ul, var]},
    dl        : {VALID   : COMMON,
                 CHILDREN: [dd, dt]},
    fieldset  : {VALID   : COMMON,
                 CHILDREN: [a, abbr, acronym, address, b, bdo, big, button, caption, cite, code, dd, del_, dfn, div, dt, em, fieldset, form, h1, h2, h3, h4, h5, h6, i, ins, kbd, label, legend, li, object_, p, pre, q, samp, small, span, strong, sub, sup, td, th, tt, var]},
    form      : {VALID   : COMMON + ['action', 'method', 'accept', 'accept-charsets', 'enctype', 'onreset', 'onsubmit'],
                 CHILDREN: [address, blockquote, del_, div, dl, fieldset, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    h1        : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    h2        : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    h3        : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    h4        : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    h5        : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    h6        : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    hr        : {VALID   : COMMON},
    ins       : {VALID   : COMMON + ['cite', 'datetime'],
                 CHILDREN: [a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, ul, var]},
    noscript  : {VALID   : COMMON,
                 CHILDREN: [address, blockquote, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    ol        : {VALID   : COMMON,
                 CHILDREN: [li]},
    p         : {VALID   : COMMON,
                 CHILDREN: COMMON_CHILDREN},
    pre       : {VALID   : COMMON + ['xml:space'],
                 CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, input_, ins, kbd, label, map_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    table     : {VALID   : COMMON + ['border', 'cellpadding', 'cellspacing', 'summary', 'width', 'frame', 'rules'],
                 CHILDREN: [caption, col, colgroup, tbody, tfoot, thead, tr]},
    ul        : {VALID   : COMMON,
                 CHILDREN: [li]},
    
    #Inline elements
    a:        {VALID   : COMMON + ['href', 'accesskey', 'charset', 'coords', 'hreflang', 'onblur', 'onfocus', 'rel', 'rev', 'shape', 'tabindex', 'type'],
               CHILDREN: [abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    abbr:     {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    acronym:  {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    b:        {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    bdo:      {VALID   : COMMON + ['dir'],
               CHILDREN: COMMON_CHILDREN},
    big:      {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    br:       {VALID   : COMMON},
    button:   {VALID   : COMMON + ['name', 'type', 'value', 'accesskey', 'disabled', 'onblur', 'onfocus', 'tabindex'],
               CHILDREN: [abbr, acronym, address, b, bdo, big, blockquote, br, cite, code, dd, del_, dfn, div, dl, em, h1, h2, h3, h4, h5, h6, hr, i, img, ins, kbd, map_, noscript, object_, ol, p, pre, q, samp, script, small, span, strong, sub, sup, table, tt, ul, var]},
    cite:     {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    code:     {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    dfn:      {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    em:       {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    i:        {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    img:      {VALID   : COMMON + ['alt', 'height', 'src', 'width', 'ismap', 'longdesc', 'usemap'],
               REQUIRED: ['alt', 'src'],
               DEFAULT : {'alt': ''}},
    input_:   {VALID   : COMMON + ['alt', 'checked', 'maxlength', 'name', 'size', 'type', 'value', 'accept', 'accesskey', 'disabled', 'ismap', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'src', 'tabindex', 'usemap']},
    kbd:      {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    label:    {VALID   : COMMON + ['for', 'accesskey', 'onblur', 'onfocus'],
               CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    map_:     {VALID   : COMMON,
               CHILDREN: [address, area, blockquote, del_, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul]},
    object_:  {VALID   : COMMON + ['classid', 'codebase', 'height', 'name', 'type', 'width', 'archive', 'codetype', 'data', 'declare', 'standby', 'tabindex', 'usemap'],
               CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, param, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    q:        {VALID   : COMMON + ['cite'],
               CHILDREN: COMMON_CHILDREN},
    ruby:     {VALID   : COMMON,
               CHILDREN: [rbc, rtc, rb, rt, rp]},
    samp:     {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    select:   {VALID   : COMMON + ['multiple', 'name', 'size', 'disabled', 'onblur', 'onchange', 'onfocus', 'tabindex'],
               CHILDREN: [optgroup, option]},
    small:    {VALID   : COMMON,
               CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    span:     {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    strong:   {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    sub:      {VALID   : COMMON,
               CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    sup:      {VALID   : COMMON,
               CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    textarea: {VALID   : COMMON + ['cols', 'name', 'rows', 'accesskey', 'disabled', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'tabindex'],
               CHILDREN: COMMON_CHILDREN},
    tt:       {VALID   : COMMON,
               CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    var:      {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    
    #List item elements
    dd: {VALID   : COMMON,
         CHILDREN: [a, abbr, acronym, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    dt: {VALID   : COMMON,
         CHILDREN: COMMON_CHILDREN},
    li: {VALID   : COMMON,
         CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, map, noscript, ul, var]},
    
    #Table content elements
    caption:  {VALID   : COMMON,
               CHILDREN: COMMON_CHILDREN},
    col:      {VALID   : COMMON + ['align', 'span', 'valign', 'width', 'char', 'charoff']},
    colgroup: {VALID   : COMMON + ['align', 'span', 'valign', 'width', 'char', 'charoff'],
               CHILDREN: [col]},
    tbody:    {VALID   : COMMON + ['align', 'valign', 'char', 'charoff'],
               CHILDREN: [tr]},
    td:       {VALID   : COMMON + ['align', 'colspan', 'headers', 'rowspan', 'valign', 'axis', 'char', 'charoff'],
               CHILDREN: [a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    tfoot:    {VALID   : COMMON + ['align', 'valign', 'char', 'charoff'],
               CHILDREN: [tr]},
    th:       {VALID   : COMMON + ['abbr', 'align', 'colspan', 'rowspan', 'valign', 'axis', 'char', 'charoff', 'scope'],
               CHILDREN: [a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    thead:    {VALID   : COMMON + ['align', 'valign', 'char', 'charoff'],
               CHILDREN: [tr]},
    tr:       {VALID   : COMMON + ['align', 'valign', 'char', 'charoff'],
               CHILDREN: [td, th]},
    
    #Form fieldset legends
    legend: {VALID   : ['accesskey'] + COMMON,
             CHILDREN: COMMON_CHILDREN},
    
    #Form menu options
    optgroup: {VALID   : ['label', 'disabled'] + COMMON,
               CHILDREN: [option]},
    option:   {VALID   : ['selected', 'value', 'disabled', 'label'] + COMMON},
    
    #Map areas
    area: {VALID   : COMMON + ['alt', 'coords', 'href', 'shape', 'accesskey', 'onblur', 'onfocus', 'nohref', 'tabindex'],
           REQUIRED: ['alt'],
           DEFAULT : {'alt': ''}},
    
    #Object parameters
    param: {VALID   : ['name', 'value', 'id', 'type', 'valuetype'],
            REQUIRED: ['name']},
    
    #Ruby annotations
    rb : {VALID   : COMMON,
          CHILDREN: [rt]},
    rbc: {VALID   : COMMON,
          CHILDREN: [rb]},
    rp : {VALID   : COMMON,
          CHILDREN: [rt]},
    rt : {VALID   : COMMON + ['rbspan'],
          CHILDREN: [rt]},
    rtc: {VALID   : COMMON,
          CHILDREN: [rt]},
  }

