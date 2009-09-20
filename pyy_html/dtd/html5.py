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

#Attributes
GLOBAL = set(['accesskey', 'class', 'class', 'contenteditable', 'contextmenu', 'dir', 'draggable', 'id', 'item', 'hidden', 'lang', 'itemprop', 'spellcheck', 'style', 'subject', 'tabindex', 'title'])
EVENTS = set(['onabort', 'onblur', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'oncontextmenu', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'onformchange', 'onforminput', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange', 'onreadystatechange', 'onscroll', 'onseeked', 'onseeking', 'onselect', 'onshow', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate', 'onvolumechange', 'onwaiting'])

#Elements
METADATA    = set([base, command, link, meta, noscript, script, style, title])
FLOW        = set([a, abbr, address, area, article, aside, audio, b, bdo, blockquote, br, button, canvas, cite, code, command, datalist, del_, details, dfn, dialog, div, dl, em, embed, fieldset, figure, footer, form, h1, h2, h3, h4, h5, h6, header, hgroup, hr, i, iframe, img, input, ins, kbd, keygen, label, link, map, mark, math, menu, meta, meter, nav, noscript, object, ol, output, p, pre, progress, q, ruby, samp, script, section, select, small, span, strong, style, sub, sup, svg, table, textarea, time, ul, var, video, str])
SECTION     = set([article, aside, nav, section])
HEADING     = set([h1, h2, h3, h4, h5, h6, hgroup])
PHRASING    = set([a, abbr, area, audio, b, bdo, br, button, canvas, cite, code, command, datalist, del_, dfn, em, embed, i, iframe, img, input, ins, kbd, keygen, label, link, map, mark, math, meta, meter, noscript, object, output, progress, q, ruby, samp, script, select, small, span, strong, sub, sup, svg, textarea, time, var, video, str])
TRANSPARENT = set([a, audio, canvas, del_, ins, map_, noscript, object_, video, str])


