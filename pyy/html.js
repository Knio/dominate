


(function()
{
    var tags = ['div','img','a','span']
    for (var i=0;i<tags.length;i++)
    {
        (function(){
        var tag = tags[i];
        func = function()
        {
            var dom = document.createElement(tag);
            
            for (var j=0;j<arguments.length;j++)
            {
                var c = arguments[j];
                if (c instanceof Node)
                    dom.appendChild(c)
                else if (typeof c == 'string')                
                    dom.appendChild(document.createTextNode(c))
                else
                {
                    for (k in c)
                    {
                        var v = c[k];
                        if (k == 'class')  YAHOO.util.Dom.addClass(dom, obj[i]);
                        else if (k == 'style') // style: {background:'#000'}
                            for (style in v)  
                                YAHOO.util.Dom.setStyle(dom, style, v[style]);
                        else if (k.slice(0,2) == 'on') // an event handler
                            YAHOO.util.Event.addListener(dom, k.slice(2), v);
                        else // otherwise a regular addribute
                            dom.setAttribute(k, v);
                    }
                }                
            }
            return dom;

        }
        window[tag] = func;
        }());
    }    
}());


