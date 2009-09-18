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

CORE   = set(['class', 'id', 'title'])
I18N   = set(['xml:lang', 'dir'])
EVENT  = set(['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup'])
STYLE  = set(['style'])
COMMON = CORE | I18N | EVENT | STYLE

#TODO: rename this, get real children sets from DTD
GLOBAL = set([a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])

class xhtml11(dtd):
  docstring =  '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"' \
               '    "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
  
  valid = {
    #Structure & Header
    base:   {VALID   : set(['href']),
             REQUIRED: set(['href'])},
    body:   {VALID   : COMMON | set(['onload', 'onunload']),
             CHILDREN: set([address, blockquote, del_, div, fieldset, form, hr, ins, noscript, p, pre, script, table, h1, h2, h3, h4, h5, h6, dl, ol, ul])},
    head:   {VALID   : I18N | set(['profile']),
             CHILDREN: set([base, link, meta, object_, script, style, title])},
    html:   {VALID   : I18N | set(['xmlns', 'xml:lang', 'xmlns:xsi', 'xsi:schemaLocation', 'version']),
             REQUIRED: set(['xmlns']),
             DEFAULT : {'xmlns': 'http://www.w3.org/1999/xhtml'},
             CHILDREN: set([head, body])},
    link:   {VALID   : COMMON | set(['href', 'media', 'type', 'charset', 'hreflang', 'rel', 'rev'])},
    meta:   {VALID   : I18N | set(['content', 'name', 'http-equiv', 'scheme']),
             REQUIRED: set(['name'])},
    script: {VALID   : COMMON | set(['src', 'type', 'charset', 'defer', 'xml:space']),
             REQUIRED: set(['type'])},
    style:  {VALID   : I18N | set(['media', 'title', 'type', 'xml:space']),
             REQUIRED: set(['type'])},
    title:  {VALID   : I18N,
             CHILDREN: set([str])},

    #Block elements
    address   : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    blockquote: {VALID   : COMMON | set(['cite']),
                 CHILDREN: set([address, blockquote, del_, div, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul])},
    del_      : {VALID   : COMMON | set(['cite', 'datetime']),
                 CHILDREN: set([a, abbr, acronym, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var])},
    div       : {VALID   : COMMON,
                 CHILDREN: set([str, a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, map, textarea, tt, ul, var])},
    dl        : {VALID   : COMMON,
                 CHILDREN: set([dd, dt])},
    fieldset  : {VALID   : COMMON,
                 CHILDREN: set([a, abbr, acronym, address, b, bdo, big, button, caption, cite, code, dd, del_, dfn, div, dt, em, fieldset, form, h1, h2, h3, h4, h5, h6, i, ins, kbd, label, legend, li, object_, p, pre, q, samp, small, span, strong, sub, sup, td, th, tt, var])},
    form      : {VALID   : COMMON | set(['action', 'method', 'accept', 'accept-charsets', 'enctype', 'onreset', 'onsubmit']),
                 CHILDREN: set([address, blockquote, del_, div, dl, fieldset, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul])},
    h1        : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    h2        : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    h3        : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    h4        : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    h5        : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    h6        : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    hr        : {VALID   : COMMON},
    ins       : {VALID   : COMMON | set(['cite', 'datetime']),
                 CHILDREN: set([a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, ul, var])},
    noscript  : {VALID   : COMMON,
                 CHILDREN: set([address, blockquote, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul])},
    ol        : {VALID   : COMMON,
                 CHILDREN: set([li])},
    p         : {VALID   : COMMON,
                 CHILDREN: GLOBAL},
    pre       : {VALID   : COMMON | set(['xml:space']),
                 CHILDREN: set([a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, input_, ins, kbd, label, map_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])},
    table     : {VALID   : COMMON | set(['border', 'cellpadding', 'cellspacing', 'summary', 'width', 'frame', 'rules']),
                 CHILDREN: set([caption, col, colgroup, tbody, tfoot, thead, tr])},
    ul        : {VALID   : COMMON,
                 CHILDREN: set([li])},
    
    #Inline elements
    a:        {VALID   : COMMON | set(['href', 'accesskey', 'charset', 'coords', 'hreflang', 'onblur', 'onfocus', 'rel', 'rev', 'shape', 'tabindex', 'type']),
               CHILDREN: set([abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])},
    abbr:     {VALID   : COMMON,
               CHILDREN: GLOBAL},
    acronym:  {VALID   : COMMON,
               CHILDREN: GLOBAL},
    b:        {VALID   : COMMON,
               CHILDREN: GLOBAL},
    bdo:      {VALID   : COMMON | set(['dir']),
               CHILDREN: GLOBAL},
    big:      {VALID   : COMMON,
               CHILDREN: GLOBAL},
    br:       {VALID   : COMMON},
    button:   {VALID   : COMMON | set(['name', 'type', 'value', 'accesskey', 'disabled', 'onblur', 'onfocus', 'tabindex']),
               CHILDREN: set([abbr, acronym, address, b, bdo, big, blockquote, br, cite, code, dd, del_, dfn, div, dl, em, h1, h2, h3, h4, h5, h6, hr, i, img, ins, kbd, map_, noscript, object_, ol, p, pre, q, samp, script, small, span, strong, sub, sup, table, tt, ul, var])},
    cite:     {VALID   : COMMON,
               CHILDREN: GLOBAL},
    code:     {VALID   : COMMON,
               CHILDREN: GLOBAL},
    dfn:      {VALID   : COMMON,
               CHILDREN: GLOBAL},
    em:       {VALID   : COMMON,
               CHILDREN: GLOBAL},
    i:        {VALID   : COMMON,
               CHILDREN: GLOBAL},
    img:      {VALID   : COMMON | set(['alt', 'height', 'src', 'width', 'ismap', 'longdesc', 'usemap']),
               REQUIRED: set(['alt', 'src']),
               DEFAULT : {'alt': ''}},
    input_:   {VALID   : COMMON | set(['alt', 'checked', 'maxlength', 'name', 'size', 'type', 'value', 'accept', 'accesskey', 'disabled', 'ismap', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'src', 'tabindex', 'usemap'])},
    kbd:      {VALID   : COMMON,
               CHILDREN: GLOBAL},
    label:    {VALID   : COMMON | set(['for', 'accesskey', 'onblur', 'onfocus']),
               CHILDREN: set([a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, ins, kbd, label, map_, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])},
    map_:     {VALID   : COMMON,
               CHILDREN: set([address, area, blockquote, del_, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, ins, noscript, ol, p, pre, script, table, ul])},
    object_:  {VALID   : COMMON | set(['classid', 'codebase', 'height', 'name', 'type', 'width', 'archive', 'codetype', 'data', 'declare', 'standby', 'tabindex', 'usemap']),
               CHILDREN: set([a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, object_, param, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])},
    q:        {VALID   : COMMON | set(['cite']),
               CHILDREN: GLOBAL},
    ruby:     {VALID   : COMMON,
               CHILDREN: set([rbc, rtc, rb, rt, rp])},
    samp:     {VALID   : COMMON,
               CHILDREN: GLOBAL},
    select:   {VALID   : COMMON | set(['multiple', 'name', 'size', 'disabled', 'onblur', 'onchange', 'onfocus', 'tabindex']),
               CHILDREN: set([optgroup, option])},
    small:    {VALID   : COMMON,
               CHILDREN: set([a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])},
    span:     {VALID   : COMMON,
               CHILDREN: GLOBAL},
    strong:   {VALID   : COMMON,
               CHILDREN: GLOBAL},
    sub:      {VALID   : COMMON,
               CHILDREN: set([a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])},
    sup:      {VALID   : COMMON,
               CHILDREN: set([a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var])},
    textarea: {VALID   : COMMON | set(['cols', 'name', 'rows', 'accesskey', 'disabled', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'tabindex']),
               CHILDREN: GLOBAL},
    tt:       {VALID   : COMMON,
               CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, em, i, img, input_, ins, kbd, label, map_, noscript, object_, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, var]},
    var:      {VALID   : COMMON,
               CHILDREN: GLOBAL},
    
    #List item elements
    dd: {VALID   : COMMON,
         CHILDREN: [a, abbr, acronym, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var]},
    dt: {VALID   : COMMON,
         CHILDREN: GLOBAL},
    li: {VALID   : COMMON,
         CHILDREN: [a, abbr, acronym, b, bdo, big, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, noscript, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, textarea, tt, map, noscript, ul, var]},
    
    #Table content elements
    caption:  {VALID   : COMMON,
               CHILDREN: GLOBAL},
    col:      {VALID   : COMMON | set(['align', 'span', 'valign', 'width', 'char', 'charoff'])},
    colgroup: {VALID   : COMMON | set(['align', 'span', 'valign', 'width', 'char', 'charoff']),
               CHILDREN: set([col])},
    tbody:    {VALID   : COMMON | set(['align', 'valign', 'char', 'charoff']),
               CHILDREN: set([tr])},
    td:       {VALID   : COMMON | set(['align', 'colspan', 'headers', 'rowspan', 'valign', 'axis', 'char', 'charoff']),
               CHILDREN: set([a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var])},
    tfoot:    {VALID   : COMMON | set(['align', 'valign', 'char', 'charoff']),
               CHILDREN: set([tr])},
    th:       {VALID   : COMMON | set(['abbr', 'align', 'colspan', 'rowspan', 'valign', 'axis', 'char', 'charoff', 'scope']),
               CHILDREN: set([a, abbr, acronym, address, b, bdo, big, blockquote, br, button, cite, code, del_, dfn, div, dl, em, fieldset, form, h1, h2, h3, h4, h5, h6, hr, i, img, input_, ins, kbd, label, map_, object_, ol, p, pre, q, samp, script, select, small, span, strong, sub, sup, table, textarea, tt, ul, var])},
    thead:    {VALID   : COMMON | set(['align', 'valign', 'char', 'charoff']),
               CHILDREN: set([tr])},
    tr:       {VALID   : COMMON | set(['align', 'valign', 'char', 'charoff']),
               CHILDREN: set([td, th])},
    
    #Form fieldset legends
    legend: {VALID   : COMMON | set(['accesskey']),
             CHILDREN: GLOBAL},
    
    #Form menu options
    optgroup: {VALID   : COMMON | set(['label', 'disabled']),
               CHILDREN: set([option])},
    option:   {VALID   : COMMON | set(['selected', 'value', 'disabled', 'label'])},
    
    #Map areas
    area: {VALID   : COMMON | set(['alt', 'coords', 'href', 'shape', 'accesskey', 'onblur', 'onfocus', 'nohref', 'tabindex']),
           REQUIRED: set(['alt']),
           DEFAULT : {'alt': ''}},
    
    #Object parameters
    param: {VALID   : set(['name', 'value', 'id', 'type', 'valuetype']),
            REQUIRED: set(['name'])},
    
    #Ruby annotations
    rb : {VALID   : COMMON,
          CHILDREN: set([rt])},
    rbc: {VALID   : COMMON,
          CHILDREN: set([rb])},
    rp : {VALID   : COMMON,
          CHILDREN: set([rt])},
    rt : {VALID   : COMMON | set(['rbspan']),
          CHILDREN: set([rt])},
    rtc: {VALID   : COMMON,
          CHILDREN: set([rt])},
  }

