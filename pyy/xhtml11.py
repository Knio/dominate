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

COMMON_CORE  = ['class', 'id', 'title']
COMMON_I18N  = ['xml:lang', 'dir']
COMMON_EVENT = ['onclick', 'ondblclick', 'onmousedown', 'onmouseup', 'onmouseover', 'onmousemove', 'onmouseout', 'onkeypress', 'onkeydown', 'onkeyup']
COMMON_STYLE = ['style']
COMMON       = COMMON_CORE + COMMON_I18N + COMMON_EVENT + COMMON_STYLE

#Structure & Header
class base (single):
    valid    = ['href']
    required = ['href']
class body (html_tag): valid = ['onload', 'onunload'] + COMMON
class head (html_tag): valid = ['profile'] + COMMON_I18N
class html (html_tag):
    valid    = ['xmlns', 'xml:lang', 'xmlns:xsi', 'xsi:schemaLocation', 'version'] + COMMON_I18N
    required = ['xmlns']
    default  = {'xmlns': 'http://www.w3.org/1999/xhtml'}
class link (single):   valid = ['href', 'media', 'type', 'charset', 'hreflang', 'rel', 'rev'] + COMMON
class meta (single):
    valid    = ['content', 'name', 'http-equiv', 'scheme'] + COMMON_I18N
    required = ['name']
class script(ugly):
    valid    = ['src', 'type', 'charset', 'defer', 'xml:space'] + COMMON
    required = ['type']
class style(ugly):
    valid    = ['media', 'title', 'type', 'xml:space'] + COMMON_I18N
    required = ['type']
class title(html_tag): valid = COMMON_I18N

#Block elements
class address   (html_tag): valid = COMMON
class blockquote(html_tag): valid = ['cite'] + COMMON
class _del      (html_tag): valid = ['cite', 'datetime'] + COMMON
class div       (html_tag): valid = COMMON
class dl        (html_tag): valid = COMMON
class fieldset  (html_tag): valid = COMMON
class form      (html_tag): valid = ['action', 'method', 'accept', 'accept-charsets', 'enctype', 'onreset', 'onsubmit'] + COMMON
class h1        (html_tag): valid = COMMON
class h2        (html_tag): valid = COMMON
class h3        (html_tag): valid = COMMON
class h4        (html_tag): valid = COMMON
class h5        (html_tag): valid = COMMON
class h6        (html_tag): valid = COMMON
class hr        (single):   valid = COMMON
class ins       (html_tag): valid = ['cite', 'datetime'] + COMMON
class noscript  (html_tag): valid = COMMON
class ol        (html_tag): valid = COMMON
class p         (html_tag): valid = COMMON
class pre       (ugly):     valid = ['xml:space'] + COMMON
class table     (html_tag): valid = ['border', 'cellpadding', 'cellspacing', 'summary', 'width', 'frame', 'rules'] + COMMON
class ul        (html_tag): valid = COMMON

#Inline elements
class a       (html_tag): valid = ['href', 'accesskey', 'charset', 'coords', 'hreflang', 'onblur', 'onfocus', 'rel', 'rev', 'shape', 'tabindex', 'type'] + COMMON
class abbr    (html_tag): valid = COMMON
class acronym (html_tag): valid = COMMON
class b       (html_tag): valid = COMMON
class bdo     (html_tag): valid = ['dir'] + COMMON
class big     (html_tag): valid = COMMON
class br      (single):   valid = COMMON
class button  (html_tag): valid = ['name', 'type', 'value', 'accesskey', 'disabled', 'onblur', 'onfocus', 'tabindex'] + COMMON
class cite    (html_tag): valid = COMMON
class code    (ugly):     valid = COMMON
class dfn     (html_tag): valid = COMMON
class em      (html_tag): valid = COMMON
class i       (html_tag): valid = COMMON
class img     (single):
    valid    = ['alt', 'height', 'src', 'width', 'ismap', 'longdesc', 'usemap'] + COMMON
    required = ['alt', 'src']
    default  = {'alt': ''}
