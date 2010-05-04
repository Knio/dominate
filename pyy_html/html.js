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

//function $(){}

(function()
{
  function node(obj)
  {   
    try { return (obj instanceof Node); }
    catch (e) { return obj.nodeType; }
  }  
  
  var tags = [
    'div', 'span', 'p', 'img', 'a', 
    'h1', 'h2', 'h3', 'h4', 'h5', 
    'table', 'tr', 'td', 'th',
    'input','form','textarea',
    'canvas','audio','video'
    ];
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
          if (node(argument))
              dom.appendChild(argument)
          else if (typeof argument == 'string')                
              dom.appendChild(document.createTextNode(argument))
          else
          {
            for (key in argument)
            {
              var value = argument[key];
              if (key == 'class')
                dom.className = value; // TODO multiple classes
              else if (key == 'style') // style: {background:'#000'}
                for (style in value)
                  YAHOO.util.Dom.setStyle(dom, style[style], value[style]);
              else if (key.slice(0, 2) == 'on') // an event handler
                dom.addEventListener(key.slice(2), value, false)
              else // otherwise a regular attribute
                dom.setAttribute(key, value);
            }
          }
        }
        return dom;
      }
      $[tag] = func;
    }());
  }
}());
