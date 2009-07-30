/*
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
*/

(function()
{
    var tags = ['div', 'img', 'a', 'span']
    for (var i=0; i < tags.length; i++)
    {
        (function(){
            var tag = tags[i];
            func = function()
            {
                var dom = document.createElement(tag);
                
                for (var j=0; j < arguments.length; j++)
                {
                    var argument = arguments[j];
                    if (argument instanceof Node)
                        dom.appendChild(argument)
                    else if (typeof argument == 'string')                
                        dom.appendChild(document.createTextNode(argument))
                    else
                    {
                        for (key in argument)
                        {
                            var value = argument[key];
                            if (key == 'class')
                                dom.className += dom.className ? ' ' + value : value;
                                //YAHOO.util.Dom.addClass(tag, value);
                            else if (key == 'style') // style: {background:'#000'}
                                for (style in value)
                                    dom.style[style] = value[style]
                                    //YAHOO.util.Dom.setStyle(dom, style, value[style]);
                            else if (k.slice(0, 2) == 'on') // an event handler
                                dom.addEventListener(key.slice(2), value, false)
                                //YAHOO.util.Event.addListener(dom, key.slice(2), value);
                            else // otherwise a regular attribute
                                dom.setAttribute(key, value);
                        }
                    }
                }
                return dom;
            }
<<<<<<< HEAD:pyy/html.js
            window[tag] = func;
=======
            return dom;
        }
        $[tag] = func;
>>>>>>> e6bfd3f... fixed setup script, htmlpage entry point:pyy/html.js
        }());
    }    
}());
