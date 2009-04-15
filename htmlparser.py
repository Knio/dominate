import html
import re

html.TAB = ' '

def parse(data):
    
    ht = re.compile('''<(/)?([^>]+)( /)?>''')
    tg = re.compile('''(\w+)''')
    at = re.compile('''(\w+)=(?:(\w+)|"([^"<>]*)")\W*''')
    
    result  = html.html()
    stack   = [result]
    
    while data:
        m = ht.search(data)
        s, e = m.span()
        if s: stack[-1] += data[0:s]
        data = data[e:]
        if m.group(1):
            result = stack.pop() # might want to check that tag matches
            continue
        inn = m.group(2)
        t = tg.match(inn)
        tag, inn = t.group(1), inn[t.end():]
        args = {}
        while inn:
            t = at.search(inn)
            args[t.group(1)] = t.group(2) or t.group(3)
            inn = inn[t.end():]
        n = getattr(html, tag)(**args)
        stack[-1] += n
        stack.append(n)
        if stack[-1].single or m.group(3): stack.pop()
    
    return result



def main():
    global r
    
    import database
    db = database.Database()
    
    row = db.get_scrape(1784)
    
    r = parse(row['data'])
    
    
    print r
    print row['type']
    print r.get('class', "SSSHYPERLINKBOLD")[0].tag(str)[0]
    




def XHTMLParse(data, allow_invalid=False, debug=False):
    import re
    
    r_xml  = re.compile(r"""<\?xml ([a-z]="\w+")+\?>""")
    r_doc  = re.compile(r"""<!DOCTYPE[^"]+"([^"]+)"[^"]+"([^"]+)/([^/]+)\.dtd">""")
    r_tag  = re.compile(r"""<(?P<closing>/)?(?P<name>[a-zA-Z0-9]+) (?P<attributes>)(?P<single> /)?>""") #TODO: make last '/' not work if leading '/'
    r_att  = re.compile(r"""(?P<name>[a-z\-\:]+)=(?:(\w+)|"([^"<>]*)")\W*""")
    
    #Remove xml declaration and doctype
    xml = r_xml.search(data)
    if xml:
        if debug:
            print 'Found DOCTYPE, ignored.'
        start, end = xml.span()
        data = data[end:]
    doctype = r_doc.search(data)
    if doctype:
        if debug:
            print 'Found XML declaration, ignored.'
        start, end = doctype.span()
        data = data[end:]
    
    result  = html()
    stack   = [result]
    
    while data:
        match = r_tag.search(data)
        if not match:
            break
        start, end = match.span()
        if debug:
            print data[start:end]
        if start: stack[-1] += data[0:start]
        data = data[end:]
        if match.group(1):
            if debug:
                print 'pop  <'
                
            result = stack.pop() # might want to check that tag matches
            continue
        inner = match.group(2)
        tag = r_name.match(inner)
        name, atts = tag.group(1), inner[tag.end():]
        args = {}
        while inner:
            tag = r_att.search(atts)
            print tag.group(1) + '=' + (tag.group(2) or tag.group(3))
            args[tag.group(1)] = tag.group(2) or tag.group(3)
            inn = inn[tag.end():]
        new = getattr(html, tag)(__invalid=allow_invalid, **args)
        
        if debug:
            print 'push > ' + str(new)
            
        stack[-1] += new
        stack.append(new)
        if stack[-1].is_single or match.group(3):
            if debug:
                print 'pop  <'
                
            stack.pop()
    
    return result

def testtest():
    import urllib
    data = urllib.urlopen('http://www.imdb.com/title/tt0095016/').read()
    print XHTMLParse(data, False, True)