class _input  (single):   valid = ['alt', 'checked', 'maxlength', 'name', 'size', 'type', 'value', 'accept', 'accesskey', 'disabled', 'ismap', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'src', 'tabindex', 'usemap'] + COMMON
class kbd     (html_tag): valid = COMMON
class label   (html_tag): valid = ['for', 'accesskey', 'onblur', 'onfocus'] + COMMON
class _map    (html_tag): valid = COMMON
class _object (html_tag): valid = ['classid', 'codebase', 'height', 'name', 'type', 'width', 'archive', 'codetype', 'data', 'declare', 'standby', 'tabindex', 'usemap'] + COMMON
class q       (html_tag): valid = ['cite'] + COMMON
class ruby    (html_tag): valid = COMMON
class samp    (html_tag): valid = COMMON
class select  (html_tag): valid = ['multiple', 'name', 'size', 'disabled', 'onblur', 'onchange', 'onfocus', 'tabindex'] + COMMON
class small   (html_tag): valid = COMMON
class span    (html_tag): valid = COMMON
class strong  (html_tag): valid = COMMON
class sub     (html_tag): valid = COMMON
class sup     (html_tag): valid = COMMON
class textarea(html_tag): valid = ['cols', 'name', 'rows', 'accesskey', 'disabled', 'onblur', 'onchange', 'onfocus', 'onselect', 'readonly', 'tabindex'] + COMMON
class tt      (ugly):     valid = COMMON
class var     (html_tag): valid = COMMON

#List item elements
class dd(html_tag): valid = COMMON
class dt(html_tag): valid = COMMON
class li(html_tag): valid = COMMON

#Table content elements
class caption (html_tag): valid = COMMON
class col     (single):   valid = ['align', 'span', 'valign', 'width', 'char', 'charoff'] + COMMON
class colgroup(html_tag): valid = ['align', 'span', 'valign', 'width', 'char', 'charoff'] + COMMON
class tbody   (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON
class td      (html_tag): valid = ['align', 'colspan', 'headers', 'rowspan', 'valign', 'axis', 'char', 'charoff'] + COMMON
class tfoot   (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON
class th      (html_tag): valid = ['abbr', 'align', 'colspan', 'rowspan', 'valign', 'axis', 'char', 'charoff', 'scope'] + COMMON
class thead   (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON
class tr      (html_tag): valid = ['align', 'valign', 'char', 'charoff'] + COMMON

#Form fieldset legends
class legend(html_tag): valid = ['accesskey'] + COMMON

#Form menu options
class optgroup(html_tag): valid = ['label', 'disabled'] + COMMON
class option  (html_tag): valid = ['selected', 'value', 'disabled', 'label'] + COMMON

#Map areas
class area(single):
    valid    = ['alt', 'coords', 'href', 'shape', 'accesskey', 'onblur', 'onfocus', 'nohref', 'tabindex'] + COMMON
    required = ['alt']
    default  = {'alt': ''}

#Object parameters
class param(single):
    valid    = ['name', 'value', 'id', 'type', 'valuetype']
    required = ['name']

#Ruby annotations
class rb (html_tag): valid = COMMON
class rbc(html_tag): valid = COMMON
class rp (html_tag): valid = COMMON
class rt (html_tag): valid = ['rbspan'] + COMMON
class rtc(html_tag): valid = COMMON

###############################################################################

class htmlpage(basepage):
    def __init__(self, title='XHTML 1.1 Page'):
        basepage.__init__(self, title)
        
        self.headers['Content-Type'] = 'application/xml'
        self.xml     = '<?xml version="1.0" encoding="utf-8"?>'
        self.doctype = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">'
        self.html    = html()
        self.html.head, self.html.body = self.html.add(head(), body())
    
    def render(self, just_html=False):
        if not just_html:
            import web
            if web.is_internetexplorer:
                self.headers['Content-Type'] = 'text/html'
        
        return basepage.render(self, just_html)
