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

from html import html_tag, single, ugly, basepage

COMMON_CORE  = ['class', 'id', 'style', 'title']
COMMON_I18N  = ['lang', 'dir']
COMMON_EVENT = ['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup']
COMMON       = COMMON_CORE + COMMON_I18N + COMMON_EVENT


class html(html_tag): valid = COMMON_I18N
class head(html_tag): valid = ['profile'] + COMMON_I18N
class title(html_tag): valid = COMMON_I18N
class meta(single):
    valid    = ['http-equiv', 'name', 'content', 'scheme'] + COMMON_I18N
    required = ['content']
class body(html_tag): valid = ['onload', 'onunload'] + COMMON

class bdo(html_tag):
    valid    = ['lang', 'dir'] + COMMON_CORE
    required = ['dir']

class div(html_tag): valid = COMMON
class span(html_tag): valid = COMMON

class h1(html_tag): valid = COMMON
class h2(html_tag): valid = COMMON
class h3(html_tag): valid = COMMON
class h4(html_tag): valid = COMMON
class h5(html_tag): valid = COMMON
class h6(html_tag): valid = COMMON

class address(html_tag): valid = COMMON

class em(html_tag): valid = COMMON
class strong(html_tag): valid = COMMON
class dfn(html_tag): valid = COMMON
class code(html_tag): valid = COMMON
class samp(html_tag): valid = COMMON
class kbd(html_tag): valid = COMMON
class var(html_tag): valid = COMMON
class cite(html_tag): valid = COMMON
class abbr(html_tag): valid = COMMON
class acronym(html_tag): valid = COMMON

class blockquote(html_tag): valid = ['cite'] + COMMON
class q(html_tag): valid = ['cite'] + COMMON

class sub(html_tag): valid = COMMON
class sup(html_tag): valid = COMMON

class p(html_tag): valid = COMMON

class br(single): valid = COMMON_CORE

class pre(ugly): valid = COMMON

class ins(html_tag): valid = ['cite', 'datetime'] + COMMON
class _del(html_tag): valid = ['cite', 'datetime'] + COMMON

class ul(html_tag): valid = COMMON
class ol(html_tag): valid = COMMON
class li(html_tag): valid = COMMON
class dl(html_tag): valid = COMMON
class dt(html_tag): valid = COMMON
class dd(html_tag): valid = COMMON

class table(html_tag): valid = ['summary', 'width', 'border', 'frame', 'rules', 'cellspacing', 'cellpadding'] + COMMON
class caption(html_tag): valid = COMMON
class thead(html_tag): valid = ['align', 'char', 'charoff', 'valign'] + COMMON
class tbody(html_tag): valid = ['align', 'char', 'charoff', 'valign'] + COMMON
class tfoot(html_tag): valid = ['align', 'char', 'charoff', 'valign'] + COMMON
class colgroup(html_tag): valid = ['span', 'width', 'align', 'char', 'charoff', 'valign'] + COMMON
class col(html_tag): valid = ['span', 'width', 'align', 'char', 'charoff', 'valign'] + COMMON
class tr(html_tag): valid = ['align', 'char', 'charoff', 'valign'] + COMMON
class td(html_tag): valid = ['abbr', 'axis', 'headers', 'scope', 'rowspan', 'colspan', 'align', 'char', 'charoff', 'valign'] + COMMON
class th(html_tag): valid = ['abbr', 'axis', 'headers', 'scope', 'rowspan', 'colspan', 'align', 'char', 'charoff', 'valign'] + COMMON

class a(html_tag): valid = ['charset', 'type', 'name', 'href', 'hreflang', 'rel', 'rev', 'accesskey', 'shape', 'coords', 'tabindex', 'onfocus', 'onblur'] + COMMON
class link(single): valid = ['charset', 'href', 'hreflang', 'type', 'rel', 'rev', 'media'] + COMMON
class base(single):
    valid    = ['href']
    required = ['href']

class img(single):
    valid    = ['src', 'alt', 'longdesc', 'name', 'height', 'width', 'usemap', 'ismap'] + COMMON
    required = ['src', 'alt']
    default  = {'alt': ''}
class _object(html_tag): valid = ['declare', 'classid', 'codebase', 'data', 'type', 'codetype', 'archive', 'standby', 'height', 'width', 'usemap', 'name', 'tabindex'] + COMMON
class param(single):
    valid    = ['id', 'name', 'value', 'valuetype', 'type']
    required = ['name']
class _map(html_tag):
    valid    = ['name'] + COMMON
    required = ['name']
class area(single):
    valid    = ['shape', 'coords', 'href', 'nohref', 'alt', 'tabindex', 'accesskey', 'onfocus', 'onblur'] + COMMON
    required = ['alt']
    default  = {'alt': ''}

class style(html_tag):
    valid    = ['type', 'media', 'title'] + COMMON
    required = ['type']

class tt(html_tag): valid = COMMON
class i(html_tag): valid = COMMON
class b(html_tag): valid = COMMON
class big(html_tag): valid = COMMON
class small(html_tag): valid = COMMON
class strike(html_tag): valid = COMMON
class s(html_tag): valid = COMMON
class u(html_tag): valid = COMMON
class hr(single): valid = COMMON

class form(html_tag):
    valid    = ['action', 'method', 'enctype', 'accept', 'name', 'onsubmit', 'onreset', 'accept-charset'] + COMMON
    required = ['action']
class _input(single): valid = ['type', 'name', 'value', 'checked', 'disabled', 'readonly', 'size', 'maxlength', 'src', 'alt', 'usemap', 'ismap', 'tabindex', 'accesskey', 'onfocus', 'onblur', 'onselect', 'onchange', 'accept'] + COMMON
class button(single): valid = ['name', 'value', 'type', 'disabled', 'tabindex', 'accesskey', 'onfocus', 'onblur'] + COMMON
class select(html_tag): valid = ['name', 'size', 'multiple', 'disabled', 'tabindex', 'onfocus', 'onblur', 'onchange'] + COMMON
class optgroup(html_tag): valid = ['disabled', 'label'] + COMMON
class option(single): valid = ['selected', 'disabled', 'label', 'value'] + COMMON
class textarea(html_tag):
    valid    = ['name', 'rows', 'cols', 'disabled', 'readonly', 'tabindex', 'accesskey', 'onfocus', 'onblur', 'onselect', 'onchange'] + COMMON
    required = ['rows', 'cols']
class label(html_tag): valid = ['for', 'accesskey', 'onfocus', 'onblur'] + COMMON
class fieldset(html_tag): valid = COMMON
class legend(html_tag): valid = ['accesskey'] + COMMON

class script(ugly):
    valid    = ['charset', 'type', 'src', 'defer']
    required = ['type']
class noscript(html_tag): valid = COMMON

###############################################################################

class htmlpage(basepage):
    def __init__(self, title='HTML 4.01 Strict Page'):
        basepage.__init__(self, title)
        
        self.doctype = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
        self.html    = html()
        self.html.head, self.html.body = self.html.add(head(), body())