__test_data = '''<tbody><tr>
<td height="3" width="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="1"></td>
<td width="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="4"></td>
<td width="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="4"></td>
<td width="5"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="5"></td>
<td width="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="1"></td>
<td width="74"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="74"></td>
<td width="32"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="32"></td>
<td width="108"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="108"></td>
<td width="97"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="97"></td>
<td width="175"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="175"></td>
<td width="44"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="44"></td>
<td width="20"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="20"></td>
<td width="46"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="46"></td>
</tr>
<tr>
<td height="24"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="10" align="left" valign="top">
<table class="PSGROUPBOXNBO" cellpadding="0" cellspacing="0" cols="1" width="543">
<tbody><tr><td class="PAGROUPBOXLABELINVISIBLE" align="left">Groupbox</td></tr>
<tr><td width="543">
<table id="ACE_width" class="PSGROUPBOX" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="2" width="543">
<tbody><tr>
<td height="0" width="14"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="14"></td>
<td width="529"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="529"></td>
</tr>
<tr>
<td height="14"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" valign="top">
<span class="PATRANSACTIONTITLE">Class Search</span>
</td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
<td colspan="2" rowspan="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="11" height="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="5" height="5"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="4" rowspan="2" align="left" valign="top">
<label for="DERIVED_CLSRCH_SSR_CLASS_LBL" class="PAPAGETITLE">Class Search Results</label>
</td>
<td colspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="5" height="23"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="4" align="left" valign="top">
<span class="PSEDITBOX_DISPONLY">&nbsp;</span>
</td>
</tr>
<tr>
<td colspan="4" height="41"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="9" align="left" valign="top">
<span class="PAPAGEINSTRUCTIONS">When available, click View All Sections to see all sections of the course.</span>
</td>
</tr>
<tr>
<td colspan="4" height="14"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="9" align="left" valign="top">
<span class="SSSKEYTEXT">University of Calgary | Fall 2008</span>
</td>
</tr>
<tr>
<td colspan="2" height="12"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="4" align="left" valign="top">
<table class="PABACKGROUNDINVISIBLEWBO" cellpadding="0" cellspacing="0" cols="1" width="84">
<tbody><tr><td height="10" width="82"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="82">
</td></tr>
</tbody></table>
</td>
<td colspan="7" rowspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="6" height="5"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="29"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="9" align="left" valign="top">
<table class="SSSKEYFRAMEWBO" cellpadding="0" cellspacing="0" cols="1" width="555">
<tbody><tr><td width="551">
<table id="ACE_width" class="SSSKEYFRAME" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="3" width="551">
<tbody><tr>
<td height="0" width="258"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="258"></td>
<td width="284"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="284"></td>
<td width="9"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="9"></td>
</tr>
<tr>
<td height="19"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" valign="top">
<table class="PABACKGROUNDINVISIBLEWBO" cellpadding="0" cellspacing="0" cols="1" width="283">
<tbody><tr><td width="281">
<table id="ACE_width" class="PABACKGROUNDINVISIBLE" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="9" width="281">
<tbody><tr>
<td height="0" width="11"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="11"></td>
<td width="16"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="16"></td>
<td width="44"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="44"></td>
<td width="36"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="36"></td>
<td width="16"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="16"></td>
<td width="52"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="52"></td>
<td width="20"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="20"></td>
<td width="16"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="16"></td>
<td width="70"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="70"></td>
</tr>
<tr>
<td colspan="2" height="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="2" align="left" valign="top">
<span class="SSSKEYTEXT">Open</span>
</td>
<td colspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="2" align="left" valign="top">
<span class="SSSKEYTEXT">Closed</span>
</td>
<td colspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="2" align="left" valign="top">
<span class="SSSKEYTEXT">Wait List</span>
</td>
</tr>
<tr>
<td height="15"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" valign="top">
<img src="/cs/saprd/cache/PS_CS_STATUS_OPEN_ICN_1.gif" alt="Open" title="Open" class="PSSTATICIMAGE" height="16" width="16">
</td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" valign="top">
<img src="/cs/saprd/cache/PS_CS_STATUS_CLOSED_ICN_1.gif" alt="Closed" title="Closed" class="PSSTATICIMAGE" height="16" width="16">
</td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" valign="top">
<img src="/cs/saprd/cache/PS_CS_STATUS_WAITLIST_ICN_1.gif" alt="Wait List" title="Wait List" class="PSSTATICIMAGE" height="16" width="16">
</td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
<td rowspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="2" height="0"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
<td rowspan="11"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="12" height="15"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="8" height="21"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="4" align="left" valign="top">
<table class="PABACKGROUNDINVISIBLEWBO" cellpadding="0" cellspacing="0" cols="1" width="335">
<tbody><tr><td width="333">
<table id="ACE_width" class="PABACKGROUNDINVISIBLE" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="3" width="333">
<tbody><tr>
<td height="0" width="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="3"></td>
<td width="192"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="192"></td>
<td width="138"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="138"></td>
</tr>
<tr>
<td height="10"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" nowrap="nowrap" valign="top">
<span class="SSSBUTTON_CANCELLINK">
<a name="CLASS_SRCH_WRK2_SSR_PB_CLOSE" id="CLASS_SRCH_WRK2_SSR_PB_CLOSE" tabindex="29" href="javascript:submitAction_win0(document.win0,'CLASS_SRCH_WRK2_SSR_PB_CLOSE');" class="SSSBUTTON_CANCELLINK" title="Close Push Button">Change Institution or Term</a></span>
</td>
<td align="left" valign="top">
<span class="SSSBUTTON_CANCELLINK">
<a name="CLASS_SRCH_WRK2_SSR_PB_NEW_SEARCH" id="CLASS_SRCH_WRK2_SSR_PB_NEW_SEARCH" tabindex="30" href="javascript:submitAction_win0(document.win0,'CLASS_SRCH_WRK2_SSR_PB_NEW_SEARCH');" class="SSSBUTTON_CANCELLINK" title="Search">Start a New Search</a></span>
</td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="12" height="0"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="2" height="8"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="5" align="left" valign="top">
<table class="PABACKGROUNDINVISIBLEWBO" cellpadding="0" cellspacing="0" cols="1" width="116">
<tbody><tr><td height="6" width="114"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="114">
</td></tr>
</tbody></table>
</td>
<td colspan="5" rowspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="7" height="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="2" height="297"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="10" align="left" valign="top">
<table class="PABACKGROUNDINVISIBLEWBO" id="$ICField59$scroll$0" cellpadding="0" cellspacing="0" cols="1" width="560">
<tbody><tr><td width="558">
<table id="ACE_width" class="PABACKGROUNDINVISIBLE" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="4" width="558">
<tbody><tr>
<td height="7" width="0"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="0"></td>
<td width="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="4"></td>
<td width="29"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="29"></td>
<td width="525"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="525"></td>
</tr>
<tr>
<td colspan="2" height="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="2" align="left" nowrap="nowrap" valign="top">
<a name="DERIVED_CLSRCH_SSR_EXPAND_COLLAP2$0" id="DERIVED_CLSRCH_SSR_EXPAND_COLLAP2$0" tabindex="50" href="javascript:submitAction_win0(document.win0,'DERIVED_CLSRCH_SSR_EXPAND_COLLAP2$0');"><img src="/cs/saprd/cache/PS_COLLAPSE_ICN_1.gif" name="DERIVED_CLSRCH_SSR_EXPAND_COLLAP2$IMG$0" alt="Expand / Collapse" title="Expand / Collapse" border="0"></a>
</td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="2" height="23"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" valign="top">
<span class="SSSHYPERLINKBOLD">CPSC&nbsp; 441 - Computer Communications</span>
</td>
</tr>
<tr>
<td height="225"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="3" align="left" valign="top">
<table class="PSGROUPBOXNBO" cellpadding="0" cellspacing="0" cols="1" width="559">
<tbody><tr><td class="PAGROUPBOXLABELINVISIBLE" align="left">Groupbox</td></tr>
<tr><td width="559">
<table id="ACE_width" class="PSGROUPBOX" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="3" width="559">
<tbody><tr>
<td height="0" width="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="4"></td>
<td width="552"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="552"></td>
<td width="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="3"></td>
</tr>
<tr>
<td height="222"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" valign="top">
<table class="PSLEVEL3GRIDWBO" id="$ICField67$scroll$0" cellpadding="0" cellspacing="0" cols="1" width="552">
<tbody><tr><td class="PTNAVSEARCHLABEL" align="right"><a name="$ICField67$hviewall$0" id="$ICField67$hviewall$0" tabindex="-1" href="javascript:submitAction_win0(document.win0,'$ICField67$hviewall$0');" class="PTNAVSEARCHLABEL">View 3</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="PTNAVSEARCHLABEL" style="color: dimgray;">First</span>&nbsp;<img src="/cs/saprd/cache/PT_PREVIOUSROW_D_1.gif" name="$ICField67$hup$img$0" alt="Show previous row (inactive button) (Alt+,)" title="Show previous row (inactive button) (Alt+,)" border="0">&nbsp;<span class="PSGRIDCOUNTER">1-2 of 2</span>&nbsp;<img src="/cs/saprd/cache/PT_NEXTROW_D_1.gif" name="$ICField67$hdown$img$0" alt="Show next row (inactive button) (Alt+.)" title="Show next row (inactive button) (Alt+.)" border="0">&nbsp;<span class="PTNAVSEARCHLABEL" style="color: dimgray;">Last</span>&nbsp;</td></tr>
<tr><td width="549">
<table id="ACE_width" class="PSLEVEL3GRID" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="12" width="549">
<tbody><tr>
<td height="10" width="0"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="0"></td>
<td width="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="1"></td>
<td width="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="3"></td>
<td width="56"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="56"></td>
<td width="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="1"></td>
<td width="111"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="111"></td>
<td width="27"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="27"></td>
<td width="249"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="249"></td>
<td width="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="4"></td>
<td width="48"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="48"></td>
<td width="28"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="28"></td>
<td width="21"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="21"></td>
</tr>
<tr>
<td colspan="4" height="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="5" rowspan="3" align="left" valign="top">
<span class="PSHYPERLINK">
<a name="DERIVED_CLSRCH_SSR_CLASSNAME_LONG$0" id="DERIVED_CLSRCH_SSR_CLASSNAME_LONG$0" tabindex="65" href="javascript:submitAction_win0(document.win0,'DERIVED_CLSRCH_SSR_CLASSNAME_LONG$0');" class="PSHYPERLINK" title="Class Name 1">01-LEC(72312)</a></span>
</td>
<td colspan="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="4" height="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="2" rowspan="2" align="left" nowrap="nowrap" valign="top">
<a name="DERIVED_CLSRCH_STATUS$0" id="DERIVED_CLSRCH_STATUS$0" tabindex="67" href="javascript:submitAction_win0(document.win0,'DERIVED_CLSRCH_STATUS$0');"><img src="/cs/saprd/cache/PS_CS_STATUS_OPEN_ICN_1.gif" name="DERIVED_CLSRCH_STATUS$IMG$0" alt="Status" title="Status" border="0"></a>
</td>
</tr>
<tr>
<td colspan="3" height="16"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="2" align="left" valign="top">
<label for="DERIVED_CLSRCH_SSR_SECTION_LBL$0" class="PSEDITBOXLABEL">Section</label>
</td>
<td align="left" valign="top">
<label for="DERIVED_CLSRCH_SSR_DESCRSHORT$0" class="PSEDITBOXLABEL">Status</label>
</td>
</tr>
<tr>
<td colspan="3" height="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="3" rowspan="3" align="left" valign="top">
<table class="PSFRAMENBO" cellpadding="0" cellspacing="0" cols="1" width="80">
<tbody><tr><td height="16" width="80"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="80">
</td></tr>
</tbody></table>
</td>
<td rowspan="5"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="3" rowspan="3" align="left" valign="top">
<label for="UCSS_E010_WRK_ASSOCIATED_CLASS$0" class="PSEDITBOXLABEL">Section Combination Group *</label>
</td>
<td colspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="11"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="3" align="right" valign="top">
<span class="PSEDITBOX_DISPONLY">1</span>
</td>
<td rowspan="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="5"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="3" rowspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="2" rowspan="2" align="left" valign="top">
<label for="SSR_CLSRCH_SCTN_SESSION_CODE$0" class="PSEDITBOXLABEL">Session</label>
</td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="10"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="7" align="left" valign="top">
<span class="PSEDITBOX_DISPONLY">Regular Academic</span>
</td>
</tr>
<tr>
<td height="40"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="11" align="left" valign="top">
<table class="PSLEVEL3GRIDWBO" id="SSR_CLSRCH_MTG1$scroll$0" dir="ltr" border="1" cellpadding="2" cellspacing="0" cols="3" width="556">
<tbody><tr valign="center">
<th scope="col" class="PSLEVEL3GRIDCOLUMNHDR" align="left" width="126"><a name="SSR_CLSRCH_MTG1$srt1$0" tabindex="-1" class="PSLEVEL3GRIDCOLUMNHDR" href="javascript:submitAction_win0(document.win0,'SSR_CLSRCH_MTG1$srt1$0');" title="Click column heading to sort ascending">Days &amp; Times</a></th>
<th scope="col" class="PSLEVEL3GRIDCOLUMNHDR" align="left" width="91"><a name="SSR_CLSRCH_MTG1$srt2$0" tabindex="-1" class="PSLEVEL3GRIDCOLUMNHDR" href="javascript:submitAction_win0(document.win0,'SSR_CLSRCH_MTG1$srt2$0');" title="Click column heading to sort ascending">Room</a></th>
<th scope="col" class="PSLEVEL3GRIDCOLUMNHDR" align="left" width="126"><a name="SSR_CLSRCH_MTG1$srt3$0" tabindex="-1" class="PSLEVEL3GRIDCOLUMNHDR" href="javascript:submitAction_win0(document.win0,'SSR_CLSRCH_MTG1$srt3$0');" title="Click column heading to sort ascending">Instructor</a></th>
</tr>
<tr valign="center">
<td class="PSLEVEL1GRIDODDROW" align="left" height="13">
<span class="PSLONGEDITBOX">MWF 11:00 - 11:50</span>
</td>
<td class="PSLEVEL1GRIDODDROW" align="left">
<span class="PSLONGEDITBOX">SS 109</span>
</td>
<td class="PSLEVEL1GRIDODDROW" align="left">
<span class="PSLONGEDITBOX">Zongpeng Li</span>
</td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="2" height="14"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="10" align="left" valign="top">
<hr class="PSLEVEL3GRID" align="left" width="100%">
</td>
</tr>
<tr>
<td colspan="4" height="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="5" rowspan="3" align="left" valign="top">
<span class="PSHYPERLINK">
<a name="DERIVED_CLSRCH_SSR_CLASSNAME_LONG$1" id="DERIVED_CLSRCH_SSR_CLASSNAME_LONG$1" tabindex="102" href="javascript:submitAction_win0(document.win0,'DERIVED_CLSRCH_SSR_CLASSNAME_LONG$1');" class="PSHYPERLINK" title="Class Name 2">T01-TUT(72314)</a></span>
</td>
<td colspan="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="4" height="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="2" rowspan="2" align="left" nowrap="nowrap" valign="top">
<a name="DERIVED_CLSRCH_STATUS$1" id="DERIVED_CLSRCH_STATUS$1" tabindex="104" href="javascript:submitAction_win0(document.win0,'DERIVED_CLSRCH_STATUS$1');"><img src="/cs/saprd/cache/PS_CS_STATUS_OPEN_ICN_1.gif" name="DERIVED_CLSRCH_STATUS$IMG$1" alt="Status" title="Status" border="0"></a>
</td>
</tr>
<tr>
<td colspan="3" height="16"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="2" align="left" valign="top">
<label for="DERIVED_CLSRCH_SSR_SECTION_LBL$1" class="PSEDITBOXLABEL">Section</label>
</td>
<td align="left" valign="top">
<label for="DERIVED_CLSRCH_SSR_DESCRSHORT$1" class="PSEDITBOXLABEL">Status</label>
</td>
</tr>
<tr>
<td colspan="3" height="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="4"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="3" rowspan="3" align="left" valign="top">
<table class="PSFRAMENBO" cellpadding="0" cellspacing="0" cols="1" width="80">
<tbody><tr><td height="16" width="80"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="80">
</td></tr>
</tbody></table>
</td>
<td rowspan="5"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="3" rowspan="3" align="left" valign="top">
<label for="UCSS_E010_WRK_ASSOCIATED_CLASS$1" class="PSEDITBOXLABEL">Section Combination Group *</label>
</td>
<td colspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="11"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td rowspan="3" align="right" valign="top">
<span class="PSEDITBOX_DISPONLY">1</span>
</td>
<td rowspan="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="5"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="3" rowspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="1"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="2" rowspan="2" align="left" valign="top">
<label for="SSR_CLSRCH_SCTN_SESSION_CODE$1" class="PSEDITBOXLABEL">Session</label>
</td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="10"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="7" align="left" valign="top">
<span class="PSEDITBOX_DISPONLY">Regular Academic</span>
</td>
</tr>
<tr>
<td height="40"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="11" align="left" valign="top">
<table class="PSLEVEL3GRIDWBO" id="SSR_CLSRCH_MTG1$scroll$1" dir="ltr" border="1" cellpadding="2" cellspacing="0" cols="3" width="556">
<tbody><tr valign="center">
<th scope="col" class="PSLEVEL3GRIDCOLUMNHDR" align="left" width="126"><a name="SSR_CLSRCH_MTG1$srt1$1" tabindex="-1" class="PSLEVEL3GRIDCOLUMNHDR" href="javascript:submitAction_win0(document.win0,'SSR_CLSRCH_MTG1$srt1$1');" title="Click column heading to sort ascending">Days &amp; Times</a></th>
<th scope="col" class="PSLEVEL3GRIDCOLUMNHDR" align="left" width="91"><a name="SSR_CLSRCH_MTG1$srt2$1" tabindex="-1" class="PSLEVEL3GRIDCOLUMNHDR" href="javascript:submitAction_win0(document.win0,'SSR_CLSRCH_MTG1$srt2$1');" title="Click column heading to sort ascending">Room</a></th>
<th scope="col" class="PSLEVEL3GRIDCOLUMNHDR" align="left" width="126"><a name="SSR_CLSRCH_MTG1$srt3$1" tabindex="-1" class="PSLEVEL3GRIDCOLUMNHDR" href="javascript:submitAction_win0(document.win0,'SSR_CLSRCH_MTG1$srt3$1');" title="Click column heading to sort ascending">Instructor</a></th>
</tr>
<tr valign="center">
<td class="PSLEVEL1GRIDODDROW" align="left" height="13">
<span class="PSLONGEDITBOX">TuTh 14:00 - 14:50</span>
</td>
<td class="PSLEVEL1GRIDODDROW" align="left">
<span class="PSLONGEDITBOX">EDC 152</span>
</td>
<td class="PSLEVEL1GRIDODDROW" align="left">
<span class="PSLONGEDITBOX">Staff</span>
</td>
</tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="12" height="0"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
<td><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="4" height="38"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="12" height="9"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="3" height="31"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="7" align="left" valign="top">
<span class="PSTEXT">* Sections with the same "Section Combination Group" or 9999 may be taken together.</span>
</td>
<td colspan="2"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
<tr>
<td colspan="8" height="21"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td colspan="4" align="left" valign="top">
<table class="PABACKGROUNDINVISIBLEWBO" cellpadding="0" cellspacing="0" cols="1" width="335">
<tbody><tr><td width="333">
<table id="ACE_width" class="PABACKGROUNDINVISIBLE" style="border-style: none;" border="0" cellpadding="0" cellspacing="0" cols="3" width="333">
<tbody><tr>
<td height="0" width="3"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="3"></td>
<td width="188"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="188"></td>
<td width="142"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt="" height="1" width="142"></td>
</tr>
<tr>
<td height="10"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
<td align="left" nowrap="nowrap" valign="top">
<span class="SSSBUTTON_CANCELLINK">
<a name="CLASS_SRCH_WRK2_SSR_PB_CLOSE$53$" id="CLASS_SRCH_WRK2_SSR_PB_CLOSE$53$" tabindex="33" href="javascript:submitAction_win0(document.win0,'CLASS_SRCH_WRK2_SSR_PB_CLOSE$53$');" class="SSSBUTTON_CANCELLINK" title="Close Push Button">Change Institution or Term</a></span>
</td>
<td align="left" valign="top">
<span class="SSSBUTTON_CANCELLINK">
<a name="CLASS_SRCH_WRK2_SSR_PB_NEW_SEARCH$54$" id="CLASS_SRCH_WRK2_SSR_PB_NEW_SEARCH$54$" tabindex="34" href="javascript:submitAction_win0(document.win0,'CLASS_SRCH_WRK2_SSR_PB_NEW_SEARCH$54$');" class="SSSBUTTON_CANCELLINK" title="Search">Start a New Search</a></span>
</td>
</tr>
</tbody></table>
</td></tr>
</tbody></table>
</td>
</tr>
<tr>
<td colspan="12" height="0"><img src="/cs/saprd/cache/PT_PIXEL_1.gif" alt=""></td>
</tr>
</tbody>'''


if __name__ == '__main__':
    main()
    
    