class html5(dtd):
  docstring = '<!DOCTYPE html>'
  
  valid = {
    #ROOT: http://www.w3.org/TR/html5/semantics.html#the-root-element
    html: {VALID: GLOBAL | set(['manifest']), CHILDREN: set([head, body])},
    
    #METADATA: http://www.w3.org/TR/html5/semantics.html#document-metadata
    head : {VALID   : GLOBAL,
            CHILDREN: METADATA},
    title: {VALID   : GLOBAL,
            CHILDREN: set([str])},
    base : {VALID   : GLOBAL | set(['href', 'target']),
            CUSTOM  : lambda self: 'href' in self.attributes or 'target' in self.attributes},
    link : {VALID   : GLOBAL | set(['href', 'rel', 'media', 'hreflang', 'type', 'sizes']),
            REQUIRED: set(['href'])},
    
    #TODO: "If either name, http-equiv, or itemprop is specified, then the content attribute must also be specified. Otherwise, it must be omitted."
    meta : {VALID   : GLOBAL | set(['name', 'http-equiv', 'content', 'charset']),
            CUSTOM  : lambda self: 'name' in self.attributes ^ 'http-equiv' in self.attributes ^ \
                                   'content' in self.attributes ^ 'charset' in self.attributes},
    style: {VALID   : GLOBAL | set(['media', 'type', 'scoped']),
            CHILDREN: set([str])},
    
    #SCRIPTING: http://www.w3.org/TR/html5/semantics.html#scripting-1
    script  : {VALID   : GLOBAL | set(['src', 'async', 'defer', 'type', 'charset']),
               #Empty if src defined, str otherwise
               CUSTOM  : lambda self: ('src' in self.attributes and not self.children) or \
                                      ('src' not in self.attributes and all(isinstance(child, str) for child in self.children))},
    noscript: {VALID   : GLOBAL,
               CHILDREN: set([])}, # <--TODO http://www.w3.org/TR/html5/semantics.html#the-noscript-element
    
    #SECTIONS: http://www.w3.org/TR/html5/semantics.html#sections
    body   : {VALID   : GLOBAL | set(['onafterprint', 'onbeforeprint', 'onbeforeunload', 'onblur', 'onerror', 'onfocus', 'onhashchange', 'onload', 'onmessage', 'onoffline', 'ononline', 'onpopstate', 'onredo', 'onresize', 'onstorage', 'onundo', 'onunload']),
              CHILDREN: FLOW},
    section: {VALID   : GLOBAL,
              CHILDREN: FLOW},
    nav    : {VALID   : GLOBAL,
              CHILDREN: FLOW},
    article: {VALID   : GLOBAL | set(['pubdate']),
              CHILDREN: FLOW},
    aside  : {VALID   : GLOBAL,
              CHILDREN: FLOW},
    h1     : {VALID   : GLOBAL,
              CHILDREN: PHRASING},
    h2     : {VALID   : GLOBAL,
              CHILDREN: PHRASING},
    h3     : {VALID   : GLOBAL,
              CHILDREN: PHRASING},
    h4     : {VALID   : GLOBAL,
              CHILDREN: PHRASING},
    h5     : {VALID   : GLOBAL,
              CHILDREN: PHRASING},
    h6     : {VALID   : GLOBAL,
              CHILDREN: PHRASING},
    hgroup : {VALID   : GLOBAL,
              CHILDREN: set([h1, h2, h3, h4, h5, h6])},
    header : {VALID   : GLOBAL,
              CHILDREN: FLOW ^ set([header, footer])},
    footer : {VALID   : GLOBAL,
              CHILDREN: FLOW ^ set([header, footer])},
    address: {VALID   : GLOBAL,
              CHILDREN: FLOW ^ (SECTION | HEADING | set([header, footer, address]))},
    
    #GROUPING: http://www.w3.org/TR/html5/semantics.html#grouping-content
    p         : {VALID   : GLOBAL,
                 CHILDREN: PHRASING},
    hr        : {VALID   : GLOBAL},
    br        : {VALID   : GLOBAL},
    pre       : {VALID   : GLOBAL,
                 CHILDREN: PHRASING},
    dialog    : {VALID   : GLOBAL,
                 CHILDREN: set([dt, dd])},
    blockquote: {VALID   : GLOBAL | set(['cite']),
                 CHILDREN: FLOW},
    ol        : {VALID   : GLOBAL | set(['reversed', 'start']),
                 CHILDREN: set([li])},
    ul        : {VALID   : GLOBAL,
                 CHILDREN: set([li])},
    li        : {VALID   : GLOBAL | set(['value']),
                 CHILDREN: FLOW},
    dl        : {VALID   : GLOBAL,
                 CHILDREN: set([dt, dd])},
    dt        : {VALID   : GLOBAL,
                 CHILDREN: PHRASING},
    dd        : {VALID   : GLOBAL,
                 CHILDREN: PHRASING},
    
    #TEXT: http://www.w3.org/TR/html5/text-level-semantics.html#text-level-semantics
    a       : {VALID   : GLOBAL | set(['href', 'target', 'ping', 'rel', 'media', 'hreflang', 'type']),
               CHILDREN: TRANSPARENT},
    em      : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    strong  : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    small   : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    cite    : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    q       : {VALID   : GLOBAL | set(['cite']),
               CHILDREN: PHRASING},
    dfn     : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    abbr    : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    code    : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    var     : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    samp    : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    kbd     : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    sub     : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    sup     : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    i       : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    b       : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    mark    : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    progress: {VALID   : GLOBAL | set(['value', 'max']),
               CHILDREN: PHRASING},
    meter   : {VALID   : GLOBAL | set(['value', 'min', 'low', 'high', 'max', 'optimum']),
               CHILDREN: PHRASING},
    time    : {VALID   : GLOBAL | set(['datetime']),
               CHILDREN: PHRASING},
    ruby    : {VALID   : GLOBAL,
               CHILDREN: PHRASING | set([rt, rp])},
    rt      : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    rp      : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    bdo     : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    span    : {VALID   : GLOBAL,
               CHILDREN: PHRASING},
    
    #EDITS: http://www.w3.org/TR/html5/text-level-semantics.html#edits
    ins : {VALID: GLOBAL | set(['cite', 'datetime']), CHILDREN: TRANSPARENT},
    del_: {VALID: GLOBAL | set(['cite', 'datetime']), CHILDREN: TRANSPARENT},
    
    #EMBEDDED: http://www.w3.org/TR/html5/text-level-semantics.html#embedded-content-1
    figure: {VALID   : GLOBAL,
             CHILDREN: FLOW | set([legend])},
    img   : {VALID   : GLOBAL | set(['alt', 'src', 'usemap', 'ismap', 'width', 'height']),
             REQUIRED: set(['src'])},
    iframe: {VALID   : GLOBAL | set(['src', 'name', 'sandbox', 'seamless', 'width', 'height']),
             CHILDREN: set([str])},
    embed : {VALID   : GLOBAL | set(['src', 'type', 'width', 'height'])},
    object: {VALID   : GLOBAL | set(['data', 'type', 'name', 'usemap', 'form', 'width', 'height']),
             CHILDREN: TRANSPARENT | set([param])},
    param : {VALID   : GLOBAL | set(['name', 'value'])},
    video : {VALID   : GLOBAL | set(['src', 'poster', 'autobuffer', 'autoplay', 'loop', 'controls', 'width', 'height']),
             CHILDREN: TRANSPARENT | set([source])},
    audio : {VALID   : GLOBAL | set(['src', 'autobuffer', 'autoplay', 'loop', 'controls']),
             CHILDREN: TRANSPARENT | set([source])},
    source: {VALID   : GLOBAL | set(['src', 'type', 'media']),
             REQUIRED: set(['src'])},
    canvas: {VALID   : GLOBAL | set(['width', 'height']),
             CHILDREN: TRANSPARENT},
    map   : {VALID   : GLOBAL | set(['name']),
             CHILDREN: TRANSPARENT | set([area])},
    area  : {VALID   : GLOBAL | set(['alt', 'coords', 'shape', 'href', 'target', 'ping', 'rel', 'media', 'hreflang', 'type'])},
    
    #TABULAR: http://www.w3.org/TR/html5/tabular-data.html#tabular-data
    table   : {VALID   : GLOBAL | set(['summary']),
               CHILDREN: set([caption, colgroup, thead, tbody, tr, tfoot])},
    caption : {VALID   : GLOBAL,
               CHILDREN: FLOW},
    colgroup: {VALID   : GLOBAL | set(['span']),
               CHILDREN: set([col])},
    col     : {VALID   : GLOBAL | set(['span'])},
    tbody   : {VALID   : GLOBAL,
               CHILDREN: set([tr])},
    thead   : {VALID   : GLOBAL,
               CHILDREN: set([tr])},
    tfoot   : {VALID   : GLOBAL,
               CHILDREN: set([tr])},
    tr      : {VALID   : GLOBAL,
               CHILDREN: set([th, td])},
    td      : {VALID   : GLOBAL | set(['colspan', 'rowspan', 'headers']),
               CHILDREN: FLOW},
    th      : {VALID   : GLOBAL | set(['colspan', 'rowspan', 'headers', 'scope']),
               CHILDREN: PHRASING},
    
    #FORMS: http://www.w3.org/TR/html5/forms.html#forms
    form    : {VALID   : GLOBAL | set(['accept-charset', 'action', 'autocomplete', 'enctype', 'method', 'name', 'novalidate', 'target']),
               CHILDREN: FLOW},
    fieldset: {VALID   : GLOBAL | set(['disabled', 'form', 'name']),
               CHILDREN: FLOW | set([legend])},
    label   : {VALID   : GLOBAL | set(['form', 'for']),
               CHILDREN: PHRASING},
    input   : {VALID   : GLOBAL | set(['accept', 'alt', 'autocomplete', 'autofocus', 'checked', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'height', 'list', 'max', 'maxlength', 'min', 'multiple', 'name', 'pattern', 'placeholder', 'readonly', 'required', 'size', 'src', 'step', 'type', 'value', 'width'])},
    button  : {VALID   : GLOBAL | set(['autofocus', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'name', 'type', 'value']),
               CHILDREN: PHRASING},
    select  : {VALID   : GLOBAL | set(['autofocus', 'disabled', 'form', 'multiple', 'name', 'size']),
               CHILDREN: set([option, optgroup])},
    datalist: {VALID   : GLOBAL,
               CHILDREN: PHRASING | set([option])},
    optgroup: {VALID   : GLOBAL | set(['disabled', 'label']),
               CHILDREN: set([option])},
    option  : {VALID   : GLOBAL | set(['disabled', 'label', 'selected', 'value']),
               CHILDREN: set([str])},
    textarea: {VALID   : GLOBAL | set(['autofocus', 'cols', 'disabled', 'form', 'maxlength', 'name', 'placeholder', 'readonly', 'required', 'rows', 'warp']),
               CHILDREN: set([str])},
    keygen  : {VALID   : GLOBAL | set(['autofocus', 'challenge', 'disabled', 'form', 'keytype', 'name'])},
    output  : {VALID   : GLOBAL | set(['for', 'form', 'name']),
               CHILDREN: PHRASING},
    
    #INTERACTIVE: http://www.w3.org/TR/html5/interactive-elements.html#interactive-elements
    details: {VALID: GLOBAL | set(['open']), CHILDREN: FLOW | set([legend])},
    command: {VALID: GLOBAL | set(['type', 'label', 'icon', 'disabled', 'checked', 'radiogroup'])},
    menu   : {VALID: GLOBAL | set(['type', 'label']), CHILDREN: FLOW | set([li])},
    
    #MISC: http://www.w3.org/TR/html5/interactive-elements.html#miscellaneous-elements
    legend: {VALID: GLOBAL, CHILDREN: FLOW | PHRASING},
    div   : {VALID: GLOBAL, CHILDREN: FLOW},
}
