var U = {};
var H;
//var Y = YUI.use('*');

Y.use('json');

(function() {

  U.load = JSON.parse;
  U.dump = JSON.stringify;

  U.io = function(method, url, data, ctx, succ, fail)
  {
    var conn = Y.io(url, {
      method: method,
      data: data,
      // TODO headers
      on: {
        start:    null,
        complete: null,
        success: function(transaction, response, conn)
        {
          if (!succ) return;
          succ.call(ctx, U.load(response.responseText),
            transaction, response, conn);
        },
        failure:  fail ? function(transaction, response, conn)
        {
          fail.call(ctx, response);
        } : null,
        end:null
      },
      context: ctx,
      timeout: 10*1000
    });
  };

  U.get = function(url, succ) {
    return U.io('GET', url, null, null, succ);
  }
  U.post = function(url, succ) {
    return U.io('POST', url, null, null, succ);
  }

  /**
   * @method: foreach
   * @for U
   * @param {Object|Array} obj - the object you want to iterate.
   * @param {Function} f - the function to apply for elements in obj.
   *      If obj is object then f(value, key), else f(value, index).
   *      If the function returns false the loop breaks.
   * @param {Object} that - optional context for the function.
   * @returns {Void}
   */
  U.foreach = function(obj, f, that)
  {
    that = that || null;
    var cont;
    if (Y.Array.test(obj) === 0)
    {
      // obj is an Object.
      // TODO check typeof obj === "object" here?
      for (var key in obj)
      {
        if (obj.hasOwnProperty(key))
        {
          cont = f.call(that, obj[key], key);
          if (cont !== undefined)
          {
            return cont;
          }
        }
      }
    }
    else
    {
      for (var i = 0; i < obj.length; ++i)
      {
        cont = f.call(that, obj[i], i);
        if (cont !== undefined)
        {
          return cont;
        }
      }
    }
    return undefined;
  };

  U.remove = function(array, obj)
  {
    var i = Y.Array.indexOf(array, obj);
    if (i === -1)
    {
      return false;
    }
    array.splice(i, 1);
    return true;
  };

  /**
   * @method splice
   * @for U
   *
   * @returns The spliced array
   */
  U.splice = function(arr)
  {
    var args = Array.prototype.slice.call(arguments, 1);
    arr.splice.apply(arr, args);
    return arr;
  };

  U.map = function(arr, f, context)
  {
    var res = [];
    U.foreach(arr, function(val, i) {
      res.push(f.call(context, val, i));
    }, context);
    return res;
  };

  U.filter = function(arr, f, context)
  {
    var res = [];
    U.foreach(arr, function(val) {
      if (f.call(context, val))
      {
        res.push(val);
      }
    }, context);
    return res;
  };

  U.filter = function(arr, f, context)
  {
    var res = [];
    U.foreach(arr, function(val, i) {
      if (f.call(context, val))
      {
        res.push(val);
      }
    }, context);
    return res;
  };

  U.min = function(lhs, rhs)
  {
    return lhs < rhs ? lhs : rhs;
  };

  U.max = function(lhs, rhs)
  {
    return lhs > rhs ? lhs : rhs;
  };

  /**
   * @param {string} a
   * @param {string} b
   * @returns whether b is a prefix of a.
   */
  U.prefix = function(a, b)
  {
    return a.slice(0, b.length) === b;
  };

  /**
   * @returns whether b is a suffix of a.
   */
  U.suffix = function(a, b)
  {
    return a.slice(a.length - b.length) === b;
  };

  /**
   * @method cap
   * @for U
   *
   * @returns min if val < min, max if val > max and val otherwise.
   */
  U.cap = function(val, min, max)
  {
    return val < min ? min : val > max ? max : val;
  };

  H = function(s)
  {
    // TODO only if s is a string
    return document.createTextNode(s);
  };

  // return a DOM element
  H.dom = function(dom)
  {
    if (Y.Lang.isString(dom))
    {
      dom = document.getElementById(dom);
    }
    return dom;
  };

  // delete a DOM element
  H.remove = function(dom)
  {
    dom = H.dom(dom);
    if (dom.parentNode)
    {
      dom.parentNode.removeChild(dom);
    }
    return dom;
  };

  // remove all children from a DOM element
  H.empty = function(dom)
  {
    dom = H.dom(dom);

    // This is bad but probably much faster than the below
    dom.innerHTML = '';

    // var current = dom.firstChild;
    // var next;
    // while (current !== null)
    // {
    //   next = current.nextSibling;
    //   dom.removeChild(current);
    //   current = next;
    // }
    return dom;
  };

  H.replace_content = function(dom, new_child)
  {
    H.empty(dom);
    dom.appendChild(new_child);
  };


  H.show = function(dom, display)
  {
    display = display || '';
    H.css(dom, {display: display});
  };

  H.hide = function(dom)
  {
    H.css(dom, {display: 'none'});
  };

  H.add_class = function(dom, klass)
  {
    Y.DOM.addClass(dom, klass);
  };

  H.remove_class = function(dom, klass)
  {
    Y.DOM.removeClass(dom, klass);
  };

  H.set_class = function(dom, klass, on)
  {
    H[on ? "add_class" : "remove_class"](dom, klass);
  };

  H.sprite = function(name)
  {
    var args = Array.prototype.slice.call(arguments, 1);
    args.unshift({'class': 'sprite_' + name, src: '/images/blank.gif'});
    return H.img.apply(this, args);
  };

  // converts all keys in dictionary from _ or - to camelCase
  var css2js_style_names = function(dict)
  {
    var style_name, style_value;
    var new_styles = {};
    var mapping = {cls: 'class'};
    var upper = function(_, letter) { return letter.toUpperCase(); };
    U.foreach(dict, function(value, name) {
        name = name.replace(/(?:-|_)(.)/g, upper);
        if (mapping.hasOwnProperty(name))
        {
          name = mapping[name];
        }
        new_styles[name] = value;
    });
    return new_styles;
  };

  H.css = function(dom, css_dict)
  {
    var css = css2js_style_names(css_dict);
    Y.DOM.setStyles(dom, css);
    if (css.hasOwnProperty('class'))
    {
      dom.className = css['class'];
    }
  };

  // Returns [x, y] of the offset between dom and a given ancestor.
  H.offsetAncestor = function(dom, ancestor)
  {

    var xy_dom = Y.DOM.getXY(dom);
    if (!ancestor) return xy_dom;
    var xy_anc = Y.DOM.getXY(ancestor);

    return [
      xy_dom[0] - xy_anc[0] -
        parseInt(Y.DOM.getComputedStyle(ancestor, "borderLeftWidth")),
      xy_dom[1] - xy_anc[1] -
        parseInt(Y.DOM.getComputedStyle(ancestor, "borderTopWidth"))
    ];


    return U.vsub(U.vsub(Y.DOM.getXY(dom), Y.DOM.getXY(ancestor)),
        // Remove the border of the ancestor if any.
        U.map([Y.DOM.getComputedStyle(ancestor, "borderLeftWidth"),
            Y.DOM.getComputedStyle(ancestor, "borderTopWidth")],
            function(s) { return parseInt(s, 10); }));
  };

  H.get_size  = function(dom)
  {
    return [dom.offsetWidth, dom.offsetHeight];
  };


  H.set_size = function(dom, size)
  {
    H.css(dom, {
        width:  size[0],
        height: size[1]
    });
  };

  H.get_off = function(dom)
  {
    return [dom.offsetLeft, dom.offsetTop];
  };

  H.set_off = function(dom, off)
  {
    H.css(dom, {
        left:   off[0],
        top:  off[1]
    });
  };

  H.get_rect = function(dom, ancestor)
  {
    dom = H.dom(dom);
    // if (!ancestor)
    // {
    //   return {
    //     x: dom.offsetLeft,
    //     y: dom.offsetTop,
    //     w: dom.offsetWidth,
    //     h: dom.offsetHeight
    //   };
    // }
    // else
    // {
      var xy = H.offsetAncestor(dom, H.dom(ancestor));
      return {
        x: xy[0],
        y: xy[1],
        w: dom.offsetWidth,
        h: dom.offsetHeight
      };
    // }
  }


  /*global Node */
  var node = function(obj)
  {
    try
    {
      return (obj instanceof Node);
    }
    catch (e)
    {
      return obj && obj.nodeType;
    }
  };

  var tags = [
    'div', 'span', 'p', 'img', 'a', 'br', 'h1', 'h2', 'h3', 'h4', 'h5',
    'hr', 'table', 'tr', 'td', 'th', 'strong', 'em', 'input', 'form',
    'textarea', 'select', 'option', 'canvas', 'audio', 'video', 'ul', 'ol',
    'li', 'button'
  ];

  H.update = function(dom)
  {

    var context = dom;

    for (var j = 1; j < arguments.length; j++)
    {
      var argument = arguments[j];

      var i, key;
      if (node(argument))
      {
        dom.appendChild(argument);
      }
      else if (typeof argument === 'string')
      {
        dom.appendChild(document.createTextNode(argument));
      }
      else if (argument instanceof Array)
      {
        for (i = 0; i < argument.length; i++)
        {
          H.update(dom, argument[i]);
        }
      }
      else
      {
        if ((typeof argument === 'object') &&
            argument.hasOwnProperty('context'))
        {
          context = argument.context;
        }

        for (key in argument)
        {
          if (!argument.hasOwnProperty(key))
          {
            continue;
          }
          var value = argument[key];
          if (key === 'context')
          {
            // handled above - must be first
            continue;
          }
          else if (key === 'class' || key === "cls")
          {
            if (!value) { continue; }
            var classes = value.split(/\s+/);
            for (var c = 0; c < classes.length; c++)
            {
              Y.DOM.addClass(dom, classes[c]);
            }
          }
          else if (key === 'style') // style: {background:'#000'}
          {
            Y.DOM.setStyles(dom, css2js_style_names(value));
          }
          else if (key.slice(0, 2) === 'on') // an event handler
          {
            var f = value, args = [];
            if (typeof value !== "function")
            {
              f = value.func;
              args = value.args;
            }
            args = [key.slice(2), f, dom, context].concat(args);
            Y.on.apply(Y, args);
          }
          else // otherwise a regular attribute
          {
            Y.DOM.setAttribute(dom, key, value);
          }
        }
      }
    }
  };

  var make_func = function(tag)
  {
    return function()
    {
      var dom   = document.createElement(tag);

      for (var j = 0; j < arguments.length; j++)
      {
        var argument = arguments[j];
        H.update(dom, argument);
      }
      return dom;
    };
  };

  for (var i = 0; i < tags.length; i++)
  {
    var tag = tags[i];
    H[tag] = make_func(tag);
  }

}());

