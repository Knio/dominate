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

#Attributes
GLOBAL = set(['accesskey', 'class', 'class', 'contenteditable', 'contextmenu', 'dir', 'draggable', 'id', 'item', 'hidden', 'lang', 'itemprop', 'spellcheck', 'style', 'subject', 'tabindex', 'title']
EVENTS = set(['onabort', 'onblur', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick', 'oncontextmenu', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter', 'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange', 'onemptied', 'onended', 'onerror', 'onfocus', 'onformchange', 'onforminput', 'oninput', 'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata', 'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel', 'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange', 'onreadystatechange', 'onscroll', 'onseeked', 'onseeking', 'onselect', 'onshow', 'onstalled', 'onsubmit', 'onsuspend', 'ontimeupdate', 'onvolumechange', 'onwaiting'])

#Elements
METADATA    = set([base, command, link, meta, noscript, script, style, title])
FLOW        = set([a, abbr, address, area, article, aside, audio, b, bdo, blockquote, br, button, canvas, cite, code, command, datalist, del_, details, dfn, dialog, div, dl, em, embed, fieldset, figure, footer, form, h1, h2, h3, h4, h5, h6, header, hgroup, hr, i, iframe, img, input, ins, kbd, keygen, label, link, map, mark, math, menu, meta, meter, nav, noscript, object, ol, output, p, pre, progress, q, ruby, samp, script, section, select, small, span, strong, style, sub, sup, svg, table, textarea, time, ul, var, video, str])
SECTION     = set([article, aside, nav, section])
HEADING     = set([h1, h2, h3, h4, h5, h6, hgroup])
PHRASING    = set([a, abbr, area, audio, b, bdo, br, button, canvas, cite, code, command, datalist, del_, dfn, em, embed, i, iframe, img, input, ins, kbd, keygen, label, link, map, mark, math, meta, meter, noscript, object, output, progress, q, ruby, samp, script, select, small, span, strong, sub, sup, svg, textarea, time, var, video, str])
TRANSPARENT = set([]) #I don't know...ask html5


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
    body   : {},
    section: {},
    nav    : {},
    article: {},
    aside  : {},
    h1     : {},
    h2     : {},
    h3     : {},
    h4     : {},
    h5     : {},
    h6     : {},
    hgroup : {},
    header : {},
    footer : {},
    address: {},
    
    #GROUPING: http://www.w3.org/TR/html5/semantics.html#grouping-content
    p         : {},
    hr        : {},
    br        : {},
    pre       : {},
    dialog    : {},
    blockquote: {},
    ol        : {},
    ul        : {},
    li        : {},
    dl        : {},
    dt        : {},
    dd        : {},
    
    #TEXT: http://www.w3.org/TR/html5/text-level-semantics.html#text-level-semantics
    a       : {},
    em      : {},
    strong  : {},
    small   : {},
    cite    : {},
    q       : {},
    dfn     : {},
    abbr    : {},
    code    : {},
    var     : {},
    samp    : {},
    kbd     : {},
    sub     : {},
    sup     : {},
    i       : {},
    b       : {},
    mark    : {},
    progress: {},
    meter   : {},
    time    : {},
    ruby    : {},
    rt      : {},
    rp      : {},
    bdo     : {},
    span    : {},
    
    #EDITS: http://www.w3.org/TR/html5/text-level-semantics.html#edits
    ins : {VALID: GLOBAL | set(['cite', 'datetime']), CHILDREN: TRANSPARENT},
    del_: {VALID: GLOBAL | set(['cite', 'datetime']), CHILDREN: TRANSPARENT},
    
    #EMBEDDED: http://www.w3.org/TR/html5/text-level-semantics.html#embedded-content-1
    figure: {},
    img   : {},
    iframe: {},
    embed : {},
    object: {},
    param : {},
    video : {},
    audio : {},
    source: {},
    canvas: {},
    map   : {},
    area  : {},
    
    #TABULAR: http://www.w3.org/TR/html5/tabular-data.html#tabular-data
    table   : {},
    caption : {},
    colgroup: {},
    col     : {},
    tbody   : {},
    thead   : {},
    tfoot   : {},
    tr      : {},
    td      : {},
    th      : {},
    
    #FORMS: http://www.w3.org/TR/html5/forms.html#forms
    form    : {},
    fieldset: {},
    label   : {},
    input   : {},
    button  : {},
    select  : {},
    datalist: {},
    optgroup: {},
    option  : {},
    textarea: {},
    keygen  : {},
    output  : {},
    
    #INTERACTIVE: http://www.w3.org/TR/html5/interactive-elements.html#interactive-elements
    details: {VALID: GLOBAL | set(['open']), CHILDREN: FLOW | set([legend])},
    command: {VALID: GLOBAL | set(['type', 'label', 'icon', 'disabled', 'checked', 'radiogroup'])},
    menu   : {VALID: GLOBAL | set(['type', 'label']), CHILDREN: FLOW | set([li])},
    
    #MISC: http://www.w3.org/TR/html5/interactive-elements.html#miscellaneous-elements
    legend: {VALID: GLOBAL, CHILDREN: FLOW | PHRASING},
    div   : {VALID: GLOBAL, CHILDREN: FLOW},
}
