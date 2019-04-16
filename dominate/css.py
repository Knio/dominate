# -*- coding: utf-8 -*-

from __future__ import print_function


"""
css classes.
"""

__license__ = '''
This file is part of Dominate.

Dominate is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

Dominate is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with Dominate.  If not, see
<http://www.gnu.org/licenses/>.
'''


class css_base(object):

    def __init__(self):
        self._selector = '*'

    @property
    def selector(self):
        """
        * `".class"` :
            Selects all elements with class="intro"
            example: `".intro"`

        * `"#id"` :
            Selects the element with id="firstname"
            example: `"#firstname"`

        * `"*"` :
            Selects all elements
            example: `"*"`

        * `"element"` :
            Selects all <p> elements
            example: `"p"`

        * `"element,element"` :
            Selects all <div> elements and all <p> elements
            example: `"div, p"`

        * `"element element"` :
            Selects all <p> elements inside <div> elements
            example: `"div p"`

        * `"element>element"`:
            Selects all <p> elements where the parent is a <div> element
            example: `"div > p"`

        * `"element+element"` :
            Selects all <p> elements that are placed immediately after <div> elements
            example: `"div + p"`

        * `"element1~element2"` :
            Selects every <ul> element that are preceded by a <p> element
            example: `"p ~ ul"`

        * `"[attribute]"` :
            Selects all elements with a target attribute
            example: `"[target]"`

        * `"[attribute=value]"` :
            Selects all elements with target="_blank"
            example: `"[target=_blank]"`

        * `"[attribute~=value]"` :
            Selects all elements with a title attribute containing the word "flower"
            example: `"[title~=flower]"`

        * `"[attribute|=value]"` :
            Selects all elements with a lang attribute value starting with "en"
            example: `"[lang|=en]"`

        * `"[attribute^=value]"`:
            Selects every <a> element whose href attribute value begins with "https"
            example: `"a[href^="https"]"`

        * `"[attribute$=value]"` :
            Selects every <a> element whose href attribute value ends with ".pdf"
            example: `"a[href$=".pdf"]"`

        * `"[attribute*=value]"` :
            Selects every <a> element whose href attribute value contains the substring "w3schools"
            example: `"a[href*="w3schools"]"`

        * `":active"` :
            Selects the active link
            example: `"a:active"`

        * `"::after"` :
            Insert something after the content of each <p> element
            example: `"p::after"`

        * `"::before"` :
            Insert something before the content of each <p> element
            example: `"p::before"`

        * `":checked"` :
            Selects every checked <input> element
            example: `"input:checked"`

        * `":default"` :
            Selects the default <input> element
            example: `"input:default"`

        * `":disabled"` :
            Selects every disabled <input> element
            example: `"input:disabled"`

        * `":empty"` :
            Selects every <p> element that has no children (including text nodes)
            example: `"p:empty"`

        * `":enabled"` :
            Selects every enabled <input> element
            example: `"input:enabled"`

        * `":first-child"` :
            Selects every <p> element that is the first child of its parent
            example: `"p:first-child"`

        * `"::first-letter"` :
            Selects the first letter of every <p> element
            example: `"p::first-letter"`

        * `"::first-line"` :
            Selects the first line of every <p> element
            example: `"p::first-line"`

        * `":first-of-type"` :
            Selects every <p> element that is the first <p> element of its parent
            example: `"p:first-of-type"`

        * `":focus"` :
            Selects the input element which has focus
            example: `"input:focus"`

        * `":hover"` :
            Selects links on mouse over
            example: `"a:hover"`

        * `":in-range"` :
            Selects input elements with a value within a specified range
            example: `"input:in-range"`

        * `":indeterminate"` :
            Selects input elements that are in an indeterminate state
            example: `"input:indeterminate"`

        * `":invalid"` :
            Selects all input elements with an invalid value
            example: `"input:invalid"`

        * `":lang(language)"` :
            Selects every <p> element with a lang attribute equal to "it" (Italian)
            example: `"p:lang(it)"`

        * `":last-child"` :
            Selects every <p> element that is the last child of its parent
            example: `"p:last-child"`

        * `":last-of-type"` :
            Selects every <p> element that is the last <p> element of its parent
            example: `"p:last-of-type"`

        * `":link"` :
            Selects all unvisited links
            example: `"a:link"`

        * `":not(selector)"` :
            Selects every element that is not a <p> element
            example: `":not(p)"`

        * `":nth-child(n)"` :
            Selects every <p> element that is the second child of its parent
            example: `"p:nth-child(2)"`

        * `":nth-last-child(n)"` :
            Selects every <p> element that is the second child of its parent, counting from the last child
            example: `"p:nth-last-child(2)"`

        * `":nth-last-of-type(n)"` :
            Selects every <p> element that is the second <p> element of its parent, counting from the last child
            example: `"p:nth-last-of-type(2)"`

        * `":nth-of-type(n)"` :
            Selects every <p> element that is the second <p> element of its parent
            example: `"p:nth-of-type(2)"`

        * `":only-of-type"` :
            Selects every <p> element that is the only <p> element of its parent
            example: `"p:only-of-type"`

        * `":only-child"` :
            Selects every <p> element that is the only child of its parent
            example: `"p:only-child"`

        * `":optional"` :
            Selects input elements with no "required" attribute
            example: `"input:optional"`

        * `":out-of-range"` :
            Selects input elements with a value outside a specified range
            example: `"input:out-of-range"`

        * `"::placeholder"` :
            Selects input elements with placeholder text
            example: `"input::placeholder"`

        * `":read-only"` :
            Selects input elements with the "readonly" attribute specified
            example: `"input:read-only"`

        * `":read-write"` :
            Selects input elements with the "readonly" attribute NOT specified
            example: `"input:read-write"`

        * `":required"` :
            Selects input elements with the "required" attribute specified
            example: `"input:required"`

        * `":root"` :
            Selects the document's root element
            example: `":root"`

        * `"::selection"` :
            Selects the portion of an element that is selected by a user
            example: `"::selection"`

        * `":target"` :
            Selects the current active #news element (clicked on a URL containing that anchor name)
            example: `"#news:target"`

        * `":valid"` :
            Selects all input elements with a valid value
            example: `"input:valid"`

        * `":visited"` :
            Selects all visited links
            example: `"a:visited"`

        """

        return self._selector

    @selector.setter
    def selector(self, value):
        self._selector = value

    def __getattr__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]

        if not item.startswith('_') and item in self.__class__.__dict__:
            return self.__class__.__dict__[item].fget(self)

        raise AttributeError(item)

    def __setattr__(self, key, value):

        if not key.startswith('_'):
            if key in self.__class__.__dict__:
                self.__class__.__dict__[key].fset(self, value)

            return

        self.__dict__[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            del self.__dict__[item]

    def __str__(self, indent=0, html=False):
        if html:
            output = ''

            for key, value in self.__dict__.items():
                if key == '_selector':
                    continue

                if key in (
                    '_charset',
                    '_font_face',
                    '_import',
                    '_keyframes',
                    '_media',
                    '_font-feature-values'
                ):
                    continue

                if isinstance(value, css_base):
                    continue

                if output:
                    output += ' '

                else:
                    attr_name = key[1:]
                    attr = self.__class__.__dict__[attr_name].fget
                    name = attr.__doc__.split('\n')[1].strip()
                    output += name + ': ' + value + ';'

            return output

        else:
            lines = [' ' * indent + self._selector + ' ' + '{']
            for key, value in self.__dict__.items():
                if key == '_selector':
                    continue

                if isinstance(value, css_base):
                    lines += [value.__str__(indent + 4, html)]
                else:
                    attr_name = key[1:]
                    attr_name = attr_name.replace('_', ' ').title()

                    attr_name = attr_name[0].lower() + attr_name[1:]
                    attr_name = attr_name.replace(' ', '')
                    attr = self.__class__.__dict__[attr_name].fget
                    name = attr.__doc__.split('\n')[1].strip()
                    lines += [
                        '    ' + ' ' * indent + name + ': ' + value + ';'
                    ]

            lines += [' ' * indent + '}']

            return '\n'.join(lines)


class font_face(css_base):

    def __init__(self):
        css_base.__init__(self)
        self._selector = '@font-face'

    @property
    def fontFamily(self):
        """
        font-family

        Required. Defines the name of the font.

        * `name`

        """
        return getattr(self, '_font_family', None)

    @fontFamily.setter
    def fontFamily(self, value):
        """
        font-family

        Required. Defines the name of the font.

        * `name`
        """
        setattr(self, '_font_family', value)

    @fontFamily.deleter
    def fontFamily(self):
        delattr(self, '_font_family')

    @property
    def fontStretch(self):
        """
        font-stretch

        Optional. Defines how the font should be stretched. Default value is "normal"

        * `"normal"`
        * `"condensed"`
        * `"ultra-condensed"`
        * `"extra-condensed"`
        * `"semi-condensed"`
        * `"expanded"`
        * `"semi-expanded"`
        * `"extra-expanded"`
        * `"ultra-expanded"`
        """
        return getattr(self, '_font_stretch', None)

    @fontStretch.setter
    def fontStretch(self, value):
        """
        font-stretch

        Optional. Defines how the font should be stretched. Default value is "normal"

        * `"normal"`
        * `"condensed"`
        * `"ultra-condensed"`
        * `"extra-condensed"`
        * `"semi-condensed"`
        * `"expanded"`
        * `"semi-expanded"`
        * `"extra-expanded"`
        * `"ultra-expanded"`
        """
        setattr(self, '_font_stretch', value)

    @fontStretch.deleter
    def fontStretch(self):
        delattr(self, '_font_stretch')

    @property
    def src(self):
        """
        src

        Required. Defines the URL(s) where the font should be downloaded from

        * `"url(sansation_light.woff)"`
        """
        return getattr(self, '_src', None)

    @src.setter
    def src(self, value):
        """
        src

        Required. Defines the URL(s) where the font should be downloaded from

        * `"url(sansation_light.woff)"`
        """
        setattr(self, '_src', value)

    @src.deleter
    def src(self):
        delattr(self, '_src')

    @property
    def fontStyle(self):
        """
        font-style

        Optional. Defines how the font should be styled. Default value is "normal"

        * `"normal"`
        * `"italic"`
        * `"oblique"`

        """
        return getattr(self, '_font_style', None)

    @fontStyle.setter
    def fontStyle(self, value):
        """
        font-style

        Optional. Defines how the font should be styled. Default value is "normal"

        * `"normal"`
        * `"italic"`
        * `"oblique"`
        """
        setattr(self, '_font_style', value)

    @fontStyle.deleter
    def fontStyle(self):
        delattr(self, '_font_style')

    @property
    def fontWeight(self):
        """
        font-weight

        Optional. Defines the boldness of the font. Default value is "normal"

        * `"normal"`
        * `"bold"`
        * `100`
        * `200`
        * `300`
        * `400`
        * `500`
        * `600`
        * `700`
        * `800`
        * `900`
        """
        return getattr(self, '_font_weight', None)

    @fontWeight.setter
    def fontWeight(self, value):
        """
        font-weight

        Optional. Defines the boldness of the font. Default value is "normal"

        * `"normal"`
        * `"bold"`
        * `100`
        * `200`
        * `300`
        * `400`
        * `500`
        * `600`
        * `700`
        * `800`
        * `900`
        """
        setattr(self, '_font_weight', value)

    @fontWeight.deleter
    def fontWeight(self):
        delattr(self, '_font_weight')

    @property
    def unicodeRange(self):
        """
        unicode-range

        Optional. Defines the range of unicode characters the font supports. Default value is "U+0-10FFFF"

        * `unicode-range`
        """
        return getattr(self, '_unicode_range', None)

    @unicodeRange.setter
    def unicodeRange(self, value):
        """
        unicode-range

        Optional. Defines the range of unicode characters the font supports. Default value is "U+0-10FFFF"

        * `unicode-range`
        """
        setattr(self, '_unicode_range', value)

    @unicodeRange.deleter
    def unicodeRange(self):
        delattr(self, '_align_content')


class css(css_base):

    def __init__(self, selector='*'):
        css_base.__init__(self)
        self._selector = selector

    @property
    def alignContent(self):
        """
        align-content

        Specifies the alignment between the lines inside a flexible container when the items do not use all available space

        object.style.alignContent = "stretch|center|flex-start|flex-end|space-between|space-around|initial|inherit"

        * `"stretch"`: Default value. Lines stretch to take up the remaining space
        * `"center"`: Lines are packed toward the center of the flex container
        * `"flex-start"`: Lines are packed toward the start of the flex container
        * `"flex-end"`: Lines are packed toward the end of the flex container
        * `"space-between"`: Lines are evenly distributed in the flex container
        * `"space-around"`: Lines are evenly distributed in the flex container, with half-size spaces on either end
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_align_content', None)

    @alignContent.setter
    def alignContent(self, value):
        setattr(self, '_align_content', value)

    @alignContent.deleter
    def alignContent(self):
        delattr(self, '_align_content')

    @property
    def alignItems(self):
        """
        align-items

        Specifies the alignment for items inside a flexible container

        object.style.alignItems = "stretch|center|flex-start|flex-end|baseline|initial|inherit"

        * `"stretch"`: Default. Items are stretched to fit the container
        * `"center"`: Items are positioned at the center of the container
        * `"flex-start"`: Items are positioned at the beginning of the container
        * `"flex-end"`: Items are positioned at the end of the container
        * `"baseline"`: Items are positioned at the baseline of the container
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_align_items', None)

    @alignItems.setter
    def alignItems(self, value):
        setattr(self, '_align_items', value)

    @alignItems.deleter
    def alignItems(self):
        delattr(self, '_align_items')

    @property
    def alignSelf(self):
        """
        align-self

        Specifies the alignment for selected items inside a flexible container

        object.style.alignSelf = "auto|stretch|center|flex-start|flex-end|baseline|initial|inherit"

        * `"auto"`: Default. The element inherits its parent container's align-items property, or "stretch" if it has no parent container
        * `"stretch"`: The element is positioned to fit the container
        * `"center"`: The element is positioned at the center of the container
        * `"flex-start"`: The element is positioned at the beginning of the container
        * `"flex-end"`: The element is positioned at the end of the container
        * `"baseline"`: The element is positioned at the baseline of the container
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_align_self', None)

    @alignSelf.setter
    def alignSelf(self, value):
        setattr(self, '_align_self', value)

    @alignSelf.deleter
    def alignSelf(self):
        delattr(self, '_align_self')

    @property
    def all(self):
        """
        all

        Resets all properties (except unicode-bidi and direction)

        object.style.all = "initial|inherit|unset"

        * `"initial"`: Changes all the properties applied to the element or the element's parent to their initial value
        * `"inherit"`: Changes all the properties applied to the element or the element's parent to their parent value
        * `"unset"`: Changes all the properties applied to the element or the element's parent to their parent value if they are inheritable or to their initial value if not
        """
        return getattr(self, '_all', None)

    @all.setter
    def all(self, value):
        setattr(self, '_all', value)

    @all.deleter
    def all(self):
        delattr(self, '_all')

    @property
    def animation(self):
        """
        animation

        A shorthand property for all the animation-* properties

        object.style.animation = "name duration timing-function delay iteration-count direction fill-mode play-state"

        * `"animation-name"`: Specifies the name of the keyframe you want to bind to the selector
        * `"animation-duration"`: Specifies how many seconds or milliseconds an animation takes to complete
        * `" animation-timing-function"`: Specifies the speed curve of the animation
        * `"animation-delay"`: Specifies a delay before the animation will start
        * `" animation-iteration-count"`: Specifies how many times an animation should be played
        * `"animation-direction"`: Specifies whether or not the animation should play in reverse on alternate cycles
        * `""`: Specifies what values are applied by the animation outside the time it is executing
        * `""`: Specifies whether the animation is running or paused
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation', None)

    @animation.setter
    def animation(self, value):
        setattr(self, '_animation', value)

    @animation.deleter
    def animation(self):
        delattr(self, '_animation')

    @property
    def animationDelay(self):
        """
        animation-delay

        Specifies a delay for the start of an animation

        object.style.animationDelay = "time|initial|inherit"

        * `"time"`: Optional. Defines the number of seconds (s) or milliseconds (ms) to wait before the animation will start. Default value is 0. Negative values are allowed. If you use negative values, the animation will start as if it had already been playing for N seconds/milliseconds.
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_delay', None)

    @animationDelay.setter
    def animationDelay(self, value):
        setattr(self, '_animation_delay', value)

    @animationDelay.deleter
    def animationDelay(self):
        delattr(self, '_animation_delay')

    @property
    def animationDirection(self):
        """
        animation-direction

        Specifies whether an animation should be played forwards, backwards or
    in alternate cycles

        object.style.animationDirection = "normal|reverse|alternate|alternate-reverse|initial|inherit"

        * `"normal"`: Default value. The animation is played as normal (forwards)
        * `"reverse"`: The animation is played in reverse direction (backwards)
        * `"alternate"`: The animation is played forwards first, then backwards
        * `"alternate-reverse"`: The animation is played backwards first, then forwards
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_direction', None)

    @animationDirection.setter
    def animationDirection(self, value):
        setattr(self, '_animation_direction', value)

    @animationDirection.deleter
    def animationDirection(self):
        delattr(self, '_animation_direction')

    @property
    def animationDuration(self):
        """
        animation-duration

        Specifies how long an animation should take to complete one cycle

        object.style.animationDuration = "time|initial|inherit"

        * `"time"`: Specifies the length of time an animation should take to complete one cycle. This can be specified in seconds or milliseconds. Default value is 0, which means that no animation will occur
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_duration', None)

    @animationDuration.setter
    def animationDuration(self, value):
        setattr(self, '_animation_duration', value)

    @animationDuration.deleter
    def animationDuration(self):
        delattr(self, '_animation_duration')

    @property
    def animationFillMode(self):
        """
        animation-fill-mode

        Specifies a style for the element when the animation is not playing (before
    it starts, after it ends, or both)

        object.style.animationFillMode = "none|forwards|backwards|both|initial|inherit"

        * `"none"`: Default value. Animation will not apply any styles to the element before or after it is executing
        * `"forwards"`: The element will retain the style values that is set by the last keyframe (depends on animation-direction and animation-iteration-count)
        * `"backwards"`: The element will get the style values that is set by the first keyframe (depends on animation-direction), and retain this during the animation-delay period
        * `"both"`: The animation will follow the rules for both forwards and backwards, extending the animation properties in both directions
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_fill_mode', None)

    @animationFillMode.setter
    def animationFillMode(self, value):
        setattr(self, '_animation_fill_mode', value)

    @animationFillMode.deleter
    def animationFillMode(self):
        delattr(self, '_animation_fill_mode')

    @property
    def animationIterationCount(self):
        """
        animation-iteration-count

        Specifies the number of times an animation should be played

        object.style.animationIterationCount = "number|infinite|initial|inherit"

        * `"number"`: A number that defines how many times an animation should be played. Default value is 1
        * `"infinite"`: Specifies that the animation should be played infinite times (for ever)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_iteration_count', None)

    @animationIterationCount.setter
    def animationIterationCount(self, value):
        setattr(self, '_animation_iteration_count', value)

    @animationIterationCount.deleter
    def animationIterationCount(self):
        delattr(self, '_animation_iteration_count')

    @property
    def animationName(self):
        """
        animation-name

        Specifies a name for the @keyframes animation

        object.style.animationName = "keyframename|none|initial|inherit"

        * `"keyframename"`: Specifies the name of the keyframe you want to bind to the selector
        * `"none"`: Default value. Specifies that there will be no animation (can be used to override animations coming from the cascade)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_name', None)

    @animationName.setter
    def animationName(self, value):
        setattr(self, '_animation_name', value)

    @animationName.deleter
    def animationName(self):
        delattr(self, '_animation_name')

    @property
    def animationPlayState(self):
        """
        animation-play-state

        Specifies whether the animation is running or paused

        object.style.animationPlayState = "paused|running|initial|inherit"

        * `"paused"`: Specifies that the animation is paused
        * `"running"`: Default value. Specifies that the animation is running
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_play_state', None)

    @animationPlayState.setter
    def animationPlayState(self, value):
        setattr(self, '_animation_play_state', value)

    @animationPlayState.deleter
    def animationPlayState(self):
        delattr(self, '_animation_play_state')

    @property
    def animationTimingFunction(self):
        """
        animation-timing-function

        Specifies the speed curve of an animation

        object.style.animationTimingFunction = "linear|ease|ease-in|ease-out|ease-in-out|step-start|step-end|steps(int,start|end)|cubic-bezier(n,n,n,n)|initial|inherit"

        * `"linear"`: The animation has the same speed from start to end
        * `"ease"`: Default value. The animation has a slow start, then fast, before it ends slowly
        * `"ease-in"`: The animation has a slow start
        * `"ease-out"`: The animation has a slow end
        * `"ease-in-out"`: The animation has both a slow start and a slow end
        * `"step-start"`: Equivalent to steps(1, start)
        * `"step-end"`: Equivalent to steps(1, end)
        * `"steps(int,start|end)"`: Specifies a stepping function, with two parameters. The first parameter specifies the number of intervals in the function. It must be a positive integer (greater than 0). The second parameter, which is optional, is either the value &quot;start&quot; or &quot;end&quot;, and specifies the point at which the change of values occur within the interval. If the second parameter is omitted, it is given the value &quot;end&quot;
        * `"cubic-bezier(n,n,n,n)"`: Define your own values in the cubic-bezier function Possible values are numeric values from 0 to 1
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_animation_timing_function', None)

    @animationTimingFunction.setter
    def animationTimingFunction(self, value):
        setattr(self, '_animation_timing_function', value)

    @animationTimingFunction.deleter
    def animationTimingFunction(self):
        delattr(self, '_animation_timing_function')

    @property
    def backfaceVisibility(self):
        """
        backface-visibility

        Defines whether or not the back face of an element should be visible when facing the user

        object.style.backfaceVisibility = "visible|hidden|initial|inherit"

        * `"visible"`: Default value. The backside is visible
        * `"hidden"`: The backside is not visible
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_backface_visibility', None)

    @backfaceVisibility.setter
    def backfaceVisibility(self, value):
        setattr(self, '_backface_visibility', value)

    @backfaceVisibility.deleter
    def backfaceVisibility(self):
        delattr(self, '_backface_visibility')

    @property
    def background(self):
        """
        background

        A shorthand property for all the background-* properties

        object.style.background = "bg-color bg-image position/bg-size bg-repeat bg-origin bg-clip bg-attachment initial|inherit"

        * `"background-color"`: Specifies the background color to be used
        * `"background-image"`: Specifies ONE or MORE background images to be used
        * `"background-position"`: Specifies the position of the background images
        * `"background-size"`: Specifies the size of the background images
        * `"background-repeat"`: Specifies how to repeat the background images
        * `"background-origin"`: Specifies the positioning area of the background images
        * `"background-clip"`: Specifies the painting area of the background images
        * `"background-attachment"`: Specifies whether the background images are fixed or scrolls with the rest of the page
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background', None)

    @background.setter
    def background(self, value):
        setattr(self, '_background', value)

    @background.deleter
    def background(self):
        delattr(self, '_background')

    @property
    def backgroundAttachment(self):
        """
        background-attachment

        Sets whether a background image scrolls with the rest of the page, or is fixed

        object.style.backgroundAttachment = "scroll|fixed|local|initial|inherit"

        * `"scroll"`: The background image will scroll with the page. This is default
        * `"fixed"`: The background image will not scroll with the page
        * `"local"`: The background image will scroll with the element's contents
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_attachment', None)

    @backgroundAttachment.setter
    def backgroundAttachment(self, value):
        setattr(self, '_background_attachment', value)

    @backgroundAttachment.deleter
    def backgroundAttachment(self):
        delattr(self, '_background_attachment')

    @property
    def backgroundBlendMode(self):
        """
        background-blend-mode

        Specifies the blending mode of each background layer (color/image)

        object.style.backgroundBlendMode = "normal|multiply|screen|overlay|darken|lighten|color-dodge|saturation|color|luminosity"

        * `"normal"`: This is default. Sets the blending mode to normal
        * `"multiply"`: Sets the blending mode to multiply
        * `"screen"`: Sets the blending mode to screen
        * `"overlay"`: Sets the blending mode to overlay
        * `"darken"`: Sets the blending mode to darken
        * `"lighten"`: Sets the blending mode to lighten
        * `"color-dodge"`: Sets the blending mode to color-dodge
        * `"saturation"`: Sets the blending mode to saturation
        * `"color"`: Sets the blending mode to color
        * `"luminosity"`: Sets the blending mode to luminosity
        """
        return getattr(self, '_background_blend_mode', None)

    @backgroundBlendMode.setter
    def backgroundBlendMode(self, value):
        setattr(self, '_background_blend_mode', value)

    @backgroundBlendMode.deleter
    def backgroundBlendMode(self):
        delattr(self, '_background_blend_mode')

    @property
    def backgroundClip(self):
        """
        background-clip

        Defines how far the background (color or image) should extend within an
    element

        object.style.backgroundClip = "border-box|padding-box|content-box|initial|inherit"

        * `"border-box"`: Default value. The background extends behind the border
        * `"padding-box"`: The background extends to the inside edge of the border
        * `"content-box"`: The background extends to the edge of the content box
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_clip', None)

    @backgroundClip.setter
    def backgroundClip(self, value):
        setattr(self, '_background_clip', value)

    @backgroundClip.deleter
    def backgroundClip(self):
        delattr(self, '_background_clip')

    @property
    def backgroundColor(self):
        """
        background-color

        Specifies the background color of an element

        object.style.backgroundColor = "color|transparent|initial|inherit"

        * `"color"`: Specifies the background color. Look at  CSS Color Values for a complete list of possible color values.
        * `"transparent"`: Specifies that the background color should be transparent. This is default
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_color', None)

    @backgroundColor.setter
    def backgroundColor(self, value):
        setattr(self, '_background_color', value)

    @backgroundColor.deleter
    def backgroundColor(self):
        delattr(self, '_background_color')

    @property
    def backgroundImage(self):
        """
        background-image

        Specifies one or more background images for an element

        object.style.backgroundImage = "url|none|initial|inherit"

        * `"url('URL')"`: The URL to the image. To specify more than one image, separate the URLs with a comma
        * `"none"`: No background image will be displayed. This is default
        * `"linear-gradient()"`: Sets a linear gradient as the background image. Define at least two colors (top to bottom)
        * `"radial-gradient()"`: Sets a radial gradient as the background image. Define at least two colors (center to edges)
        * `"repeating-linear-gradient()"`: Repeats a linear gradient
        * `"repeating-radial-gradient()"`: Repeats a radial gradient
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_image', None)

    @backgroundImage.setter
    def backgroundImage(self, value):
        setattr(self, '_background_image', value)

    @backgroundImage.deleter
    def backgroundImage(self):
        delattr(self, '_background_image')

    @property
    def backgroundOrigin(self):
        """
        background-origin

        Specifies the origin position of a background image

        object.style.backgroundOrigin = "padding-box|border-box|content-box|initial|inherit"

        * `"padding-box"`: Default value. The background image starts from the upper left corner of the padding edge
        * `"border-box"`: The background image starts from the upper left corner of the border
        * `"content-box"`: The background image starts from the upper left corner of the content
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_origin', None)

    @backgroundOrigin.setter
    def backgroundOrigin(self, value):
        setattr(self, '_background_origin', value)

    @backgroundOrigin.deleter
    def backgroundOrigin(self):
        delattr(self, '_background_origin')

    @property
    def backgroundPosition(self):
        """
        background-position

        Specifies the position of a background image

        object.style.backgroundPosition = "value"

        * `" left center"`: If you only specify one keyword, the other value will be &quot;center&quot;
        * `"x% y%"`: The first value is the horizontal position and the second value is the vertical. The top left corner is 0% 0%. The right bottom corner is 100% 100%. If you only specify one value, the other value will be 50%. . Default value is: 0% 0%
        * `"xpos ypos"`: The first valueis the horizontal position and the second value is the vertical. The top left corner is 0 0. Units can be pixels (0px 0px) or any other CSS units. If you only specify one value, the other value will be 50%. You can mix % and positions
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_position', None)

    @backgroundPosition.setter
    def backgroundPosition(self, value):
        setattr(self, '_background_position', value)

    @backgroundPosition.deleter
    def backgroundPosition(self):
        delattr(self, '_background_position')

    @property
    def backgroundRepeat(self):
        """
        background-repeat

        Sets if/how a background image will be repeated

        object.style.backgroundRepeat = "repeat|repeat-x|repeat-y|no-repeat|initial|inherit"

        * `"repeat"`: The background image is repeated both vertically and horizontally. The last image will be clipped if it does not fit. This is default
        * `"repeat-x"`: The background image is repeated only horizontally
        * `"repeat-y"`: The background image is repeated only vertically
        * `"no-repeat"`: The background-image is not repeated. The image will only be shown once
        * `"space"`: The background-image is repeated as much as possible without clipping. The first and last images are pinned to either side of the element, and whitespace is distributed evenly between the images
        * `"round"`: The background-image is repeated and squished or stretched to fill the space (no gaps)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_repeat', None)

    @backgroundRepeat.setter
    def backgroundRepeat(self, value):
        setattr(self, '_background_repeat', value)

    @backgroundRepeat.deleter
    def backgroundRepeat(self):
        delattr(self, '_background_repeat')

    @property
    def backgroundSize(self):
        """
        background-size

        Specifies the size of the background images

        object.style.backgroundSize = "auto|length|cover|contain|initial|inherit"

        * `"auto"`: Default value. The background image is displayed in its original size
        * `"length"`: Sets the width and height of the background image. The first value sets the width, the second value sets the height. If only one value is given, the second is set to &quot;auto&quot;. Read about length units
        * `"percentage"`: Sets the width and height of the background image in percent of the parent element. The first value sets the width, the second value sets the height. If only one value is given, the second is set to &quot;auto&quot;
        * `"cover"`: Resize the background image to cover the entire container, even if it has to stretch the image or cut a little bit off one of the edges
        * `"contain"`: Resize the background image to make sure the image is fully visible
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_background_size', None)

    @backgroundSize.setter
    def backgroundSize(self, value):
        setattr(self, '_background_size', value)

    @backgroundSize.deleter
    def backgroundSize(self):
        delattr(self, '_background_size')

    @property
    def border(self):
        """
        border

        A shorthand property for border-width, border-style and border-color

        object.style.border = "border-width border-style border-color|initial|inherit"

        * `"border-width"`: Specifies the width of the border. Default value is "medium"
        * `"border-style"`: Specifies the style of the border. Default value is "none"
        * `"border-color"`: Specifies the color of the border. Default value is the color of the text
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border', None)

    @border.setter
    def border(self, value):
        setattr(self, '_border', value)

    @border.deleter
    def border(self):
        delattr(self, '_border')

    @property
    def borderBottom(self):
        """
        border-bottom

        A shorthand property for border-bottom-width, border-bottom-style
    and border-bottom-color

        object.style.borderBottom = "border-width border-style border-color|initial|inherit"

        * `"border-bottom-width"`: Required. Specifies the width of the bottom border. Default value is &quot;medium&quot;
        * `"border-bottom-style"`: Required. Specifies the style of the bottom border. Default value is &quot;none&quot;
        * `"border-bottom-color"`: Optional. Specifies the color of the bottom border. Default value is the color of the text
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_bottom', None)

    @borderBottom.setter
    def borderBottom(self, value):
        setattr(self, '_border_bottom', value)

    @borderBottom.deleter
    def borderBottom(self):
        delattr(self, '_border_bottom')

    @property
    def borderBottomColor(self):
        """
        border-bottom-color

        Sets the color of the bottom border

        object.style.borderBottomColor = "color|transparent|initial|inherit"

        * `"color"`: Specifies the background color. Look at  CSS Color Values for a complete list of possible color values. Default color is the color of the element
        * `"transparent"`: Specifies that the border color should be transparent
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_bottom_color', None)

    @borderBottomColor.setter
    def borderBottomColor(self, value):
        setattr(self, '_border_bottom_color', value)

    @borderBottomColor.deleter
    def borderBottomColor(self):
        delattr(self, '_border_bottom_color')

    @property
    def borderBottomLeftRadius(self):
        """
        border-bottom-left-radius

        Defines the radius of the border of the bottom-left corner

        object.style.borderBottomLeftRadius = "length|% [length|%]|initial|inherit"

        * `"length"`: Defines the shape of the bottom-left corner. Default value is 0. Read about length units
        * `"%"`: Defines the shape of the bottom-left corner in %
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_bottom_left_radius', None)

    @borderBottomLeftRadius.setter
    def borderBottomLeftRadius(self, value):
        setattr(self, '_border_bottom_left_radius', value)

    @borderBottomLeftRadius.deleter
    def borderBottomLeftRadius(self):
        delattr(self, '_border_bottom_left_radius')

    @property
    def borderBottomRightRadius(self):
        """
        border-bottom-right-radius

        Defines the radius of the border of the bottom-right corner

        object.style.borderBottomRightRadius = "length|% [length|%]|initial|inherit"

        * `"length"`: Defines the shape of the bottom-right corner. Default value is 0. Read about length units
        * `"%"`: Defines the shape of the bottom-right corner in %
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_bottom_right_radius', None)

    @borderBottomRightRadius.setter
    def borderBottomRightRadius(self, value):
        setattr(self, '_border_bottom_right_radius', value)

    @borderBottomRightRadius.deleter
    def borderBottomRightRadius(self):
        delattr(self, '_border_bottom_right_radius')

    @property
    def borderBottomStyle(self):
        """
        border-bottom-style

        Sets the style of the bottom border

        object.style.borderBottomStyle = "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|initial|inherit"

        * `"none"`: Specifies no border. This is default
        * `"hidden"`: The same as &quot;none&quot;, except in border conflict resolution for table elements
        * `"dotted"`: Specifies a dotted border
        * `"dashed"`: Specifies a dashed border
        * `"solid"`: Specifies a solid border
        * `"double"`: Specifies a double border
        * `"groove"`: Specifies a 3D grooved border. The effect depends on the border-color value
        * `"ridge"`: Specifies a 3D ridged border. The effect depends on the border-color value
        * `"inset"`: Specifies a 3D inset border. The effect depends on the border-color value
        * `"outset"`: Specifies a 3D outset border. The effect depends on the border-color value
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_bottom_style', None)

    @borderBottomStyle.setter
    def borderBottomStyle(self, value):
        setattr(self, '_border_bottom_style', value)

    @borderBottomStyle.deleter
    def borderBottomStyle(self):
        delattr(self, '_border_bottom_style')

    @property
    def borderBottomWidth(self):
        """
        border-bottom-width

        Sets the width of the bottom border

        object.style.borderBottomWidth = "medium|thin|thick|length|initial|inherit"

        * `"medium"`: Specifies a medium bottom border. This is default
        * `"thin"`: Specifies a thin bottom border
        * `"thick"`: Specifies a thick bottom border
        * `"length"`: Allows you to define the thickness of the bottom border. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_bottom_width', None)

    @borderBottomWidth.setter
    def borderBottomWidth(self, value):
        setattr(self, '_border_bottom_width', value)

    @borderBottomWidth.deleter
    def borderBottomWidth(self):
        delattr(self, '_border_bottom_width')

    @property
    def borderCollapse(self):
        """
        border-collapse

        Sets whether table borders should collapse into a single border or be separated

        object.style.borderCollapse = "separate|collapse|initial|inherit"

        * `"separate"`: Borders are separated; each cell will display its own borders. This is default.
        * `"collapse"`: Borders are collapsed into a single border when possible (border-spacing and empty-cells properties have no effect)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_collapse', None)

    @borderCollapse.setter
    def borderCollapse(self, value):
        setattr(self, '_border_collapse', value)

    @borderCollapse.deleter
    def borderCollapse(self):
        delattr(self, '_border_collapse')

    @property
    def borderColor(self):
        """
        border-color

        Sets the color of the four borders

        object.style.borderColor = "color|transparent|initial|inherit"

        * `"color"`: Specifies the background color. Look at  CSS Color Values for a complete list of possible color values. Default color is black
        * `"transparent"`: Specifies that the border color should be transparent
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_color', None)

    @borderColor.setter
    def borderColor(self, value):
        setattr(self, '_border_color', value)

    @borderColor.deleter
    def borderColor(self):
        delattr(self, '_border_color')

    @property
    def borderImage(self):
        """
        border-image

        A shorthand property for all the border-image-* properties

        object.style.borderImage = "source slice width outset repeat|initial|inherit"

        * `"border-image-source"`: The path to the image to be used as a border
        * `"border-image-slice"`: How to slice the border image
        * `"border-image-width"`: The width of the border image
        * `"border-image-outset"`: The amount by which the border image area extends beyond the border box
        * `"border-image-repeat"`: Whether the border image should be repeated, rounded or stretched
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_image', None)

    @borderImage.setter
    def borderImage(self, value):
        setattr(self, '_border_image', value)

    @borderImage.deleter
    def borderImage(self):
        delattr(self, '_border_image')

    @property
    def borderImageOutset(self):
        """
        border-image-outset

        Specifies the amount by which the border image area extends beyond the border box

        object.style.borderImageOutset = "length|number|initial|inherit"

        * `"length"`: A length unit specifying how far from the edges the border-image will appear. Default value is 0
        * `"number"`: Represent multiples of the corresponding border-width
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_image_outset', None)

    @borderImageOutset.setter
    def borderImageOutset(self, value):
        setattr(self, '_border_image_outset', value)

    @borderImageOutset.deleter
    def borderImageOutset(self):
        delattr(self, '_border_image_outset')

    @property
    def borderImageRepeat(self):
        """
        border-image-repeat

        Specifies whether the border image should be repeated, rounded or stretched

        object.style.borderImageRepeat = "stretch|repeat|round|initial|inherit"

        * `"stretch"`: Default value. The image is stretched to fill the area
        * `"repeat"`: The image is tiled (repeated) to fill the area
        * `"round"`: The image is tiled (repeated) to fill the area. If it does not fill the area with a whole number of tiles, the image is rescaled so it fits
        * `"space"`: The image is tiled (repeated) to fill the area. If it does not fill the area with a whole number of tiles, the extra space is distributed around the tiles
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_image_repeat', None)

    @borderImageRepeat.setter
    def borderImageRepeat(self, value):
        setattr(self, '_border_image_repeat', value)

    @borderImageRepeat.deleter
    def borderImageRepeat(self):
        delattr(self, '_border_image_repeat')

    @property
    def borderImageSlice(self):
        """
        border-image-slice

        Specifies how to slice the border image

        object.style.borderImageSlice = "number|%|fill|initial|inherit"

        * `"number"`: The number(s) represent pixels for raster images or coordinates for vector images
        * `"%"`: Percentages are relative to the height or width of the image
        * `"fill"`: Causes the middle part of the image to be displayed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_image_slice', None)

    @borderImageSlice.setter
    def borderImageSlice(self, value):
        setattr(self, '_border_image_slice', value)

    @borderImageSlice.deleter
    def borderImageSlice(self):
        delattr(self, '_border_image_slice')

    @property
    def borderImageSource(self):
        """
        border-image-source

        Specifies the path to the image to be used as a border

        object.style.borderImageSource = "none|image|initial|inherit"

        * `"none"`: No image will be used
        * `"image"`: The path to the image to be used as a border
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_image_source', None)

    @borderImageSource.setter
    def borderImageSource(self, value):
        setattr(self, '_border_image_source', value)

    @borderImageSource.deleter
    def borderImageSource(self):
        delattr(self, '_border_image_source')

    @property
    def borderImageWidth(self):
        """
        border-image-width

        Specifies the width of the border image

        object.style.borderImageWidth = "number|%|auto|initial|inherit"

        * `"length"`: A length unit (px) specifying the size of the border-width
        * `"number"`: Default value 1. Represents multiples of the corresponding border-width
        * `"%"`: Refers to the size of the border image area: the width of the area for horizontal offsets, the height for vertical offsets
        * `"auto"`: If specified, the width is the intrinsic width or height of the corresponding image slice
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_image_width', None)

    @borderImageWidth.setter
    def borderImageWidth(self, value):
        setattr(self, '_border_image_width', value)

    @borderImageWidth.deleter
    def borderImageWidth(self):
        delattr(self, '_border_image_width')

    @property
    def borderLeft(self):
        """
        border-left

        A shorthand property for all the border-left-* properties

        object.style.borderLeft = "border-width border-style border-color|initial|inherit"

        * `"border-left-width"`: Optional. Specifies the width of the left border. Default value is &quot;medium&quot;
        * `"border-left-style"`: Required. Specifies the style of the left border. Default value is &quot;none&quot;
        * `"border-left-color"`: Optional. Specifies the color of the left border. Default value is the color of the text
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_left', None)

    @borderLeft.setter
    def borderLeft(self, value):
        setattr(self, '_border_left', value)

    @borderLeft.deleter
    def borderLeft(self):
        delattr(self, '_border_left')

    @property
    def borderLeftColor(self):
        """
        border-left-color

        Sets the color of the left border

        object.style.borderLeftColor = "color|transparent|initial|inherit"

        * `"color"`: Specifies the color of the left border. Look at CSS Color Values for a complete list of possible color values. Default color is the color of the element
        * `"transparent"`: Specifies that the border color should be transparent
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_left_color', None)

    @borderLeftColor.setter
    def borderLeftColor(self, value):
        setattr(self, '_border_left_color', value)

    @borderLeftColor.deleter
    def borderLeftColor(self):
        delattr(self, '_border_left_color')

    @property
    def borderLeftStyle(self):
        """
        border-left-style

        Sets the style of the left border

        object.style.borderLeftStyle = "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|initial|inherit"

        * `"none"`: Specifies no border. This is default
        * `"hidden"`: The same as &quot;none&quot;, except in border conflict resolution for table elements
        * `"dotted"`: Specifies a dotted border
        * `"dashed"`: Specifies a dashed border
        * `"solid"`: Specifies a solid border
        * `"double"`: Specifies a double border
        * `"groove"`: Specifies a 3D grooved border. The effect depends on the border-color value
        * `"ridge"`: Specifies a 3D ridged border. The effect depends on the border-color value
        * `"inset"`: Specifies a 3D inset border. The effect depends on the border-color value
        * `"outset"`: Specifies a 3D outset border. The effect depends on the border-color value
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_left_style', None)

    @borderLeftStyle.setter
    def borderLeftStyle(self, value):
        setattr(self, '_border_left_style', value)

    @borderLeftStyle.deleter
    def borderLeftStyle(self):
        delattr(self, '_border_left_style')

    @property
    def borderLeftWidth(self):
        """
        border-left-width

        Sets the width of the left border

        object.style.borderLeftWidth = "medium|thin|thick|length|initial|inherit"

        * `"medium"`: Specifies a medium left border. This is default
        * `"thin"`: Specifies a thin left border
        * `"thick"`: Specifies a thick left border
        * `"length"`: Allows you to define the thickness of the left border. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_left_width', None)

    @borderLeftWidth.setter
    def borderLeftWidth(self, value):
        setattr(self, '_border_left_width', value)

    @borderLeftWidth.deleter
    def borderLeftWidth(self):
        delattr(self, '_border_left_width')

    @property
    def borderRadius(self):
        """
        border-radius

        A shorthand property for the four border-*-radius properties

        object.style.borderRadius = "1-4 length|% / 1-4 length|%|initial|inherit"

        * `"length"`: Defines the shape of the corners. Default value is 0. Read about length units
        * `"%"`: Defines the shape of the corners in %
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_radius', None)

    @borderRadius.setter
    def borderRadius(self, value):
        setattr(self, '_border_radius', value)

    @borderRadius.deleter
    def borderRadius(self):
        delattr(self, '_border_radius')

    @property
    def borderRight(self):
        """
        border-right

        A shorthand property for all the border-right-* properties

        object.style.borderRight = "border-width border-style border-color|initial|inherit"

        * `"border-right-width"`: Required. Specifies the width of the right border. Default value is &quot;medium&quot;
        * `"border-right-style"`: Required. Specifies the style of the right border. Default value is &quot;none&quot;
        * `"border-right-color"`: Optional. Specifies the color of the right border. Default value is the color of the text
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_right', None)

    @borderRight.setter
    def borderRight(self, value):
        setattr(self, '_border_right', value)

    @borderRight.deleter
    def borderRight(self):
        delattr(self, '_border_right')

    @property
    def borderRightColor(self):
        """
        border-right-color

        Sets the color of the right border

        object.style.borderRightColor = "color|transparent|initial|inherit"

        * `"color"`: Specifies the color of the right border. Look at CSS Color Values for a complete list of possible color values. Default color is black
        * `"transparent"`: Specifies that the border color should be transparent
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_right_color', None)

    @borderRightColor.setter
    def borderRightColor(self, value):
        setattr(self, '_border_right_color', value)

    @borderRightColor.deleter
    def borderRightColor(self):
        delattr(self, '_border_right_color')

    @property
    def borderRightStyle(self):
        """
        border-right-style

        Sets the style of the right border

        object.style.borderRightStyle = "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|initial|inherit"

        * `"none"`: Specifies no border. This is default
        * `"hidden"`: The same as &quot;none&quot;, except in border conflict resolution for table elements
        * `"dotted"`: Specifies a dotted border
        * `"dashed"`: Specifies a dashed border
        * `"solid"`: Specifies a solid border
        * `"double"`: Specifies a double border
        * `"groove"`: Specifies a 3D grooved border. The effect depends on the border-color value
        * `"ridge"`: Specifies a 3D ridged border. The effect depends on the border-color value
        * `"inset"`: Specifies a 3D inset border. The effect depends on the border-color value
        * `"outset"`: Specifies a 3D outset border. The effect depends on the border-color value
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_right_style', None)

    @borderRightStyle.setter
    def borderRightStyle(self, value):
        setattr(self, '_border_right_style', value)

    @borderRightStyle.deleter
    def borderRightStyle(self):
        delattr(self, '_border_right_style')

    @property
    def borderRightWidth(self):
        """
        border-right-width

        Sets the width of the right border

        object.style.borderRightWidth = "medium|thin|thick|length|initial|inherit"

        * `"medium"`: Specifies a medium right border. This is default
        * `"thin"`: Specifies a thin right border
        * `"thick"`: Specifies a thick right border
        * `"length"`: Allows you to define the thickness of the right border. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_right_width', None)

    @borderRightWidth.setter
    def borderRightWidth(self, value):
        setattr(self, '_border_right_width', value)

    @borderRightWidth.deleter
    def borderRightWidth(self):
        delattr(self, '_border_right_width')

    @property
    def borderSpacing(self):
        """
        border-spacing

        Sets the distance between the borders of adjacent cells

        object.style.borderSpacing = "length|initial|inherit"

        * `"length length"`: Specifies the distance between the borders of adjacent cells in px, cm, etc. Negative values are not allowed. If one  value is specified, it defines both the horizontal and vertical spacing between cells If two values are specified, the first sets the horizontal spacing and the second sets the vertical spacing
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_spacing', None)

    @borderSpacing.setter
    def borderSpacing(self, value):
        setattr(self, '_border_spacing', value)

    @borderSpacing.deleter
    def borderSpacing(self):
        delattr(self, '_border_spacing')

    @property
    def borderStyle(self):
        """
        border-style

        Sets the style of the four borders

        object.style.borderStyle = "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|initial|inherit"

        * `"none"`: Default value. Specifies no border
        * `"hidden"`: The same as &quot;none&quot;, except in border conflict resolution for table elements
        * `"dotted"`: Specifies a dotted border
        * `"dashed"`: Specifies a dashed border
        * `"solid"`: Specifies a solid border
        * `"double"`: Specifies a double border
        * `"groove"`: Specifies a 3D grooved border. The effect depends on the border-color value
        * `"ridge"`: Specifies a 3D ridged border. The effect depends on the border-color value
        * `"inset"`: Specifies a 3D inset border. The effect depends on the border-color value
        * `"outset"`: Specifies a 3D outset border. The effect depends on the border-color value
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_style', None)

    @borderStyle.setter
    def borderStyle(self, value):
        setattr(self, '_border_style', value)

    @borderStyle.deleter
    def borderStyle(self):
        delattr(self, '_border_style')

    @property
    def borderTop(self):
        """
        border-top

        A shorthand property for border-top-width, border-top-style and
    border-top-color

        object.style.borderTop = "border-width border-style border-color|initial|inherit"

        * `"border-top-width"`: Required. Specifies the width of the top border. Default value is &quot;medium&quot;
        * `"border-top-style"`: Required. Specifies the style of the top border. Default value is &quot;none&quot;
        * `"border-top-color"`: Optional. Specifies the color of the top border. Default value is the color of the text
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_top', None)

    @borderTop.setter
    def borderTop(self, value):
        setattr(self, '_border_top', value)

    @borderTop.deleter
    def borderTop(self):
        delattr(self, '_border_top')

    @property
    def borderTopColor(self):
        """
        border-top-color

        Sets the color of the top border

        object.style.borderTopColor = "color|transparent|initial|inherit"

        * `"color"`: Specifies the color of the top border. Look at CSS Color Values for a complete list of possible color values. Default color is the color of the element
        * `"transparent"`: Specifies that the border color should be transparent
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_top_color', None)

    @borderTopColor.setter
    def borderTopColor(self, value):
        setattr(self, '_border_top_color', value)

    @borderTopColor.deleter
    def borderTopColor(self):
        delattr(self, '_border_top_color')

    @property
    def borderTopLeftRadius(self):
        """
        border-top-left-radius

        Defines the radius of the border of the top-left corner

        object.style.borderTopLeftRadius = "length|% [length|%]|initial|inherit"

        * `"length"`: Defines the shape of the top-left corner. Read about length units
        * `"%"`: Defines the shape of the top-left corner in %
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_top_left_radius', None)

    @borderTopLeftRadius.setter
    def borderTopLeftRadius(self, value):
        setattr(self, '_border_top_left_radius', value)

    @borderTopLeftRadius.deleter
    def borderTopLeftRadius(self):
        delattr(self, '_border_top_left_radius')

    @property
    def borderTopRightRadius(self):
        """
        border-top-right-radius

        Defines the radius of the border of the top-right corner

        object.style.borderTopRightRadius = "length|% [length|%]|initial|inherit"

        * `"length"`: Defines the shape of the top-right corner. Read about length units
        * `"%"`: Defines the shape of the top-right corner in %
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_top_right_radius', None)

    @borderTopRightRadius.setter
    def borderTopRightRadius(self, value):
        setattr(self, '_border_top_right_radius', value)

    @borderTopRightRadius.deleter
    def borderTopRightRadius(self):
        delattr(self, '_border_top_right_radius')

    @property
    def borderTopStyle(self):
        """
        border-top-style

        Sets the style of the top border

        object.style.borderTopStyle = "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|initial|inherit"

        * `"none"`: Specifies no border. This is default
        * `"hidden"`: The same as &quot;none&quot;, except in border conflict resolution for table elements
        * `"dotted"`: Specifies a dotted border
        * `"dashed"`: Specifies a dashed border
        * `"solid"`: Specifies a solid border
        * `"double"`: Specifies a double border
        * `"groove"`: Specifies a 3D grooved border. The effect depends on the border-color value
        * `"ridge"`: Specifies a 3D ridged border. The effect depends on the border-color value
        * `"inset"`: Specifies a 3D inset border. The effect depends on the border-color value
        * `"outset"`: Specifies a 3D outset border. The effect depends on the border-color value
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_top_style', None)

    @borderTopStyle.setter
    def borderTopStyle(self, value):
        setattr(self, '_border_top_style', value)

    @borderTopStyle.deleter
    def borderTopStyle(self):
        delattr(self, '_border_top_style')

    @property
    def borderTopWidth(self):
        """
        border-top-width

        Sets the width of the top border

        object.style.borderTopWidth = "medium|thin|thick|length|initial|inherit"

        * `"medium"`: Specifies a medium top border. This is default
        * `"thin"`: Specifies a thin top border
        * `"thick"`: Specifies a thick top border
        * `"length"`: Allows you to define the thickness of the top border. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_top_width', None)

    @borderTopWidth.setter
    def borderTopWidth(self, value):
        setattr(self, '_border_top_width', value)

    @borderTopWidth.deleter
    def borderTopWidth(self):
        delattr(self, '_border_top_width')

    @property
    def borderWidth(self):
        """
        border-width

        Sets the width of the four borders

        object.style.borderWidth = "medium|thin|thick|length|initial|inherit"

        * `"medium"`: Specifies a medium border. This is default
        * `"thin"`: Specifies a thin border
        * `"thick"`: Specifies a thick border
        * `"length"`: Allows you to define the thickness of the border. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_border_width', None)

    @borderWidth.setter
    def borderWidth(self, value):
        setattr(self, '_border_width', value)

    @borderWidth.deleter
    def borderWidth(self):
        delattr(self, '_border_width')

    @property
    def bottom(self):
        """
        bottom

        Sets the elements position, from the bottom of its parent element

        object.style.bottom = "auto|length|initial|inherit"

        * `"auto"`: Lets the browser calculate the bottom edge position. This is default
        * `"length"`: Sets the bottom edge position in px, cm, etc. Negative values are allowed. Read about length units
        * `"%"`: Sets the bottom edge position in % of containing element. Negative values are allowed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_bottom', None)

    @bottom.setter
    def bottom(self, value):
        setattr(self, '_bottom', value)

    @bottom.deleter
    def bottom(self):
        delattr(self, '_bottom')

    @property
    def boxDecorationBreak(self):
        """
        box-decoration-break

        Sets the behavior of the background and border of an element at page-break, or, for  in-line elements, at line-break.

        object.style.boxDecorationBreak = "slice|clone|initial|inherit|unset"

        * `"slice"`: Default. Box decorations are applied to the element as a whole and break at the edges of the element fragments
        * `"clone"`: Box decorations apply to each fragment of the element as if the fragments were individual elements. Borders wrap the four edges of each fragment of the element, and backgrounds are redrawn in full for each fragment
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_box_decoration_break', None)

    @boxDecorationBreak.setter
    def boxDecorationBreak(self, value):
        setattr(self, '_box_decoration_break', value)

    @boxDecorationBreak.deleter
    def boxDecorationBreak(self):
        delattr(self, '_box_decoration_break')

    @property
    def boxShadow(self):
        """
        box-shadow

        Attaches one or more shadows to an element

        object.style.boxShadow = "none|h-offset v-offset blur spread color |inset|initial|inherit"

        * `"none"`: Default value. No shadow is displayed
        * `"h-offset"`: Required. The horizontal offset of the shadow. A positive value puts the shadow on the right side of the box, a negative value puts the shadow on the left side of the box
        * `"v-offset"`: Required. The vertical offset of the shadow. A positive value puts the shadow below the box, a negative value puts the shadow above the box
        * `"blur"`: Optional. The blur radius. The higher the number, the more blurred the shadow will be
        * `"spread"`: Optional. The spread radius. A positive value increases the size of the shadow, a negative value decreases the size of the shadow
        * `"color"`: Optional. The color of the shadow. The default value is the text color. Look at CSS Color Values for a complete list of possible color values.Note: In Safari (on PC) the color parameter is required. If you do not specify the color, the shadow is not displayed at all.
        * `"inset"`: Optional. Changes the shadow from an outer shadow (outset) to an inner shadow
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_box_shadow', None)

    @boxShadow.setter
    def boxShadow(self, value):
        setattr(self, '_box_shadow', value)

    @boxShadow.deleter
    def boxShadow(self):
        delattr(self, '_box_shadow')

    @property
    def boxSizing(self):
        """
        box-sizing

        Defines how the width and height of an element are calculated: should
    they include padding and borders, or not

        object.style.boxSizing = "content-box|border-box|initial|inherit"

        * `"content-box"`: Default. The width and height properties (and min/max properties) includes only the content. Border and padding are not included
        * `"border-box"`: The width and height properties (and min/max properties) includes content, padding and border
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_box_sizing', None)

    @boxSizing.setter
    def boxSizing(self, value):
        setattr(self, '_box_sizing', value)

    @boxSizing.deleter
    def boxSizing(self):
        delattr(self, '_box_sizing')

    @property
    def breakAfter(self):
        """
        break-after

        Specifies the page-, column-, or region-break behavior after the generated box
        """
        return getattr(self, '_break_after', None)

    @breakAfter.setter
    def breakAfter(self, value):
        setattr(self, '_break_after', value)

    @breakAfter.deleter
    def breakAfter(self):
        delattr(self, '_break_after')

    @property
    def breakBefore(self):
        """
        break-before

        Specifies the page-, column-, or region-break behavior before the generated box
        """
        return getattr(self, '_break_before', None)

    @breakBefore.setter
    def breakBefore(self, value):
        setattr(self, '_break_before', value)

    @breakBefore.deleter
    def breakBefore(self):
        delattr(self, '_break_before')

    @property
    def breakInside(self):
        """
        break-inside

        Specifies the page-, column-, or region-break behavior inside the generated box
        """
        return getattr(self, '_break_inside', None)

    @breakInside.setter
    def breakInside(self, value):
        setattr(self, '_break_inside', value)

    @breakInside.deleter
    def breakInside(self):
        delattr(self, '_break_inside')

    @property
    def captionSide(self):
        """
        caption-side

        Specifies the placement of a table caption

        object.style.captionSide = "top|bottom|initial|inherit"

        * `"top"`: Puts the caption above the table. This is default
        * `"bottom"`: Puts the caption below the table
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_caption_side', None)

    @captionSide.setter
    def captionSide(self, value):
        setattr(self, '_caption_side', value)

    @captionSide.deleter
    def captionSide(self):
        delattr(self, '_caption_side')

    @property
    def caretColor(self):
        """
        caret-color

        Specifies the color of the cursor (caret) in inputs, textareas, or any
    element that is editable

        object.style.caretColor = "auto|color"

        * `"auto"`: Default. Browsers uses the currentColor for the caret
        * `"color"`: Specifies a color to use for the caret. All legal color values can be used (rgb, hex, named-color, etc). For more information on legal values, read our CSS Colors Tutorial
        """
        return getattr(self, '_caret_color', None)

    @caretColor.setter
    def caretColor(self, value):
        setattr(self, '_caret_color', value)

    @caretColor.deleter
    def caretColor(self):
        delattr(self, '_caret_color')

    @property
    def charset(self):
        """
        @charset

        Specifies the character encoding used in the style sheet

        object.style.charset = "&quot;charset&quot"

        * `"charset"`: Specifies the character encoding to use
        """
        return getattr(self, '_charset', None)

    @charset.setter
    def charset(self, value):
        setattr(self, '_charset', value)

    @charset.deleter
    def charset(self):
        delattr(self, '_charset')

    @property
    def clear(self):
        """
        clear

        Specifies on which sides of an element floating elements are not allowed to float

        object.style.clear = "none|left|right|both|initial|inherit"

        * `"none"`: Default. Allows floating elements on both sides
        * `"left"`: No floating elements allowed on the left side
        * `"right"`: No floating elements allowed on the right side
        * `"both"`: No floating elements allowed on either the left or the right side
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_clear', None)

    @clear.setter
    def clear(self, value):
        setattr(self, '_clear', value)

    @clear.deleter
    def clear(self):
        delattr(self, '_clear')

    @property
    def clip(self):
        """
        clip

        Clips an absolutely positioned element

        object.style.clip = "auto|shape|initial|inherit"

        * `"auto"`: No clipping will be applied. This is default
        * `"shape"`: Clips an element. The only valid value is: rect (top, right, bottom, left)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_clip', None)

    @clip.setter
    def clip(self, value):
        setattr(self, '_clip', value)

    @clip.deleter
    def clip(self):
        delattr(self, '_clip')

    @property
    def color(self):
        """
        color

        Sets the color of text

        object.style.color = "color|initial|inherit"

        * `"color"`: Specifies the text color. Look at CSS Color Values for a complete list of possible color values.
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_color', None)

    @color.setter
    def color(self, value):
        setattr(self, '_color', value)

    @color.deleter
    def color(self):
        delattr(self, '_color')

    @property
    def columnCount(self):
        """
        column-count

        Specifies the number of columns an element should be divided into

        object.style.columnCount = "number|auto|initial|inherit"

        * `"number"`: The optimal number of columns into which the content of the element will be flowed
        * `"auto"`: Default value. The number of columns will be determined by other properties, like e.g. &quot;column-width&quot;
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_count', None)

    @columnCount.setter
    def columnCount(self, value):
        setattr(self, '_column_count', value)

    @columnCount.deleter
    def columnCount(self):
        delattr(self, '_column_count')

    @property
    def columnFill(self):
        """
        column-fill

        Specifies how to fill columns, balanced or not

        object.style.columnFill = "balance|auto|initial|inherit"

        * `"balance"`: Default value. Fills each column with about the same amount of content, but will not allow the columns to be taller than the height (so, columns might be shorter than the height as the browser distributes the content evenly horizontally)
        * `"auto"`: Fills each column until it reaches the height, and do this until it runs out of content (so, this value will not necessarily fill all the columns nor fill them evenly)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_fill', None)

    @columnFill.setter
    def columnFill(self, value):
        setattr(self, '_column_fill', value)

    @columnFill.deleter
    def columnFill(self):
        delattr(self, '_column_fill')

    @property
    def columnGap(self):
        """
        column-gap

        Specifies the gap between the columns

        object.style.columnGap = "length|normal|initial|inherit"

        * `"length"`: A specified length that will set the gap between the columns
        * `"normal"`: Default value. Specifies a normal gap between the columns. W3C suggests a value of 1em
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_gap', None)

    @columnGap.setter
    def columnGap(self, value):
        setattr(self, '_column_gap', value)

    @columnGap.deleter
    def columnGap(self):
        delattr(self, '_column_gap')

    @property
    def columnRule(self):
        """
        column-rule

        A shorthand property for all the column-rule-* properties

        object.style.columnRule = "column-rule-width column-rule-style column-rule-color|initial|inherit"

        * `"column-rule-width"`: Sets the width of the rule between columns. Default value is medium
        * `"column-rule-style"`: Sets the style of the rule between columns. Default value is none
        * `"column-rule-color"`: Sets the color of the rule between columns. Default value is the color of the element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_rule', None)

    @columnRule.setter
    def columnRule(self, value):
        setattr(self, '_column_rule', value)

    @columnRule.deleter
    def columnRule(self):
        delattr(self, '_column_rule')

    @property
    def columnRuleColor(self):
        """
        column-rule-color

        Specifies the color of the rule between columns

        object.style.columnRuleColor = "color|initial|inherit"

        * `"color"`: Specifies the color of the rule. Look at CSS Color Values for a complete list of possible color values
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_rule_color', None)

    @columnRuleColor.setter
    def columnRuleColor(self, value):
        setattr(self, '_column_rule_color', value)

    @columnRuleColor.deleter
    def columnRuleColor(self):
        delattr(self, '_column_rule_color')

    @property
    def columnRuleStyle(self):
        """
        column-rule-style

        Specifies the style of the rule between columns

        object.style.columnRuleStyle = "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|initial|inherit"

        * `"none"`: Default value. Defines no rule
        * `"hidden"`: Defines a hidden rule
        * `"dotted"`: Defines a dotted rule
        * `"dashed"`: Defines a dashed rule
        * `"solid"`: Defines a solid rule
        * `"double"`: Defines a double rule
        * `"groove"`: Specifies a 3D grooved rule. The effect depends on the width and color values
        * `"ridge"`: Specifies a 3D ridged rule. The effect depends on the width and color values
        * `"inset"`: Specifies a 3D inset rule. The effect depends on the width and color values
        * `"outset"`: Specifies a 3D outset rule. The effect depends on the width and color values
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_rule_style', None)

    @columnRuleStyle.setter
    def columnRuleStyle(self, value):
        setattr(self, '_column_rule_style', value)

    @columnRuleStyle.deleter
    def columnRuleStyle(self):
        delattr(self, '_column_rule_style')

    @property
    def columnRuleWidth(self):
        """
        column-rule-width

        Specifies the width of the rule between columns

        object.style.columnRuleWidth = "medium|thin|thick|length|initial|inherit"

        * `"medium"`: Default value. Defines a medium rule
        * `"thin"`: Defines a thin rule
        * `"thick"`: Defines a thick rule
        * `"length"`: Specifies the width of the rule
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_rule_width', None)

    @columnRuleWidth.setter
    def columnRuleWidth(self, value):
        setattr(self, '_column_rule_width', value)

    @columnRuleWidth.deleter
    def columnRuleWidth(self):
        delattr(self, '_column_rule_width')

    @property
    def columnSpan(self):
        """
        column-span

        Specifies how many columns an element should span across

        object.style.columnSpan = "none|all|initial|inherit"

        * `"none"`: Default value. The element should span across one column
        * `"all"`: The element should span across all columns
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_span', None)

    @columnSpan.setter
    def columnSpan(self, value):
        setattr(self, '_column_span', value)

    @columnSpan.deleter
    def columnSpan(self):
        delattr(self, '_column_span')

    @property
    def columnWidth(self):
        """
        column-width

        Specifies the column width

        object.style.columnWidth = "auto|length|initial|inherit"

        * `"auto"`: Default value. The column width will be determined by the browser
        * `"length"`: A length that specifies the width of the columns. The number of columns will be the minimum number of columns needed to show all the content across the element. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_column_width', None)

    @columnWidth.setter
    def columnWidth(self, value):
        setattr(self, '_column_width', value)

    @columnWidth.deleter
    def columnWidth(self):
        delattr(self, '_column_width')

    @property
    def columns(self):
        """
        columns

        A shorthand property for column-width and column-count

        object.style.columns = "auto|column-width column-count|initial|inherit"

        * `"auto"`: Default value. Sets both the column-width and column-count to "auto"
        * `"column-width"`: Defines the minimum width for each column
        * `"column-count"`: Defines the maximum number of columns
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_columns', None)

    @columns.setter
    def columns(self, value):
        setattr(self, '_columns', value)

    @columns.deleter
    def columns(self):
        delattr(self, '_columns')

    @property
    def content(self):
        """
        content

        Used with the :before and :after pseudo-elements, to insert generated content

        object.style.content = "normal|none|counter|attr|string|open-quote|close-quote|no-open-quote|no-close-quote|url|initial|inherit"

        * `"normal"`: Default value. Sets the content, if specified, to normal, which default is &quot;none&quot; (which is nothing)
        * `"none"`: Sets the content, if specified, to nothing
        * `"counter"`: Sets the content as a counter
        * `"attr(attribute)"`: Sets the content as one of the selector's attribute
        * `"string"`: Sets the content to the text you specify
        * `"open-quote"`: Sets the content to be an opening quote
        * `"close-quote"`: Sets the content to be a closing quote
        * `"no-open-quote"`: Removes the opening quote from the content, if specified
        * `"no-close-quote"`: Removes the closing quote from the content, if specified
        * `"url(url)"`: Sets the content to be some kind of media (an image, a sound, a video, etc.)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_content', None)

    @content.setter
    def content(self, value):
        setattr(self, '_content', value)

    @content.deleter
    def content(self):
        delattr(self, '_content')

    @property
    def counterIncrement(self):
        """
        counter-increment

        Increases or decreases the value of one or more CSS counters

        object.style.counterIncrement = "none|id|initial|inherit"

        * `"none"`: Default value. No counters will be incremented
        * `"id number"`: The id defines which counter to increment. The number sets how much the counter will increment on each occurrence of the selector. The default increment is 1. Negative values are allowed. If id refers to a counter that has not been initialized by counter-reset, the default initial value is 0
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_counter_increment', None)

    @counterIncrement.setter
    def counterIncrement(self, value):
        setattr(self, '_counter_increment', value)

    @counterIncrement.deleter
    def counterIncrement(self):
        delattr(self, '_counter_increment')

    @property
    def counterReset(self):
        """
        counter-reset

        Creates or resets one or more CSS counters

        object.style.counterReset = "none|name number|initial|inherit"

        * `"none"`: Default value. No counters will be reset
        * `"id number"`: The id defines which counter to reset. The number sets the value the counter is reset to on each occurrence of the selector. The default number value is 0
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_counter_reset', None)

    @counterReset.setter
    def counterReset(self, value):
        setattr(self, '_counter_reset', value)

    @counterReset.deleter
    def counterReset(self):
        delattr(self, '_counter_reset')

    @property
    def cursor(self):
        """
        cursor

        Specifies the mouse cursor to be displayed when pointing over an element

        object.style.cursor = "value"

        * `"alias"`: The cursor indicates an alias of something is to be created
        * `"all-scroll"`: The cursor indicates that something can be scrolled in any direction
        * `"auto"`: Default. The browser sets a cursor
        * `"cell"`: The cursor indicates that a cell (or set of cells) may be selected
        * `"context-menu"`: The cursor indicates that a context-menu is available
        * `"col-resize"`: The cursor indicates that the column can be resized horizontally
        * `"copy"`: The cursor indicates something is to be copied
        * `"crosshair"`: The cursor render as a crosshair
        * `"default"`: The default cursor
        * `"e-resize"`: The cursor indicates that an edge of a box is to be moved right (east)
        * `"ew-resize"`: Indicates a bidirectional resize cursor
        * `"grab"`: The cursor indicates that something can be grabbed
        * `"grabbing"`: The cursor indicates that something can be grabbed
        * `"help"`: The cursor indicates that help is available
        * `"move"`: The cursor indicates something is to be moved
        * `"n-resize"`: The cursor indicates that an edge of a box is to be moved up (north)
        * `"ne-resize"`: The cursor indicates that an edge of a box is to be moved up and right (north/east)
        * `"nesw-resize"`: Indicates a bidirectional resize cursor
        * `"ns-resize"`: Indicates a bidirectional resize cursor
        * `"nw-resize"`: The cursor indicates that an edge of a box is to be moved up and left (north/west)
        * `"nwse-resize"`: Indicates a bidirectional resize cursor
        * `"no-drop"`: The cursor indicates that the dragged item cannot be dropped here
        * `"none"`: No cursor is rendered for the element
        * `"not-allowed"`: The cursor indicates that the requested action will not be executed
        * `"pointer"`: The cursor is a pointer and indicates a link
        * `"progress"`: The cursor indicates that the program is busy (in progress)
        * `"row-resize"`: The cursor indicates that the row can be resized vertically
        * `"s-resize"`: The cursor indicates that an edge of a box is to be moved down (south)
        * `"se-resize"`: The cursor indicates that an edge of a box is to be moved down and right (south/east)
        * `"sw-resize"`: The cursor indicates that an edge of a box is to be moved down and left (south/west)
        * `"text"`: The cursor indicates text that may be selected
        * `"URL"`: A comma separated list of URLs to custom cursors. Note: Always specify a generic cursor at the end of the list, in case none of the URL-defined cursors can be used
        * `"vertical-text"`: The cursor indicates vertical-text that may be selected
        * `"w-resize"`: The cursor indicates that an edge of a box is to be moved left (west)
        * `"wait"`: The cursor indicates that the program is busy
        * `"zoom-in"`: The cursor indicates that something can be zoomed in
        * `"zoom-out"`: The cursor indicates that something can be zoomed out
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_cursor', None)

    @cursor.setter
    def cursor(self, value):
        setattr(self, '_cursor', value)

    @cursor.deleter
    def cursor(self):
        delattr(self, '_cursor')

    @property
    def direction(self):
        """
        direction

        Specifies the text direction/writing direction

        object.style.direction = "ltr|rtl|initial|inherit"

        * `"ltr"`: Text direction goes from left-to-right. This is default
        * `"rtl"`: Text direction goes from right-to-left
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_direction', None)

    @direction.setter
    def direction(self, value):
        setattr(self, '_direction', value)

    @direction.deleter
    def direction(self):
        delattr(self, '_direction')

    @property
    def display(self):
        """
        display

        Specifies how a certain HTML element should be displayed

        object.style.display = "value"

        * `"inline"`: Displays an element as an inline element (like &lt;span&gt;). Any height and width properties will have no effect
        * `"block"`: Displays an element as a block element (like &lt;p&gt;). It starts on a new line, and takes up the whole width
        * `"contents"`: Makes the container disappear, making the child elements children of the element the next level up in the DOM
        * `"flex"`: Displays an element as a block-level flex container
        * `"grid"`: Displays an element as a block-level grid container
        * `"inline-block"`: Displays an element as an inline-level block container. The element itself is formatted as an inline element, but you can apply height and width values
        * `"inline-flex"`: Displays an element as an inline-level flex container
        * `"inline-grid"`: Displays an element as an inline-level grid container
        * `"inline-table"`: The element is displayed as an inline-level table
        * `"list-item"`: Let the element behave like a &lt;li&gt; element
        * `"run-in"`: Displays an element as either block or inline, depending on context
        * `"table"`: Let the element behave like a &lt;table&gt; element
        * `"table-caption"`: Let the element behave like a &lt;caption&gt; element
        * `"table-column-group"`: Let the element behave like a &lt;colgroup&gt; element
        * `"table-header-group"`: Let the element behave like a &lt;thead&gt; element
        * `"table-footer-group"`: Let the element behave like a &lt;tfoot&gt; element
        * `"table-row-group"`: Let the element behave like a &lt;tbody&gt; element
        * `"table-cell"`: Let the element behave like a &lt;td&gt; element
        * `"table-column"`: Let the element behave like a &lt;col&gt; element
        * `"table-row"`: Let the element behave like a &lt;tr&gt; element
        * `"none"`: The element is completely removed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_display', None)

    @display.setter
    def display(self, value):
        setattr(self, '_display', value)

    @display.deleter
    def display(self):
        delattr(self, '_display')

    @property
    def emptyCells(self):
        """
        empty-cells

        Specifies whether or not to display borders and background on empty cells in a table

        object.style.emptyCells = "show|hide|initial|inherit"

        * `"show"`: Display borders on empty cells. This  is default
        * `"hide"`: Hide borders on empty cells
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_empty_cells', None)

    @emptyCells.setter
    def emptyCells(self, value):
        setattr(self, '_empty_cells', value)

    @emptyCells.deleter
    def emptyCells(self):
        delattr(self, '_empty_cells')

    @property
    def filter(self):
        """
        filter

        Defines effects (e.g. blurring or color shifting) on an element before the element is displayed

        object.style.filter = "none | blur() | brightness() | contrast() | drop-shadow() | grayscale() | hue-rotate() | invert() | opacity() | saturate() | sepia() | url()"
        """
        return getattr(self, '_filter', None)

    @filter.setter
    def filter(self, value):
        setattr(self, '_filter', value)

    @filter.deleter
    def filter(self):
        delattr(self, '_filter')

    @property
    def flex(self):
        """
        flex

        A shorthand property for the flex-grow, flex-shrink, and the
    flex-basis
    properties

        object.style.flex = "flex-grow flex-shrink flex-basis|auto|initial|inherit"

        * `""`: A number specifying how much the item will grow relative to the rest of the flexible items
        * `""`: A number specifying how much the item will shrink relative to the rest of the flexible items
        * `""`: The length of the item. Legal values: "auto", "inherit", or a number followed by "%", "px", "em" or any other length unit
        * `"auto"`: Same as 1 1 auto.
        * `"initial"`: Same as 0 1 auto. Read about initial
        * `"none"`: Same as 0 0 auto.
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_flex', None)

    @flex.setter
    def flex(self, value):
        setattr(self, '_flex', value)

    @flex.deleter
    def flex(self):
        delattr(self, '_flex')

    @property
    def flexBasis(self):
        """
        flex-basis

        Specifies the initial length of a flexible item

        object.style.flexBasis = "number|auto|initial|inherit"

        * `"number"`: A length unit, or percentage, specifying the initial length of the flexible item(s)
        * `"auto"`: Default value. The length is equal to the length of the flexible item. If the item has no length specified, the length will be according to its content
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_flex_basis', None)

    @flexBasis.setter
    def flexBasis(self, value):
        setattr(self, '_flex_basis', value)

    @flexBasis.deleter
    def flexBasis(self):
        delattr(self, '_flex_basis')

    @property
    def flexDirection(self):
        """
        flex-direction

        Specifies the direction of the flexible items

        object.style.flexDirection = "row|row-reverse|column|column-reverse|initial|inherit"

        * `"row"`: Default value. The flexible items are displayed horizontally, as a row
        * `"row-reverse"`: Same as row, but in reverse order
        * `"column"`: The flexible items are displayed vertically, as a column
        * `"column-reverse"`: Same as column, but in reverse order
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_flex_direction', None)

    @flexDirection.setter
    def flexDirection(self, value):
        setattr(self, '_flex_direction', value)

    @flexDirection.deleter
    def flexDirection(self):
        delattr(self, '_flex_direction')

    @property
    def flexFlow(self):
        """
        flex-flow

        A shorthand property for the flex-direction and the flex-wrap properties

        object.style.flexFlow = "flex-direction flex-wrap|initial|inherit"

        * `"flex-direction"`: Possible values:rowrow-reversecolumncolumn-reverseinitialinherit Default value is "row". Specifying the direction of the flexible items
        * `"flex-wrap"`: Possible values:nowrapwrapwrap-reverseinitialinherit Default value is "nowrap".  Specifying whether the flexible items should wrap or not
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_flex_flow', None)

    @flexFlow.setter
    def flexFlow(self, value):
        setattr(self, '_flex_flow', value)

    @flexFlow.deleter
    def flexFlow(self):
        delattr(self, '_flex_flow')

    @property
    def flexGrow(self):
        """
        flex-grow

        Specifies how much the item will grow relative to the rest

        object.style.flexGrow = "number|initial|inherit"

        * `"number"`: A number specifying how much the item will grow relative to the rest of the flexible items. Default value is 0
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_flex_grow', None)

    @flexGrow.setter
    def flexGrow(self, value):
        setattr(self, '_flex_grow', value)

    @flexGrow.deleter
    def flexGrow(self):
        delattr(self, '_flex_grow')

    @property
    def flexShrink(self):
        """
        flex-shrink

        Specifies how the item will shrink relative to the rest

        object.style.flexShrink = "number|initial|inherit"

        * `"number"`: A number specifying how much the item will shrink relative to the rest of the flexible items. Default value is 1
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_flex_shrink', None)

    @flexShrink.setter
    def flexShrink(self, value):
        setattr(self, '_flex_shrink', value)

    @flexShrink.deleter
    def flexShrink(self):
        delattr(self, '_flex_shrink')

    @property
    def flexWrap(self):
        """
        flex-wrap

        Specifies whether the flexible items should wrap or not

        object.style.flexWrap = "nowrap|wrap|wrap-reverse|initial|inherit"

        * `"nowrap"`: Default value. Specifies that the flexible items will not wrap
        * `"wrap"`: Specifies that the flexible items will wrap if necessary
        * `"wrap-reverse"`: Specifies that the flexible items will wrap, if necessary, in reverse order
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_flex_wrap', None)

    @flexWrap.setter
    def flexWrap(self, value):
        setattr(self, '_flex_wrap', value)

    @flexWrap.deleter
    def flexWrap(self):
        delattr(self, '_flex_wrap')

    @property
    def float(self):
        """
        float

        Specifies whether or not a box should float

        object.style.float = "none|left|right|initial|inherit"

        * `"none"`: The element does not float, (will be displayed just where it occurs in the text). This is default
        * `"left"`: The element floats to the left of its container
        * `"right"`: The element floats the right of its container
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_float', None)

    @float.setter
    def float(self, value):
        setattr(self, '_float', value)

    @float.deleter
    def float(self):
        delattr(self, '_float')

    @property
    def font(self):
        """
        font

        A shorthand property for the font-style, font-variant, font-weight, font-size/line-height, and the font-family properties

        object.style.font = "font-style font-variant font-weight font-size/line-height font-family|caption|icon|menu|message-box|small-caption|status-bar|initial|inherit"

        * `"font-style"`: Specifies the font style. Default value is &quot;normal&quot;
        * `"font-variant"`: Specifies the font variant. Default value is &quot;normal&quot;
        * `"font-weight"`: Specifies the font weight. Default value is &quot;normal&quot;
        * `"font-size/"`: Specifies the font size and the line-height. Default value is &quot;normal&quot;
        * `"font-family"`: Specifies the font family. Default value depends on the browser
        * `"caption"`: Uses the font that are used by captioned controls (like buttons, drop-downs, etc.)
        * `"icon"`: Uses the font that are used by icon labels
        * `"menu"`: Uses the fonts that are used by dropdown menus
        * `"message-box"`: Uses the fonts that are used by dialog boxes
        * `"small-caption"`: A smaller version of the caption font
        * `"status-bar"`: Uses the fonts that are used by the status bar
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font', None)

    @font.setter
    def font(self, value):
        setattr(self, '_font', value)

    @font.deleter
    def font(self):
        delattr(self, '_font')

    @property
    def fontFace(self):
        """
        @font-face

        A rule that allows websites to download and use fonts other than the &quot;web-safe&quot; fonts

        * `"TTF/OTF"`: 4.0
        * `"WOFF"`: 5.0
        * `"WOFF2"`: 36.0
        * `"SVG"`: 4.0
        * `"EOT"`: Not supported
        """
        return getattr(self, '_font_face', None)

    @fontFace.setter
    def fontFace(self, value):
        setattr(self, '_font_face', value)

    @fontFace.deleter
    def fontFace(self):
        delattr(self, '_font_face')

    @property
    def fontFamily(self):
        """
        font-family

        Specifies the font family for text

        object.style.fontFamily = "family-name|generic-family|initial|inherit"

        * `"generic-family"`: A prioritized list of font family names and/or generic family names
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font_family', None)

    @fontFamily.setter
    def fontFamily(self, value):
        setattr(self, '_font_family', value)

    @fontFamily.deleter
    def fontFamily(self):
        delattr(self, '_font_family')

    @property
    def fontFeatureSettings(self):
        """
        font-feature-settings

        Allows control over advanced typographic features in OpenType fonts
        """
        return getattr(self, '_font_feature_settings', None)

    @fontFeatureSettings.setter
    def fontFeatureSettings(self, value):
        setattr(self, '_font_feature_settings', value)

    @fontFeatureSettings.deleter
    def fontFeatureSettings(self):
        delattr(self, '_font_feature_settings')

    @property
    def fontFeatureValues(self):
        """
        @font-feature-values

        Allows authors to use a common name in font-variant-alternate for feature activated differently in OpenType
        """
        return getattr(self, '_font_feature_values', None)

    @fontFeatureValues.setter
    def fontFeatureValues(self, value):
        setattr(self, '_font_feature_values', value)

    @fontFeatureValues.deleter
    def fontFeatureValues(self):
        delattr(self, '_font_feature_values')

    @property
    def fontKerning(self):
        """
        font-kerning

        Controls the usage of the kerning information (how letters are spaced)

        object.style.fontKerning = "auto|normal|none"

        * `"auto"`: Default. The browser determines whether font kerning should be applied or not
        * `"normal"`: Specifies that font kerning is applied
        * `"none"`: Specifies that font kerning is not applied
        """
        return getattr(self, '_font_kerning', None)

    @fontKerning.setter
    def fontKerning(self, value):
        setattr(self, '_font_kerning', value)

    @fontKerning.deleter
    def fontKerning(self):
        delattr(self, '_font_kerning')

    @property
    def fontLanguageOverride(self):
        """
        font-language-override

        Controls the usage of language-specific glyphs in a typeface
        """
        return getattr(self, '_font_language_override', None)

    @fontLanguageOverride.setter
    def fontLanguageOverride(self, value):
        setattr(self, '_font_language_override', value)

    @fontLanguageOverride.deleter
    def fontLanguageOverride(self):
        delattr(self, '_font_language_override')

    @property
    def fontSize(self):
        """
        font-size

        Specifies the font size of text

        object.style.fontSize = "medium|xx-small|x-small|small|large|x-large|xx-large|smaller|larger|length|initial|inherit"

        * `"medium"`: Sets the font-size to a medium size. This is default
        * `"xx-small"`: Sets the font-size to an xx-small size
        * `"x-small"`: Sets the font-size to an extra small size
        * `"small"`: Sets the font-size to a small size
        * `"large"`: Sets the font-size to a large size
        * `"x-large"`: Sets the font-size to an extra large size
        * `"xx-large"`: Sets the font-size to an xx-large size
        * `"smaller"`: Sets the font-size to a smaller size than the parent element
        * `"larger"`: Sets the font-size to a larger size than the parent element
        * `"length"`: Sets the font-size to a fixed size in px, cm, etc. Read about length units
        * `"%"`: Sets the font-size to a percent of the parent element's font size
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font_size', None)

    @fontSize.setter
    def fontSize(self, value):
        setattr(self, '_font_size', value)

    @fontSize.deleter
    def fontSize(self):
        delattr(self, '_font_size')

    @property
    def fontSizeAdjust(self):
        """
        font-size-adjust

        Preserves the readability of text when font fallback occurs

        * `"number"`: Defines the aspect value to use
        * `"none"`: Default value. No font size adjustment
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font_size_adjust', None)

    @fontSizeAdjust.setter
    def fontSizeAdjust(self, value):
        setattr(self, '_font_size_adjust', value)

    @fontSizeAdjust.deleter
    def fontSizeAdjust(self):
        delattr(self, '_font_size_adjust')

    @property
    def fontStretch(self):
        """
        font-stretch

        Selects a normal, condensed, or expanded face from a font family

        * `"ultra-condensed"`: Makes the text as narrow as it gets
        * `"extra-condensed"`: Makes the text narrower than condensed, but not as narrow as ultra-condensed
        * `"condensed"`: Makes the text narrower than semi-condensed, but not as narrow as extra-condensed
        * `"semi-condensed"`: Makes the text narrower than normal, but not as narrow as condensed
        * `"normal"`: Default value. No font stretching
        * `"semi-expanded"`: Makes the text wider than normal, but not as wide as expanded
        * `"expanded"`: Makes the text wider than semi-expanded, but not as wide as extra-expanded
        * `"extra-expanded"`: Makes the text wider than expanded, but not as wide as ultra-expanded
        * `"ultra-expanded"`: Makes the text as wide as it gets
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font_stretch', None)

    @fontStretch.setter
    def fontStretch(self, value):
        setattr(self, '_font_stretch', value)

    @fontStretch.deleter
    def fontStretch(self):
        delattr(self, '_font_stretch')

    @property
    def fontStyle(self):
        """
        font-style

        Specifies the font style for text

        object.style.fontStyle = "normal|italic|oblique|initial|inherit"

        * `"normal"`: The browser displays a normal font style. This is default
        * `"italic"`: The browser displays an italic font style
        * `"oblique"`: The browser displays an oblique font style
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font_style', None)

    @fontStyle.setter
    def fontStyle(self, value):
        setattr(self, '_font_style', value)

    @fontStyle.deleter
    def fontStyle(self):
        delattr(self, '_font_style')

    @property
    def fontSynthesis(self):
        """
        font-synthesis

        Controls which missing typefaces (bold or italic) may be synthesized by the browser
        """
        return getattr(self, '_font_synthesis', None)

    @fontSynthesis.setter
    def fontSynthesis(self, value):
        setattr(self, '_font_synthesis', value)

    @fontSynthesis.deleter
    def fontSynthesis(self):
        delattr(self, '_font_synthesis')

    @property
    def fontVariant(self):
        """
        font-variant

        Specifies whether or not a text should be displayed in a small-caps font

        object.style.fontVariant = "normal|small-caps|initial|inherit"

        * `"normal"`: The browser displays a normal font. This is default
        * `"small-caps"`: The browser displays a small-caps font
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font_variant', None)

    @fontVariant.setter
    def fontVariant(self, value):
        setattr(self, '_font_variant', value)

    @fontVariant.deleter
    def fontVariant(self):
        delattr(self, '_font_variant')

    @property
    def fontVariantAlternates(self):
        """
        font-variant-alternates

        Controls the usage of alternate glyphs associated to alternative names defined in @font-feature-values
        """
        return getattr(self, '_font_variant_alternates', None)

    @fontVariantAlternates.setter
    def fontVariantAlternates(self, value):
        setattr(self, '_font_variant_alternates', value)

    @fontVariantAlternates.deleter
    def fontVariantAlternates(self):
        delattr(self, '_font_variant_alternates')

    @property
    def fontVariantCaps(self):
        """
        font-variant-caps

        Controls the usage of alternate glyphs for capital letters
        """
        return getattr(self, '_font_variant_caps', None)

    @fontVariantCaps.setter
    def fontVariantCaps(self, value):
        setattr(self, '_font_variant_caps', value)

    @fontVariantCaps.deleter
    def fontVariantCaps(self):
        delattr(self, '_font_variant_caps')

    @property
    def fontVariantEastAsian(self):
        """
        font-variant-east-asian

        Controls the usage of alternate glyphs for East Asian scripts (e.g Japanese and Chinese)
        """
        return getattr(self, '_font_variant_east_asian', None)

    @fontVariantEastAsian.setter
    def fontVariantEastAsian(self, value):
        setattr(self, '_font_variant_east_asian', value)

    @fontVariantEastAsian.deleter
    def fontVariantEastAsian(self):
        delattr(self, '_font_variant_east_asian')

    @property
    def fontVariantLigatures(self):
        """
        font-variant-ligatures

        Controls which ligatures and contextual forms are used in textual content of the elements it applies to
        """
        return getattr(self, '_font_variant_ligatures', None)

    @fontVariantLigatures.setter
    def fontVariantLigatures(self, value):
        setattr(self, '_font_variant_ligatures', value)

    @fontVariantLigatures.deleter
    def fontVariantLigatures(self):
        delattr(self, '_font_variant_ligatures')

    @property
    def fontVariantNumeric(self):
        """
        font-variant-numeric

        Controls the usage of alternate glyphs for numbers, fractions, and ordinal markers
        """
        return getattr(self, '_font_variant_numeric', None)

    @fontVariantNumeric.setter
    def fontVariantNumeric(self, value):
        setattr(self, '_font_variant_numeric', value)

    @fontVariantNumeric.deleter
    def fontVariantNumeric(self):
        delattr(self, '_font_variant_numeric')

    @property
    def fontVariantPosition(self):
        """
        font-variant-position

        Controls the usage of alternate glyphs of smaller size positioned as superscript or subscript regarding the baseline of the font
        """
        return getattr(self, '_font_variant_position', None)

    @fontVariantPosition.setter
    def fontVariantPosition(self, value):
        setattr(self, '_font_variant_position', value)

    @fontVariantPosition.deleter
    def fontVariantPosition(self):
        delattr(self, '_font_variant_position')

    @property
    def fontWeight(self):
        """
        font-weight

        Specifies the weight of a font

        object.style.fontWeight = "normal|bold|bolder|lighter|number|initial|inherit"

        * `"normal"`: Defines normal characters. This is default
        * `"bold"`: Defines thick characters
        * `"bolder"`: Defines thicker characters
        * `"lighter"`: Defines lighter characters
        * `" 200"`: Defines from thin to thick characters. 400 is the same as normal, and 700 is the same as bold
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_font_weight', None)

    @fontWeight.setter
    def fontWeight(self, value):
        setattr(self, '_font_weight', value)

    @fontWeight.deleter
    def fontWeight(self):
        delattr(self, '_font_weight')

    @property
    def grid(self):
        """
        grid

        A shorthand property for the grid-template-rows,
    grid-template-columns, grid-template-areas, grid-auto-rows,
    grid-auto-columns, and the grid-auto-flow properties
        """
        return getattr(self, '_grid', None)

    @grid.setter
    def grid(self, value):
        setattr(self, '_grid', value)

    @grid.deleter
    def grid(self):
        delattr(self, '_grid')

    @property
    def gridArea(self):
        """
        grid-area

        Either specifies a name for the grid item, or this property is a shorthand property for the grid-row-start, grid-column-start, grid-row-end, and grid-column-end properties

        object.style.gridArea = "grid-row-start / grid-column-start / grid-row-end / grid-column-end | itemname"

        * `"grid-row-start"`: Specifies on which row to start displaying the item.
        * `"grid-column-start"`: Specifies on which column to start displaying the item.
        * `"grid-row-end"`: Specifies on which row-line to stop displaying the item, or how many rows to span.
        * `"grid-column-end"`: Specifies on which column-line to stop displaying the item, or how many columns to span.
        * `"itemname"`: Specifies a name for the grid item
        """
        return getattr(self, '_grid_area', None)

    @gridArea.setter
    def gridArea(self, value):
        setattr(self, '_grid_area', value)

    @gridArea.deleter
    def gridArea(self):
        delattr(self, '_grid_area')

    @property
    def gridAutoColumns(self):
        """
        grid-auto-columns

        Specifies a default column size

        object.style.gridAutoColumns = "auto|max-content|min-content|length"

        * `"auto"`: Default value. The size of the columns is determined by the size of the container
        * `"fit-content()"`:
        * `"max-content"`: Sets the size of each column depending on the largest item in the column
        * `"min-content"`: Sets the size of each column depending on the smallest item in the column
        * `"minmax(min.max)"`: Sets a size range greater than or equal to min and less than or equal to max
        * `"length"`: Sets the size of the columns, by using a legal length value. Read about length units
        * `"%"`: Sets the size of the columns, by using a percent value
        """
        return getattr(self, '_grid_auto_columns', None)

    @gridAutoColumns.setter
    def gridAutoColumns(self, value):
        setattr(self, '_grid_auto_columns', value)

    @gridAutoColumns.deleter
    def gridAutoColumns(self):
        delattr(self, '_grid_auto_columns')

    @property
    def gridAutoFlow(self):
        """
        grid-auto-flow

        Specifies how auto-placed items are inserted in the grid

        object.style.gridAutoFlow = "row|column|dense|row dense|column dense"

        * `"row"`: Default value. Places items by filling each row
        * `"column"`: Places items by filling each column
        * `"dense"`: Place items to fill any holes in the grid
        * `"row dense"`: Places items by filling each row, and fill any holes in the grid
        * `"column dense"`: Places items by filling each column, and fill any holes in the grid
        """
        return getattr(self, '_grid_auto_flow', None)

    @gridAutoFlow.setter
    def gridAutoFlow(self, value):
        setattr(self, '_grid_auto_flow', value)

    @gridAutoFlow.deleter
    def gridAutoFlow(self):
        delattr(self, '_grid_auto_flow')

    @property
    def gridAutoRows(self):
        """
        grid-auto-rows

        Specifies a default row size

        * `"auto"`: Default value. The size of the rows is determined by the size of the largest item in the row
        * `"max-content"`: Sets the size of each row to depend on the largest item in the row
        * `"min-content"`: Sets the size of each row to depend on the largest item in the row
        * `"length"`: Sets the size of the rows, by using a legal length value. Read about length units
        """
        return getattr(self, '_grid_auto_rows', None)

    @gridAutoRows.setter
    def gridAutoRows(self, value):
        setattr(self, '_grid_auto_rows', value)

    @gridAutoRows.deleter
    def gridAutoRows(self):
        delattr(self, '_grid_auto_rows')

    @property
    def gridColumn(self):
        """
        grid-column

        A shorthand property for the grid-column-start and the grid-column-end properties

        object.style.gridColumn = "grid-column-start / grid-column-end"

        * `"grid-column-start"`: Specifies on which column to start displaying the item.
        * `"grid-column-end"`: Specifies on which column-line to stop displaying the item, or how many columns to span.
        """
        return getattr(self, '_grid_column', None)

    @gridColumn.setter
    def gridColumn(self, value):
        setattr(self, '_grid_column', value)

    @gridColumn.deleter
    def gridColumn(self):
        delattr(self, '_grid_column')

    @property
    def gridColumnEnd(self):
        """
        grid-column-end

        Specifies where to end the grid item

        object.style.gridColumnEnd = "auto|span n|column-line"

        * `"auto"`: Default value. The item will span one column
        * `"n"`: Specifies the number of columns the item will span
        * `"column-line"`: Specifies on which column to end the display of the item
        """
        return getattr(self, '_grid_column_end', None)

    @gridColumnEnd.setter
    def gridColumnEnd(self, value):
        setattr(self, '_grid_column_end', value)

    @gridColumnEnd.deleter
    def gridColumnEnd(self):
        delattr(self, '_grid_column_end')

    @property
    def gridColumnGap(self):
        """
        grid-column-gap

        Specifies the size of the gap between columns

        object.style.gridColumnGap = "length"

        * `"length"`: Any legal length value, like px or %. 0 is the default value. Read about length units
        """
        return getattr(self, '_grid_column_gap', None)

    @gridColumnGap.setter
    def gridColumnGap(self, value):
        setattr(self, '_grid_column_gap', value)

    @gridColumnGap.deleter
    def gridColumnGap(self):
        delattr(self, '_grid_column_gap')

    @property
    def gridColumnStart(self):
        """
        grid-column-start

        Specifies where to start the grid item

        object.style.gridColumnStart = "auto|span n|column-line"

        * `"auto"`: Default value. The item will be placed following the flow
        * `"n"`: Specifies the number of columns the item will span
        * `"column-line"`: Specifies on which column to start the display of the item
        """
        return getattr(self, '_grid_column_start', None)

    @gridColumnStart.setter
    def gridColumnStart(self, value):
        setattr(self, '_grid_column_start', value)

    @gridColumnStart.deleter
    def gridColumnStart(self):
        delattr(self, '_grid_column_start')

    @property
    def gridGap(self):
        """
        grid-gap

        A shorthand property for the grid-row-gap and grid-column-gap properties

        object.style.gridGap = "grid-row-gap grid-column-gap"

        * `""`: Sets the size of the gap between the rows in a grid layout. 0 is the default value
        * `""`: Sets the size of the gap between the columns in a grid layout. 0 is the default value
        """
        return getattr(self, '_grid_gap', None)

    @gridGap.setter
    def gridGap(self, value):
        setattr(self, '_grid_gap', value)

    @gridGap.deleter
    def gridGap(self):
        delattr(self, '_grid_gap')

    @property
    def gridRow(self):
        """
        grid-row

        A shorthand property for the grid-row-start and the grid-row-end properties

        object.style.gridRow = "grid-row-start / grid-row-end"

        * `""`: Specifies on which row to start displaying the item.
        * `"grid-row-end"`: Specifies on which row-line to stop displaying the item, or how many rows to span.
        """
        return getattr(self, '_grid_row', None)

    @gridRow.setter
    def gridRow(self, value):
        setattr(self, '_grid_row', value)

    @gridRow.deleter
    def gridRow(self):
        delattr(self, '_grid_row')

    @property
    def gridRowEnd(self):
        """
        grid-row-end

        Specifies where to end the grid item

        object.style.gridRowEnd = "auto|row-line|span n"

        * `"auto"`: Default value. The item will span one row.
        * `"n"`: Specifies the number of rows the item will span.
        * `"column-line"`: Specifies on which row to end the display of the item.
        """
        return getattr(self, '_grid_row_end', None)

    @gridRowEnd.setter
    def gridRowEnd(self, value):
        setattr(self, '_grid_row_end', value)

    @gridRowEnd.deleter
    def gridRowEnd(self):
        delattr(self, '_grid_row_end')

    @property
    def gridRowGap(self):
        """
        grid-row-gap

        Specifies the size of the gap between rows

        object.style.gridRowGap = "length"

        * `"length"`: Any legal length value, like px or %. 0 is the default value
        """
        return getattr(self, '_grid_row_gap', None)

    @gridRowGap.setter
    def gridRowGap(self, value):
        setattr(self, '_grid_row_gap', value)

    @gridRowGap.deleter
    def gridRowGap(self):
        delattr(self, '_grid_row_gap')

    @property
    def gridRowStart(self):
        """
        grid-row-start

        Specifies where to start the grid item

        object.style.gridRowStart = "auto|row-line"

        * `"auto"`: Default value. The item will be placed by following the flow.
        * `"row-line"`: Specifies on which row to start the display of the item.
        """
        return getattr(self, '_grid_row_start', None)

    @gridRowStart.setter
    def gridRowStart(self, value):
        setattr(self, '_grid_row_start', value)

    @gridRowStart.deleter
    def gridRowStart(self):
        delattr(self, '_grid_row_start')

    @property
    def gridTemplate(self):
        """
        grid-template

        A shorthand property for the grid-template-rows, grid-template-columns
    and grid-areas properties

        object.style.gridTemplate = "none|grid-template-rows / grid-template-columns|grid-template-areas|initial|inherit"

        * `"none"`: Default value. No specific sizing of the columns or rows
        * `"grid-template rows / grid-template-columns"`: Specifies the size(s) of the columns and rows
        * `"grid-template-areas"`: Specifies the grid layout using named items
        * `"initial"`: Sets this property to its default value.  Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about  inherit
        """
        return getattr(self, '_grid_template', None)

    @gridTemplate.setter
    def gridTemplate(self, value):
        setattr(self, '_grid_template', value)

    @gridTemplate.deleter
    def gridTemplate(self):
        delattr(self, '_grid_template')

    @property
    def gridTemplateAreas(self):
        """
        grid-template-areas

        Specifies how to display columns and rows, using named grid items

        object.style.gridTemplateAreas = "none|itemnames"

        * `"none"`: Default value. No named grid areas
        * `"itemnames"`: A sequence that specifies how each columns and row should display
        """
        return getattr(self, '_grid_template_areas', None)

    @gridTemplateAreas.setter
    def gridTemplateAreas(self, value):
        setattr(self, '_grid_template_areas', value)

    @gridTemplateAreas.deleter
    def gridTemplateAreas(self):
        delattr(self, '_grid_template_areas')

    @property
    def gridTemplateColumns(self):
        """
        grid-template-columns

        Specifies the size of the columns, and how many columns in a grid layout

        object.style.gridTemplateColumns = "none|auto|max-content|min-content|length|initial|inherit"

        * `"none"`: Default value. Columns are created if needed
        * `"auto"`: The size of the columns is determined by the size of the container and on the size of the content of the items in the column
        * `"max-content"`: Sets the size of each column to depend on the largest item in the column
        * `"min-content"`: Sets the size of each column to depend on the largest item in the column
        * `"length"`: Sets the size of the columns, by using a legal length value. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_grid_template_columns', None)

    @gridTemplateColumns.setter
    def gridTemplateColumns(self, value):
        setattr(self, '_grid_template_columns', value)

    @gridTemplateColumns.deleter
    def gridTemplateColumns(self):
        delattr(self, '_grid_template_columns')

    @property
    def gridTemplateRows(self):
        """
        grid-template-rows

        Specifies the size of the rows in a grid layout

        object.style.gridTemplateRows = "none|auto|max-content|min-content|length|initial|inherit"

        * `"none"`: No size is set. Rows are created if needed
        * `"auto"`: The size of the rows is determined by the size of the container, and on the size of the content of the items in the row
        * `"max-content"`: Sets the size of each row to depend on the largest item in the row
        * `"min-content"`: Sets the size of each row to depend on the largest item in the row
        * `"length"`: Sets the size of the rows, by using a legal length value. Read about length units
        """
        return getattr(self, '_grid_template_rows', None)

    @gridTemplateRows.setter
    def gridTemplateRows(self, value):
        setattr(self, '_grid_template_rows', value)

    @gridTemplateRows.deleter
    def gridTemplateRows(self):
        delattr(self, '_grid_template_rows')

    @property
    def hangingPunctuation(self):
        """
        hanging-punctuation

        Specifies whether a punctuation character may be placed outside the line box

        object.style.hangingPunctuation = "none|first|last|allow-end|force-end|initial|inherit"

        * `"none"`: No punctuation mark may be placed outside the line box at the start or at the end of a full line of text
        * `"first"`: Punctuation may hang outside the start edge of the first line
        * `"last"`: Punctuation may hang outside the end edge of the last line
        * `"allow-end"`: Punctuation may hang outside the end edge of all lines if the punctuation does not otherwise fit prior to justification
        * `"force-end"`: Punctuation may hang outside the end edge of all lines. If justification is enabled on this line, then it will force the punctuation to hang
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_hanging_punctuation', None)

    @hangingPunctuation.setter
    def hangingPunctuation(self, value):
        setattr(self, '_hanging_punctuation', value)

    @hangingPunctuation.deleter
    def hangingPunctuation(self):
        delattr(self, '_hanging_punctuation')

    @property
    def height(self):
        """
        height

        Sets the height of an element

        object.style.height = "auto|length|initial|inherit"

        * `"auto"`: The browser calculates the height. This is default
        * `"length"`: Defines the height in px, cm, etc. Read about length units
        * `"%"`: Defines the height in percent of the containing block
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_height', None)

    @height.setter
    def height(self, value):
        setattr(self, '_height', value)

    @height.deleter
    def height(self):
        delattr(self, '_height')

    @property
    def hyphens(self):
        """
        hyphens

        Sets how to split words to improve the layout of paragraphs

        object.style.hyphens = "none|manual|auto|initial|inherit"

        * `"none"`: Words are not hyphenated
        * `"manual"`: Default. Words are only hyphenated at &amp;hyphen; or &amp;shy; (if needed)
        * `"auto"`: Words are hyphenated where the algorithm is deciding (if needed)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_hyphens', None)

    @hyphens.setter
    def hyphens(self, value):
        setattr(self, '_hyphens', value)

    @hyphens.deleter
    def hyphens(self):
        delattr(self, '_hyphens')

    @property
    def imageRendering(self):
        """
        image-rendering

        Gives a hint to the browser about what aspects of an image are most important to preserve when the image is scaled
        """
        return getattr(self, '_image_rendering', None)

    @imageRendering.setter
    def ImageRendering(self, value):
        setattr(self, '_image_rendering', value)

    @imageRendering.deleter
    def imageRendering(self):
        delattr(self, '_image_rendering')

    @property
    def import_(self):
        """
        @import

        Allows you to import a style sheet into another style sheet

        object.style.import = "url|string list-of-mediaqueries"

        * `"url"`: A url or a string representing the location of the resource to import. The url may be absolute or relative
        * `"list-of-mediaqueries"`: A comma-separated list of media queries conditioning the application of the CSS rules defined in the linked URL
        """
        return getattr(self, '_import', None)

    @import_.setter
    def import_(self, value):
        setattr(self, '_import', value)

    @import_.deleter
    def import_(self):
        delattr(self, '_import')

    @property
    def isolation(self):
        """
        isolation

        Defines whether an element must create a new stacking content

        object.style.isolation = "auto|isolate|initial|inherit"

        * `"auto"`: Default. A new stacking context is created only if one of the properties applied to the element requires it
        * `"isolate"`: A new stacking context must be created
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_isolation', None)

    @isolation.setter
    def isolation(self, value):
        setattr(self, '_isolation', value)

    @isolation.deleter
    def isolation(self):
        delattr(self, '_isolation')

    @property
    def justifyContent(self):
        """
        justify-content

        Specifies the alignment between the items inside a flexible container when the items do not use all available space

        object.style.justifyContent = "flex-start|flex-end|center|space-between|space-around|initial|inherit"

        * `"flex-start"`: Default value. Items are positioned at the beginning of the container
        * `"flex-end"`: Items are positioned at the end of the container
        * `"center"`: Items are positioned at the center of the container
        * `"space-between"`: Items are positioned with space between the lines
        * `"space-around"`: Items are positioned with space before, between, and after the lines
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_justify_content', None)

    @justifyContent.setter
    def justifyContent(self, value):
        setattr(self, '_justify_content', value)

    @justifyContent.deleter
    def justifyContent(self):
        delattr(self, '_justify_content')

    @property
    def keyframes(self):
        """
        @keyframes

        Specifies the animation code

        object.style.keyframes = "animationname {keyframes-selector {css-styles;}"

        * `"animationname"`: Required. Defines the name of the animation.
        * `"keyframes-selector"`: Required. Percentage of the animation duration.Legal values:0-100% from (same as 0%) to (same as 100%)Note: You can have many keyframes-selectors in one animation.
        * `"css-styles"`: Required. One or more legal CSS style properties
        """
        return getattr(self, '_keyframes', None)

    @keyframes.setter
    def keyframes(self, value):
        setattr(self, '_keyframes', value)

    @keyframes.deleter
    def keyframes(self):
        delattr(self, '_keyframes')

    @property
    def left(self):
        """
        left

        Specifies the left position of a positioned element

        object.style.left = "auto|length|initial|inherit"

        * `"auto"`: Lets the browser calculate the left edge position. This is default
        * `"length"`: Sets the left edge position in px, cm, etc. Negative values are allowed. Read about length units
        * `"%"`: Sets the left edge position in % of containing element. Negative values are allowed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_left', None)

    @left.setter
    def left(self, value):
        setattr(self, '_left', value)

    @left.deleter
    def left(self):
        delattr(self, '_left')

    @property
    def letterSpacing(self):
        """
        letter-spacing

        Increases or decreases the space between characters in a text

        object.style.letterSpacing = "normal|length|initial|inherit"

        * `"normal"`: No extra space between characters. This is default
        * `"length"`: Defines an extra space between characters (negative values are allowed). Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_letter_spacing', None)

    @letterSpacing.setter
    def letterSpacing(self, value):
        setattr(self, '_letter_spacing', value)

    @letterSpacing.deleter
    def letterSpacing(self):
        delattr(self, '_letter_spacing')

    @property
    def lineBreak(self):
        """
        line-break

        Specifies how/if to break lines
        """
        return getattr(self, '_line_break', None)

    @lineBreak.setter
    def lineBreak(self, value):
        setattr(self, '_line_break', value)

    @lineBreak.deleter
    def lineBreak(self):
        delattr(self, '_line_break')

    @property
    def lineHeight(self):
        """
        line-height

        Sets the line height

        object.style.lineHeight = "normal|number|length|initial|inherit"

        * `"normal"`: A normal line height. This is default
        * `"number"`: A number that will be multiplied with the current font-size to set the line height
        * `"length"`: A fixed line height in px, pt, cm, etc.
        * `"%"`: A line height in percent of the current font size
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_line_height', None)

    @lineHeight.setter
    def lineHeight(self, value):
        setattr(self, '_line_height', value)

    @lineHeight.deleter
    def lineHeight(self):
        delattr(self, '_line_height')

    @property
    def listStyle(self):
        """
        list-style

        Sets all the properties for a list in one declaration

        object.style.listStyle = "list-style-type list-style-position list-style-image|initial|inherit"

        * `"list-style-type"`: Specifies the type of list-item marker. Default value is &quot;disc&quot;
        * `"list-style-position"`: Specifies where to place the list-item marker. Default value is &quot;outside&quot;
        * `"list-style-image"`: Specifies the type of list-item marker. Default value is &quot;none&quot;
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_list_style', None)

    @listStyle.setter
    def listStyle(self, value):
        setattr(self, '_list_style', value)

    @listStyle.deleter
    def listStyle(self):
        delattr(self, '_list_style')

    @property
    def listStyleImage(self):
        """
        list-style-image

        Specifies an image as the list-item marker

        object.style.listStyleImage = "none|url|initial|inherit"

        * `"none"`: No image will be displayed. Instead, the list-style-type property will define what type of list marker will be rendered. This is default
        * `"url"`: The path to the image to be used as a list-item marker
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_list_style_image', None)

    @listStyleImage.setter
    def listStyleImage(self, value):
        setattr(self, '_list_style_image', value)

    @listStyleImage.deleter
    def listStyleImage(self):
        delattr(self, '_list_style_image')

    @property
    def listStylePosition(self):
        """
        list-style-position

        Specifies the position of the list-item markers (bullet points)

        object.style.listStylePosition = "inside|outside|initial|inherit"

        * `"inside"`: The bullet points will be inside the list item
        * `"outside"`: The bullet points will be outside the list item. This is default
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_list_style_position', None)

    @listStylePosition.setter
    def listStylePosition(self, value):
        setattr(self, '_list_style_position', value)

    @listStylePosition.deleter
    def listStylePosition(self):
        delattr(self, '_list_style_position')

    @property
    def listStyleType(self):
        """
        list-style-type

        Specifies the type of list-item marker

        object.style.listStyleType = "value"

        * `"disc"`: Default value. The marker is a filled circle
        * `"armenian"`: The marker is traditional Armenian numbering
        * `"circle"`: The marker is a circle
        * `"cjk-ideographic"`: The marker is plain ideographic numbers
        * `"decimal"`: The marker is a number
        * `"decimal-leading-zero"`: The marker is a number with leading zeros (01, 02,  03, etc.)
        * `"georgian"`: The marker is traditional Georgian numbering
        * `"hebrew"`: The marker is traditional Hebrew numbering
        * `"hiragana"`: The marker is traditional Hiragana numbering
        * `"hiragana-iroha"`: The marker is traditional Hiragana iroha numbering
        * `"katakana"`: The marker is traditional Katakana numbering
        * `"katakana-iroha"`: The marker is traditional Katakana iroha numbering
        * `"lower-alpha"`: The marker is lower-alpha (a, b, c, d, e, etc.)
        * `"lower-greek"`: The marker is lower-greek
        * `"lower-latin"`: The marker is lower-latin (a, b, c, d, e, etc.)
        * `"lower-roman"`: The marker is lower-roman (i, ii, iii, iv, v, etc.)
        * `"none"`: No marker is shown
        * `"square"`: The marker is a square
        * `"upper-alpha"`: The marker is upper-alpha (A, B, C, D, E, etc.)
        * `"upper-greek"`: The marker is upper-greek
        * `"upper-latin"`: The marker is upper-latin (A, B, C, D, E, etc.)
        * `"upper-roman"`: The marker is upper-roman (I, II, III, IV, V, etc.)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_list_style_type', None)

    @listStyleType.setter
    def listStyleType(self, value):
        setattr(self, '_list_style_type', value)

    @listStyleType.deleter
    def listStyleType(self):
        delattr(self, '_list_style_type')

    @property
    def margin(self):
        """
        margin

        Sets all the margin properties in one declaration

        object.style.margin = "length|auto|initial|inherit"

        * `"length"`: Specifies a margin in px, pt, cm, etc. Default value is 0. Negative values are allowed. Read about length units
        * `"%"`: Specifies a margin in percent of the width of the containing element
        * `"auto"`: The browser calculates a margin
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_margin', None)

    @margin.setter
    def margin(self, value):
        setattr(self, '_margin', value)

    @margin.deleter
    def margin(self):
        delattr(self, '_margin')

    @property
    def marginBottom(self):
        """
        margin-bottom

        Sets the bottom margin of an element

        object.style.marginBottom = "length|auto|initial|inherit"

        * `"length"`: Specifies a fixed bottom margin in px, cm, em, etc. Default value is 0. Negative values are allowed. Read about length units
        * `"%"`: Specifies a bottom margin in percent of the width of the containing element
        * `"auto"`: The browser calculates a bottom margin
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_margin_bottom', None)

    @marginBottom.setter
    def marginBottom(self, value):
        setattr(self, '_margin_bottom', value)

    @marginBottom.deleter
    def marginBottom(self):
        delattr(self, '_margin_bottom')

    @property
    def marginLeft(self):
        """
        margin-left

        Sets the left margin of an element

        object.style.marginLeft = "length|auto|initial|inherit"

        * `"length"`: Specifies a fixed left margin in px, pt, cm, etc. Default value is 0px. Negative values are allowed. Read about length units
        * `"%"`: Specifies a left margin in percent of the width of the containing element
        * `"auto"`: The browser calculates a left margin
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_margin_left', None)

    @marginLeft.setter
    def marginLeft(self, value):
        setattr(self, '_margin_left', value)

    @marginLeft.deleter
    def marginLeft(self):
        delattr(self, '_margin_left')

    @property
    def marginRight(self):
        """
        margin-right

        Sets the right margin of an element

        object.style.marginRight = "length|auto|initial|inherit"

        * `"length"`: Specifies a fixed right margin in px, pt, cm, etc. Default value is 0px. Read about length units
        * `"%"`: Specifies a right margin in percent of the width of the containing element
        * `"auto"`: The browser calculates a right margin
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_margin_right', None)

    @marginRight.setter
    def marginRight(self, value):
        setattr(self, '_margin_right', value)

    @marginRight.deleter
    def marginRight(self):
        delattr(self, '_margin_right')

    @property
    def marginTop(self):
        """
        margin-top

        Sets the top margin of an element

        object.style.marginTop = "length|auto|initial|inherit"

        * `"length"`: Specifies a fixed top margin in px, pt, cm, etc. Default value is 0px. Negative values are allowed. Read about length units
        * `"%"`: Specifies a top margin in percent of the width of the containing element
        * `"auto"`: The browser calculates a top margin
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_margin_top', None)

    @marginTop.setter
    def marginTop(self, value):
        setattr(self, '_margin_top', value)

    @marginTop.deleter
    def marginTop(self):
        delattr(self, '_margin_top')

    @property
    def maxHeight(self):
        """
        max-height

        Sets the maximum height of an element

        object.style.maxHeight = "none|length|initial|inherit"

        * `"none"`: No maximum height. This is default
        * `"length"`: Defines the maximum height in px, cm, etc. Read about length units
        * `"%"`: Defines the maximum height in percent of the containing block
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_max_height', None)

    @maxHeight.setter
    def maxHeight(self, value):
        setattr(self, '_max_height', value)

    @maxHeight.deleter
    def maxHeight(self):
        delattr(self, '_max_height')

    @property
    def maxWidth(self):
        """
        max-width

        Sets the maximum width of an element

        object.style.maxWidth = "none|length|initial|inherit"

        * `"none"`: No maximum width. This is default
        * `"length"`: Defines the maximum width in px, cm, etc. Read about length units
        * `"%"`: Defines the maximum width in percent of the containing block
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_max_width', None)

    @maxWidth.setter
    def maxWidth(self, value):
        setattr(self, '_max_width', value)

    @maxWidth.deleter
    def maxWidth(self):
        delattr(self, '_max_width')

    @property
    def media(self):
        """
        @media

        Sets the style rules for different media types/devices/sizes

        object.style.media = "not|only mediatype and (mediafeature  and|or|not mediafeature)"
        """
        return getattr(self, '_media', None)

    @media.setter
    def media(self, value):
        setattr(self, '_media', value)

    @media.deleter
    def media(self):
        delattr(self, '_media')

    @property
    def minHeight(self):
        """
        min-height

        Sets the minimum height of an element

        object.style.minHeight = "length|initial|inherit"

        * `"length"`: Default value is 0. Defines the minimum height in px, cm, etc. Read about length units
        * `"%"`: Defines the minimum height in percent of the containing block
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_min_height', None)

    @minHeight.setter
    def minHeight(self, value):
        setattr(self, '_min_height', value)

    @minHeight.deleter
    def minHeight(self):
        delattr(self, '_min_height')

    @property
    def minWidth(self):
        """
        min-width

        Sets the minimum width of an element

        object.style.minWidth = "length|initial|inherit"

        * `"length"`: Default value is 0. Defines the minimum width in px, cm, etc. Read about length units
        * `"%"`: Defines the minimum width in percent of the containing block
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_min_width', None)

    @minWidth.setter
    def minWidth(self, value):
        setattr(self, '_min_width', value)

    @minWidth.deleter
    def minWidth(self):
        delattr(self, '_min_width')

    @property
    def mixBlendMode(self):
        """
        mix-blend-mode

        Specifies how an element's content should blend with its direct parent background

        object.style.mixBlendMode = "normal|multiply|screen|overlay|darken|lighten|color-dodge|color-burn|difference|exclusion|hue|saturation|color|luminosity"

        * `"normal"`: This is default. Sets the blending mode to normal
        * `"multiply"`: Sets the blending mode to multiply
        * `"screen"`: Sets the blending mode to screen
        * `"overlay"`: Sets the blending mode to overlay
        * `"darken"`: Sets the blending mode to darken
        * `"lighten"`: Sets the blending mode to lighten
        * `"color-dodge"`: Sets the blending mode to color-dodge
        * `"color-burn"`: Sets the blending mode to color-burn
        * `"difference"`: Sets the blending mode to difference
        * `"exclusion"`: Sets the blending mode to exclusion
        * `"hue"`: Sets the blending mode to hue
        * `"saturation"`: Sets the blending mode to saturation
        * `"color"`: Sets the blending mode to color
        * `"luminosity"`: Sets the blending mode to luminosity
        """
        return getattr(self, '_mix_blend_mode', None)

    @mixBlendMode.setter
    def mixBlendMode(self, value):
        setattr(self, '_mix_blend_mode', value)

    @mixBlendMode.deleter
    def mixBlendMode(self):
        delattr(self, '_mix_blend_mode')

    @property
    def objectFit(self):
        """
        object-fit

        Specifies how the contents of a replaced element should be fitted to the box established by its used height and width

        object.style.objectFit = "fill|contain|cover|scale-down|none|initial|inherit"

        * `"fill"`: This is default. The replaced content is sized to fill the element's content box. If necessary, the object will be stretched or squished to fit
        * `"contain"`: The replaced content is scaled to maintain its aspect ratio while fitting within the element's content box
        * `"cover"`: The replaced content is sized to maintain its aspect ratio while filling the element's entire content box. The object will be clipped to fit
        * `"none"`: The replaced content is not resized
        * `"scale-down"`: The content is sized as if none or contain were specified (would result in a smaller concrete object size)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_object_fit', None)

    @objectFit.setter
    def objectFit(self, value):
        setattr(self, '_object_fit', value)

    @objectFit.deleter
    def objectFit(self):
        delattr(self, '_object_fit')

    @property
    def objectPosition(self):
        """
        object-position

        Specifies the alignment of the replaced element inside its box

        * `"position"`: Specifies the position of the image or video inside its content box. First value controls the x-asis and the second value controls the y-axis. Can be a string (left, center or right), or a number (in px or %). Negative values are allowed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_object_position', None)

    @objectPosition.setter
    def objectPosition(self, value):
        setattr(self, '_object_position', value)

    @objectPosition.deleter
    def objectPosition(self):
        delattr(self, '_object_position')

    @property
    def opacity(self):
        """
        opacity

        Sets the opacity level for an element

        object.style.opacity = "number|initial|inherit"

        * `"number"`: Specifies the opacity. From 0.0 (fully transparent) to 1.0 (fully opaque)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_opacity', None)

    @opacity.setter
    def opacity(self, value):
        setattr(self, '_opacity', value)

    @opacity.deleter
    def opacity(self):
        delattr(self, '_opacity')

    @property
    def order(self):
        """
        order

        Sets the order of the flexible item, relative to the rest

        object.style.order = "number|initial|inherit"

        * `"number"`: Default value 0. Specifies the order for the flexible item
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_order', None)

    @order.setter
    def order(self, value):
        setattr(self, '_order', value)

    @order.deleter
    def order(self):
        delattr(self, '_order')

    @property
    def orphans(self):
        """
        orphans

        Sets the minimum number of lines that must be left at the bottom of a page when a page break occurs inside an element
        """
        return getattr(self, '_orphans', None)

    @orphans.setter
    def orphans(self, value):
        setattr(self, '_orphans', value)

    @orphans.deleter
    def orphans(self):
        delattr(self, '_orphans')

    @property
    def outline(self):
        """
        outline

        A shorthand property for the outline-width, outline-style, and
    the outline-color properties

        object.style.outline = "outline-width outline-style outline-color|initial|inherit"

        * `"outline-width"`: Specifies the width of outline
        * `"outline-style"`: Specifies the style of the outline
        * `"outline-color"`: Specifies the color of the outline
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_outline', None)

    @outline.setter
    def outline(self, value):
        setattr(self, '_outline', value)

    @outline.deleter
    def outline(self):
        delattr(self, '_outline')

    @property
    def outlineColor(self):
        """
        outline-color

        Sets the color of an outline

        object.style.outlineColor = "invert|color|initial|inherit"

        * `"invert"`: Performs a color inversion. This ensures that the outline is visible, regardless of color background. This is default
        * `"color"`: Specifies the color of the outline. Look at CSS Color Values for a complete list of possible color values.
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_outline_color', None)

    @outlineColor.setter
    def outlineColor(self, value):
        setattr(self, '_outline_color', value)

    @outlineColor.deleter
    def outlineColor(self):
        delattr(self, '_outline_color')

    @property
    def outlineOffset(self):
        """
        outline-offset

        Offsets an outline, and draws it beyond the border edge

        object.style.outlineOffset = "length|initial|inherit"

        * `"length"`: The distance the outline is outset from the border edge. Default value is 0
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_outline_offset', None)

    @outlineOffset.setter
    def outlineOffset(self, value):
        setattr(self, '_outline_offset', value)

    @outlineOffset.deleter
    def outlineOffset(self):
        delattr(self, '_outline_offset')

    @property
    def outlineStyle(self):
        """
        outline-style

        Sets the style of an outline

        object.style.outlineStyle = "none|hidden|dotted|dashed|solid|double|groove|ridge|inset|outset|initial|inherit"

        * `"none"`: Specifies no outline. This is default
        * `"hidden"`: Specifies a hidden outline
        * `"dotted"`: Specifies a dotted outline
        * `"dashed"`: Specifies a dashed outline
        * `"solid"`: Specifies a solid outline
        * `"double"`: Specifies a double outliner
        * `"groove"`: Specifies a 3D grooved outline. The effect depends on the outline-color value
        * `"ridge"`: Specifies a 3D ridged outline. The effect depends on the outline-color value
        * `"inset"`: Specifies a 3D inset outline. The effect depends on the outline-color value
        * `"outset"`: Specifies a 3D outset outline. The effect depends on the outline-color value
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_outline_style', None)

    @outlineStyle.setter
    def outlineStyle(self, value):
        setattr(self, '_outline_style', value)

    @outlineStyle.deleter
    def outlineStyle(self):
        delattr(self, '_outline_style')

    @property
    def outlineWidth(self):
        """
        outline-width

        Sets the width of an outline

        object.style.outlineWidth = "medium|thin|thick|length|initial|inherit"

        * `"medium"`: Specifies a medium outline. This is default
        * `"thin"`: Specifies a thin outline
        * `"thick"`: Specifies a thick outline
        * `"length"`: Allows you to define the thickness of the outline. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_outline_width', None)

    @outlineWidth.setter
    def outlineWidth(self, value):
        setattr(self, '_outline_width', value)

    @outlineWidth.deleter
    def outlineWidth(self):
        delattr(self, '_outline_width')

    @property
    def overflow(self):
        """
        overflow

        Specifies what happens if content overflows an element's box

        object.style.overflow = "visible|hidden|scroll|auto|initial|inherit"

        * `"visible"`: The overflow is not clipped. It renders outside the element's box. This is default
        * `"hidden"`: The overflow is clipped, and the rest of the contentwill be invisible
        * `"scroll"`: The overflow is clipped, but a scroll-bar is added to see the rest of the content
        * `"auto"`: If overflow is clipped, a scroll-bar should be added to see the rest of the content
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_overflow', None)

    @overflow.setter
    def overflow(self, value):
        setattr(self, '_overflow', value)

    @overflow.deleter
    def overflow(self):
        delattr(self, '_overflow')

    @property
    def overflowWrap(self):
        """
        overflow-wrap

        Specifies whether or not the browser may break lines within words in order to prevent overflow (when a string is too long to fit its containing box)
        """
        return getattr(self, '_overflow_wrap', None)

    @overflowWrap.setter
    def overflowWrap(self, value):
        setattr(self, '_overflow_wrap', value)

    @overflowWrap.deleter
    def overflowWrap(self):
        delattr(self, '_overflow_wrap')

    @property
    def overflowX(self):
        """
        overflow-x

        Specifies whether or not to clip the left/right edges of the content, if it overflows the element's content area

        object.style.overflowX = "visible|hidden|scroll|auto|initial|inherit"

        * `"visible"`: The content is not clipped, and it may be rendered outside the left and right edges. This is default
        * `"hidden"`: The content is clipped - and no scrolling mechanism is provided
        * `"scroll"`: The content is clipped and a scrolling mechanism is provided
        * `"auto"`: Should cause a scrolling mechanism to be provided for overflowing boxes
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_overflow_x', None)

    @overflowX.setter
    def overflowX(self, value):
        setattr(self, '_overflow_x', value)

    @overflowX.deleter
    def overflowX(self):
        delattr(self, '_overflow_x')

    @property
    def overflowY(self):
        """
        overflow-y

        Specifies whether or not to clip the top/bottom edges of the content, if it overflows the element's content area

        object.style.overflowY = "visible|hidden|scroll|auto|initial|inherit"

        * `"visible"`: The content is not clipped, and it may be rendered outside the content box. This is default
        * `"hidden"`: The content is clipped - and no scrolling mechanism is provided
        * `"scroll"`: The content is clipped and a scrolling mechanism is provided
        * `"auto"`: Should cause a scrolling mechanism to be provided for overflowing boxes
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_overflow_y', None)

    @overflowY.setter
    def overflowY(self, value):
        setattr(self, '_overflow_y', value)

    @overflowY.deleter
    def overflowY(self):
        delattr(self, '_overflow_y')

    @property
    def padding(self):
        """
        padding

        A shorthand property for all the padding-* properties

        object.style.padding = "length|initial|inherit"

        * `"length"`: Specifies the padding in px, pt, cm, etc. Default value is 0. Read about length units
        * `"%"`: Specifies the padding in percent of the width of the containing element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_padding', None)

    @padding.setter
    def padding(self, value):
        setattr(self, '_padding', value)

    @padding.deleter
    def padding(self):
        delattr(self, '_padding')

    @property
    def paddingBottom(self):
        """
        padding-bottom

        Sets the bottom padding of an element

        object.style.paddingBottom = "length|initial|inherit"

        * `"length"`: Specifies a fixed bottom padding in px, pt, cm, etc. Default value is 0. Read about length units
        * `"%"`: Specifies a bottom padding in percent of the width of the element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_padding_bottom', None)

    @paddingBottom.setter
    def paddingBottom(self, value):
        setattr(self, '_padding_bottom', value)

    @paddingBottom.deleter
    def paddingBottom(self):
        delattr(self, '_padding_bottom')

    @property
    def paddingLeft(self):
        """
        padding-left

        Sets the left padding of an element

        object.style.paddingLeft = "length|initial|inherit"

        * `"length"`: Specifies a fixed left padding in px, pt, cm, etc. Default value is 0. Read about length units
        * `"%"`: Specifies a left padding in percent of the width of the element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_padding_left', None)

    @paddingLeft.setter
    def paddingLeft(self, value):
        setattr(self, '_padding_left', value)

    @paddingLeft.deleter
    def paddingLeft(self):
        delattr(self, '_padding_left')

    @property
    def paddingRight(self):
        """
        padding-right

        Sets the right padding of an element

        object.style.paddingRight = "length|initial|inherit"

        * `"length"`: Specifies a fixed right padding in px, pt, cm, etc. Default value is 0. Read about length units
        * `"%"`: Specifies a right padding in percent of the width of the element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_padding_right', None)

    @paddingRight.setter
    def paddingRight(self, value):
        setattr(self, '_padding_right', value)

    @paddingRight.deleter
    def paddingRight(self):
        delattr(self, '_padding_right')

    @property
    def paddingTop(self):
        """
        padding-top

        Sets the top padding of an element

        object.style.paddingTop = "length|initial|inherit"

        * `"length"`: Specifies a fixed top padding in px, pt, cm, etc. Default value is 0. Read about length units
        * `"%"`: Specifies a top padding in percent of the width of the element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_padding_top', None)

    @paddingTop.setter
    def paddingTop(self, value):
        setattr(self, '_padding_top', value)

    @paddingTop.deleter
    def paddingTop(self):
        delattr(self, '_padding_top')

    @property
    def pageBreakAfter(self):
        """
        page-break-after

        Sets the page-break behavior after an element

        object.style.pageBreakAfter = "auto|always|avoid|left|right|initial|inherit"

        * `"auto"`: Default. Automatic page-break
        * `"always"`: Always insert a page-break after the element
        * `"avoid"`: Avoid a page-break after the element (if possible)
        * `"left"`: Insert page-break after the element so that the next page is   formatted as a left page
        * `"right"`: Insert page-break after the element so that the next page is   formatted as a right page
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_page_break_after', None)

    @pageBreakAfter.setter
    def pageBreakAfter(self, value):
        setattr(self, '_page_break_after', value)

    @pageBreakAfter.deleter
    def pageBreakAfter(self):
        delattr(self, '_page_break_after')

    @property
    def pageBreakBefore(self):
        """
        page-break-before

        Sets the page-break behavior before an element

        object.style.pageBreakBefore = "auto|always|avoid|left|right|initial|inherit"

        * `"auto"`: Default. Automatic page-breaks
        * `"always"`: Always insert a page-break before the element
        * `"avoid"`: Avoid page-break before the element (if possible)
        * `"left"`: Insert page-break before the element so that the next page is   formatted as a left page
        * `"right"`: Insert page-break before the element so that the next page is   formatted as a right page
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_page_break_before', None)

    @pageBreakBefore.setter
    def pageBreakBefore(self, value):
        setattr(self, '_page_break_before', value)

    @pageBreakBefore.deleter
    def pageBreakBefore(self):
        delattr(self, '_page_break_before')

    @property
    def pageBreakInside(self):
        """
        page-break-inside

        Sets the page-break behavior inside an element

        object.style.pageBreakInside = "auto|avoid|initial|inherit"

        * `"auto"`: Default. Automatic page-breaks
        * `"avoid"`: Avoid page-break inside the element (if possible)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_page_break_inside', None)

    @pageBreakInside.setter
    def pageBreakInside(self, value):
        setattr(self, '_page_break_inside', value)

    @pageBreakInside.deleter
    def pageBreakInside(self):
        delattr(self, '_page_break_inside')

    @property
    def perspective(self):
        """
        perspective

        Gives a 3D-positioned element some perspective

        object.style.perspective = "length|none"

        * `"length"`: How far the element is placed from the view
        * `"none"`: Default value. Same as 0. The perspective is not set
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_perspective', None)

    @perspective.setter
    def perspective(self, value):
        setattr(self, '_perspective', value)

    @perspective.deleter
    def perspective(self):
        delattr(self, '_perspective')

    @property
    def perspectiveOrigin(self):
        """
        perspective-origin

        Defines at which position the user is looking at the 3D-positioned element

        object.style.perspectiveOrigin = "x-axis y-axis|initial|inherit"

        * `"x-axis"`: Defining where the view is placed at the x-axisPossible values:  left center right length %  Default value: 50%
        * `"y-axis"`: Defining where the view is placed at the y-axisPossible values:  top center bottom length %  Default value: 50%
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_perspective_origin', None)

    @perspectiveOrigin.setter
    def perspectiveOrigin(self, value):
        setattr(self, '_perspective_origin', value)

    @perspectiveOrigin.deleter
    def perspectiveOrigin(self):
        delattr(self, '_perspective_origin')

    @property
    def pointerEvents(self):
        """
        pointer-events

        Defines whether or not an element reacts to pointer events

        object.style.pointerEvents = "auto|none"

        * `"auto"`: The element reacts to pointer events, like :hover and click. This is default
        * `"none"`: The element does not react to pointer events
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_pointer_events', None)

    @pointerEvents.setter
    def pointerEvents(self, value):
        setattr(self, '_pointer_events', value)

    @pointerEvents.deleter
    def pointerEvents(self):
        delattr(self, '_pointer_events')

    @property
    def position(self):
        """
        position

        Specifies the type of positioning method used for an element (static, relative, absolute or fixed)

        object.style.position = "static|absolute|fixed|relative|sticky|initial|inherit"

        * `"static"`: Default value. Elements render in order, as they appear in the document flow
        * `"absolute"`: The element is positioned relative to its first positioned (not static) ancestor element
        * `"fixed"`: The element is positioned relative to the browser window
        * `"relative"`: The element is positioned relative to its normal position, so &quot;left:20px&quot; adds 20 pixels to the element's LEFT position
        * `"sticky"`: The element is positioned based on the user's scroll position A sticky element toggles between relative and fixed, depending on the scroll position. It is positioned relative until a given offset position is met in the viewport - then it "sticks" in place (like position:fixed). Note: Not supported in IE/Edge 15 or earlier. Supported in Safari from version 6.1 with a -webkit- prefix.
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_position', None)

    @position.setter
    def position(self, value):
        setattr(self, '_position', value)

    @position.deleter
    def position(self):
        delattr(self, '_position')

    @property
    def quotes(self):
        """
        quotes

        Sets the type of quotation marks for embedded quotations

        object.style.quotes = "none|string|initial|inherit"

        * `"none"`: Specifies that the "open-quote" and "close-quote" values of the "content" property will not produce any quotation marks
        * `"string string string string"`: Specifies which quotation marks to use. The first two values specifies the first level of quotation embedding, the next two values specifies the next level of quote embedding, etc
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_quotes', None)

    @quotes.setter
    def quotes(self, value):
        setattr(self, '_quotes', value)

    @quotes.deleter
    def quotes(self):
        delattr(self, '_quotes')

    @property
    def resize(self):
        """
        resize

        Defines if (and how) an element is resizable by the user

        object.style.resize = "none|both|horizontal|vertical|initial|inherit"

        * `"none"`: Default value. The user cannot resize the element
        * `"both"`: The user can resize both the height and width of the element
        * `"horizontal"`: The user can resize the width of the element
        * `"vertical"`: The user can resize the height of the element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_resize', None)

    @resize.setter
    def resize(self, value):
        setattr(self, '_resize', value)

    @resize.deleter
    def resize(self):
        delattr(self, '_resize')

    @property
    def right(self):
        """
        right

        Specifies the right position of a positioned element

        object.style.right = "auto|length|initial|inherit"

        * `"auto"`: Lets the browser calculate the right edge position. This is default
        * `"length"`: Sets the right edge position in px, cm, etc. Negative values are allowed. Read about length units
        * `"%"`: Sets the right edge position in % of containing element. Negative values are allowed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_right', None)

    @right.setter
    def right(self, value):
        setattr(self, '_right', value)

    @right.deleter
    def right(self):
        delattr(self, '_right')

    @property
    def scrollBehavior(self):
        """
        scroll-behavior

        Specifies whether to smoothly animate the scroll position in a scrollable box, instead of a straight jump

        object.style.scrollBehavior = "auto|smooth|initial|inherit"

        * `"auto"`: Allows a straight jump "scroll effect" between elements within the scrolling box. This is default
        * `"smooth"`: Allows a smooth animated "scroll effect" between elements within the scrolling box.
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_scroll_behavior', None)

    @scrollBehavior.setter
    def scrollBehavior(self, value):
        setattr(self, '_scroll_behavior', value)

    @scrollBehavior.deleter
    def scrollBehavior(self):
        delattr(self, '_scroll_behavior')

    @property
    def tabSize(self):
        """
        tab-size

        Specifies the width of a tab character

        object.style.tabSize = "number|length|initial|inherit"

        * `"number"`: The number of space-characters to be displayed for each tab-character. Default value is 8
        * `"length"`: The length of a tab-character. This property value is not supported in any of the major browsers
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_tab_size', None)

    @tabSize.setter
    def tabSize(self, value):
        setattr(self, '_tab_size', value)

    @tabSize.deleter
    def tabSize(self):
        delattr(self, '_tab_size')

    @property
    def tableLayout(self):
        """
        table-layout

        Defines the algorithm used to lay out table cells, rows, and columns

        object.style.tableLayout = "auto|fixed|initial|inherit"

        * `"auto"`: Browsers use an automatic table layout algorithm. The column width is set by the widest unbreakable content in the cells. The content will dictate the layout
        * `"fixed"`: Sets a fixed table layout algorithm. The table and column widths are set by the widths of table and col or by the width of the first row of cells. Cells in other rows do not affect column widths. If no widths are present on the first row, the column widths are divided equally across the table, regardless of content inside the cells
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_table_layout', None)

    @tableLayout.setter
    def tableLayout(self, value):
        setattr(self, '_table_layout', value)

    @tableLayout.deleter
    def tableLayout(self):
        delattr(self, '_table_layout')

    @property
    def textAlign(self):
        """
        text-align

        Specifies the horizontal alignment of text

        object.style.textAlign = "left|right|center|justify|initial|inherit"

        * `"left"`: Aligns the text to the left
        * `"right"`: Aligns the text to the right
        * `"center"`: Centers the text
        * `"justify"`: Stretches the lines so that each line has equal width (like in newspapers and magazines)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_align', None)

    @textAlign.setter
    def textAlign(self, value):
        setattr(self, '_text_align', value)

    @textAlign.deleter
    def textAlign(self):
        delattr(self, '_text_align')

    @property
    def textAlignLast(self):
        """
        text-align-last

        Describes how the last line of a block or a line right before a forced line break is aligned when text-align is &quot;justify&quot;

        object.style.textAlignLast = "auto|left|right|center|justify|start|end|initial|inherit"

        * `"auto"`: Default value. The last line is justified and aligned left
        * `"left"`: The last line is aligned to the left
        * `"right"`: The last line is aligned to the right
        * `"center"`: The last line is center-aligned
        * `"justify"`: The last line is justified as the rest of the lines
        * `"start"`: The last line is aligned at the beginning of the line (left if the text-direction is left-to-right, and right is the text-direction is right-to-left)
        * `"end"`: The last line is aligned at the end of the line (right if the text-direction is left-to-right, and left is the text-direction is right-to-left)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_align_last', None)

    @textAlignLast.setter
    def textAlignLast(self, value):
        setattr(self, '_text_align_last', value)

    @textAlignLast.deleter
    def textAlignLast(self):
        delattr(self, '_text_align_last')

    @property
    def textCombineUpright(self):
        """
        text-combine-upright

        Specifies the combination of multiple characters into the space of a single character
        """
        return getattr(self, '_text_combine_upright', None)

    @textCombineUpright.setter
    def textCombineUpright(self, value):
        setattr(self, '_text_combine_upright', value)

    @textCombineUpright.deleter
    def textCombineUpright(self):
        delattr(self, '_text_combine_upright')

    @property
    def textDecoration(self):
        """
        text-decoration

        Specifies the decoration added to text

        object.style.textDecoration = "text-decoration-line text-decoration-color text-decoration-style|initial|inherit"

        * `"text-decoration-line"`: Sets the kind of text decoration to use (like underline, overline, line-through)
        * `"text-decoration-color"`: Sets the color of the text decoration
        * `"text-decoration-style"`: Sets the style of the text decoration (like solid, wavy, dotted, dashed, double)
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_decoration', None)

    @textDecoration.setter
    def textDecoration(self, value):
        setattr(self, '_text_decoration', value)

    @textDecoration.deleter
    def textDecoration(self):
        delattr(self, '_text_decoration')

    @property
    def textDecorationColor(self):
        """
        text-decoration-color

        Specifies the color of the text-decoration

        object.style.textDecorationColor = "color|initial|inherit"

        * `"color"`: Specifies the color of the text-decoration
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_decoration_color', None)

    @textDecorationColor.setter
    def textDecorationColor(self, value):
        setattr(self, '_text_decoration_color', value)

    @textDecorationColor.deleter
    def textDecorationColor(self):
        delattr(self, '_text_decoration_color')

    @property
    def textDecorationLine(self):
        """
        text-decoration-line

        Specifies the type of line in a text-decoration

        object.style.textDecorationLine = "none|underline|overline|line-through|initial|inherit"

        * `"none"`: Default value. Specifies no line for the text-decoration
        * `"underline"`: Specifies that a line will be displayed under the text
        * `"overline"`: Specifies that a line will be displayed over the text
        * `"line-through"`: Specifies that a line will be displayed through the text
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_decoration_line', None)

    @textDecorationLine.setter
    def textDecorationLine(self, value):
        setattr(self, '_text_decoration_line', value)

    @textDecorationLine.deleter
    def textDecorationLine(self):
        delattr(self, '_text_decoration_line')

    @property
    def textDecorationStyle(self):
        """
        text-decoration-style

        Specifies the style of the line in a text decoration

        object.style.textDecorationStyle = "solid|double|dotted|dashed|wavy|initial|inherit"

        * `"solid"`: Default value. The line will display as a single line
        * `"double"`: The line will display as a double line
        * `"dotted"`: The line will display as a dotted line
        * `"dashed"`: The line will display as a dashed line
        * `"wavy"`: The line will display as a wavy line
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_decoration_style', None)

    @textDecorationStyle.setter
    def textDecorationStyle(self, value):
        setattr(self, '_text_decoration_style', value)

    @textDecorationStyle.deleter
    def textDecorationStyle(self):
        delattr(self, '_text_decoration_style')

    @property
    def textIndent(self):
        """
        text-indent

        Specifies the indentation of the first line in a text-block

        object.style.textIndent = "length|initial|inherit"

        * `"length"`: Defines a fixed indentation in px, pt, cm, em, etc. Default value is 0. Read about length units
        * `"%"`: Defines the indentation in % of the width of the parent element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_indent', None)

    @textIndent.setter
    def textIndent(self, value):
        setattr(self, '_text_indent', value)

    @textIndent.deleter
    def textIndent(self):
        delattr(self, '_text_indent')

    @property
    def textJustify(self):
        """
        text-justify

        Specifies the justification method used when text-align is &quot;justify&quot;

        object.style.textJustify = "auto|inter-word|inter-character|none|initial|inherit"

        * `"auto"`: The browser determines the justification algorithm
        * `"inter-word"`: Increases/Decreases the space between words
        * `"inter-character"`: Increases/Decreases the space between characters
        * `"none"`: Disables justification methods
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_justify', None)

    @textJustify.setter
    def textJustify(self, value):
        setattr(self, '_text_justify', value)

    @textJustify.deleter
    def textJustify(self):
        delattr(self, '_text_justify')

    @property
    def textOrientation(self):
        """
        text-orientation

        Defines the orientation of the text in a line
        """
        return getattr(self, '_text_orientation', None)

    @textOrientation.setter
    def textOrientation(self, value):
        setattr(self, '_text_orientation', value)

    @textOrientation.deleter
    def textOrientation(self):
        delattr(self, '_text_orientation')

    @property
    def textOverflow(self):
        """
        text-overflow

        Specifies what should happen when text overflows the containing element

        object.style.textOverflow = "clip|ellipsis|string|initial|inherit"

        * `"clip"`: Default value. The text is clipped and not accessible
        * `"ellipsis"`: Render an ellipsis (&quot;...&quot;) to represent the clipped text
        * `"string"`: Render the given string to represent the clipped text
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_overflow', None)

    @textOverflow.setter
    def textOverflow(self, value):
        setattr(self, '_text_overflow', value)

    @textOverflow.deleter
    def textOverflow(self):
        delattr(self, '_text_overflow')

    @property
    def textShadow(self):
        """
        text-shadow

        Adds shadow to text

        object.style.textShadow = "h-shadow v-shadow blur-radius color|none|initial|inherit"

        * `"h-shadow"`: Required. The position of the horizontal shadow. Negative values are allowed
        * `"v-shadow"`: Required. The position of the vertical shadow. Negative values are allowed
        * `"blur-radius"`: Optional. The blur radius. Default value is 0
        * `"color"`: Optional. The color of the shadow. Look at CSS Color Values for a complete list of possible color values
        * `"none"`: Default value. No shadow
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_shadow', None)

    @textShadow.setter
    def textShadow(self, value):
        setattr(self, '_text_shadow', value)

    @textShadow.deleter
    def textShadow(self):
        delattr(self, '_text_shadow')

    @property
    def textTransform(self):
        """
        text-transform

        Controls the capitalization of text

        object.style.textTransform = "none|capitalize|uppercase|lowercase|initial|inherit"

        * `"none"`: No capitalization. The text renders as it is. This is default
        * `"capitalize"`: Transforms the first character of each word to uppercase
        * `"uppercase"`: Transforms all characters to uppercase
        * `"lowercase"`: Transforms all characters to lowercase
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_text_transform', None)

    @textTransform.setter
    def textTransform(self, value):
        setattr(self, '_text_transform', value)

    @textTransform.deleter
    def textTransform(self):
        delattr(self, '_text_transform')

    @property
    def textUnderlinePosition(self):
        """
        text-underline-position

        Specifies the position of the underline which is set using the text-decoration property
        """
        return getattr(self, '_text_underline_position', None)

    @textUnderlinePosition.setter
    def textUnderlinePosition(self, value):
        setattr(self, '_text_underline_position', value)

    @textUnderlinePosition.deleter
    def textUnderlinePosition(self):
        delattr(self, '_text_underline_position')

    @property
    def top(self):
        """
        top

        Specifies the top position of a positioned element

        object.style.top = "auto|length|initial|inherit"

        * `"auto"`: Lets the browser calculate the top edge position. This is default
        * `"length"`: Sets the top edge position in px, cm, etc. Negative values are allowed. Read about length units
        * `"%"`: Sets the top edge position in % of containing element. Negative values are allowed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_top', None)

    @top.setter
    def top(self, value):
        setattr(self, '_top', value)

    @top.deleter
    def top(self):
        delattr(self, '_top')

    @property
    def transform(self):
        """
        transform

        Applies a 2D or 3D transformation to an element

        * `"none"`: Defines that there should be no transformation
        * `"matrix(n,n,n,n,n,n)"`: Defines a 2D transformation, using a matrix of six values
        * `"matrix3d (n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n)"`: Defines a 3D transformation, using a 4x4 matrix of 16 values
        * `"translate(x,y)"`: Defines a 2D translation
        * `"translate3d(x,y,z)"`: Defines a 3D translation
        * `"translateX(x)"`: Defines a translation, using only the value for the X-axis
        * `"translateY(y)"`: Defines a translation, using only the value for the Y-axis
        * `"translateZ(z)"`: Defines a 3D translation, using only the value for the Z-axis
        * `"scale(x,y)"`: Defines a 2D scale transformation
        * `"scale3d(x,y,z)"`: Defines a 3D scale transformation
        * `"scaleX(x)"`: Defines a scale transformation by giving a value for the X-axis
        * `"scaleY(y)"`: Defines a scale transformation by giving a value for the Y-axis
        * `"scaleZ(z)"`: Defines a 3D scale transformation by giving a value for the Z-axis
        * `"rotate(angle)"`: Defines a 2D rotation, the angle is specified in the  parameter
        * `"rotate3d(x,y,z,angle)"`: Defines a 3D rotation
        * `"rotateX(angle)"`: Defines a 3D rotation along the X-axis
        * `"rotateY(angle)"`: Defines a 3D rotation along the Y-axis
        * `"rotateZ(angle)"`: Defines a 3D rotation along the Z-axis
        * `"skew(x-angle,y-angle)"`: Defines a 2D skew transformation along the X- and the Y-axis
        * `"skewX(angle)"`: Defines a 2D skew transformation along the X-axis
        * `"skewY(angle)"`: Defines a 2D skew transformation along the Y-axis
        * `"perspective(n)"`: Defines a perspective view for a 3D transformed element
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transform', None)

    @transform.setter
    def transform(self, value):
        setattr(self, '_transform', value)

    @transform.deleter
    def transform(self):
        delattr(self, '_transform')

    @property
    def transformOrigin(self):
        """
        transform-origin

        Allows you to change the position on transformed elements

        object.style.transformOrigin = "x-axis y-axis z-axis|initial|inherit"

        * `"x-axis"`: Defines where the view is placed at the x-axis. Possible values: left center right length %
        * `"y-axis"`: Defines where the view is placed at the y-axis. Possible values: top center bottom length %
        * `"z-axis"`: Defines where the view is placed at the z-axis (for 3D transformations). Possible values: length
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transform_origin', None)

    @transformOrigin.setter
    def transformOrigin(self, value):
        setattr(self, '_transform_origin', value)

    @transformOrigin.deleter
    def transformOrigin(self):
        delattr(self, '_transform_origin')

    @property
    def transformStyle(self):
        """
        transform-style

        Specifies how nested elements are rendered in 3D space

        object.style.transformStyle = "flat|preserve-3d|initial|inherit"

        * `"flat"`: Specifies that child elements will NOT preserve its 3D position. This is default
        * `"preserve-3d"`: Specifies that child elements will preserve its 3D position
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transform_style', None)

    @transformStyle.setter
    def transformStyle(self, value):
        setattr(self, '_transform_style', value)

    @transformStyle.deleter
    def transformStyle(self):
        delattr(self, '_transform_style')

    @property
    def transition(self):
        """
        transition

        A shorthand property for all the transition-* properties

        object.style.transition = "property duration timing-function delay|initial|inherit"

        * `"transition-property"`: Specifies the name of the CSS property the transition effect is for
        * `"transition-duration"`: Specifies how many seconds or milliseconds the transition effect takes to complete
        * `"transition-timing-function"`: Specifies the speed curve of the transition effect
        * `"transition-delay"`: Defines when the transition effect will start
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transition', None)

    @transition.setter
    def transition(self, value):
        setattr(self, '_transition', value)

    @transition.deleter
    def transition(self):
        delattr(self, '_transition')

    @property
    def transitionDelay(self):
        """
        transition-delay

        Specifies when the transition effect will start

        object.style.transitionDelay = "time|initial|inherit"

        * `"time"`: Specifies the number of seconds or milliseconds to wait before the transition effect will start
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transition_delay', None)

    @transitionDelay.setter
    def transitionDelay(self, value):
        setattr(self, '_transition_delay', value)

    @transitionDelay.deleter
    def transitionDelay(self):
        delattr(self, '_transition_delay')

    @property
    def transitionDuration(self):
        """
        transition-duration

        Specifies how many seconds or milliseconds a transition effect takes to complete

        object.style.transitionDuration = "time|initial|inherit"

        * `"time"`: Specifies how many seconds or milliseconds a transition effect takes to complete. Default value is 0s, meaning there will be no effect
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transition_duration', None)

    @transitionDuration.setter
    def transitionDuration(self, value):
        setattr(self, '_transition_duration', value)

    @transitionDuration.deleter
    def transitionDuration(self):
        delattr(self, '_transition_duration')

    @property
    def transitionProperty(self):
        """
        transition-property

        Specifies the name of the CSS property the transition effect is for

        object.style.transitionProperty = "none|all|property|initial|inherit"

        * `"none"`: No property will get a transition effect
        * `"all"`: Default value. All properties will get a transition effect
        * `"property"`: Defines a comma separated list of CSS property names the transition effect is for
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transition_property', None)

    @transitionProperty.setter
    def transitionProperty(self, value):
        setattr(self, '_transition_property', value)

    @transitionProperty.deleter
    def transitionProperty(self):
        delattr(self, '_transition_property')

    @property
    def transitionTimingFunction(self):
        """
        transition-timing-function

        Specifies the speed curve of the transition effect

        object.style.transitionTimingFunction = "linear|ease|ease-in|ease-out|ease-in-out|step-start|step-end|steps(int,start|end)|cubic-bezier(n,n,n,n)|initial|inherit"

        * `"ease"`: Default value. Specifies a transition effect with a slow start, then fast, then end slowly (equivalent to cubic-bezier(0.25,0.1,0.25,1))
        * `"linear"`: Specifies a transition effect with the same speed from start to end (equivalent to cubic-bezier(0,0,1,1))
        * `"ease-in"`: Specifies a transition effect with a slow start (equivalent to cubic-bezier(0.42,0,1,1))
        * `"ease-out"`: Specifies a transition effect with a slow end (equivalent to cubic-bezier(0,0,0.58,1))
        * `"ease-in-out"`: Specifies a transition effect with a slow start and end (equivalent to cubic-bezier(0.42,0,0.58,1))
        * `"step-start"`: Equivalent to steps(1, start)
        * `"step-end"`: Equivalent to steps(1, end)
        * `"steps(int,start|end)"`: Specifies a stepping function, with two parameters. The first parameter specifies the number of intervals in the function. It must be a positive integer (greater than 0). The second parameter, which is optional, is either the value &quot;start&quot; or &quot;end&quot;, and specifies the point at which the change of values occur within the interval. If the second parameter is omitted, it is given the value &quot;end&quot;
        * `"cubic-bezier(n,n,n,n)"`: Define your own values in the cubic-bezier function. Possible values are numeric values from 0 to 1
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_transition_timing_function', None)

    @transitionTimingFunction.setter
    def transitionTimingFunction(self, value):
        setattr(self, '_transition_timing_function', value)

    @transitionTimingFunction.deleter
    def transitionTimingFunction(self):
        delattr(self, '_transition_timing_function')

    @property
    def unicodeBidi(self):
        """
        unicode-bidi

        Used together with the direction property to set or return whether the text should be overridden to support multiple languages in the same document

        object.style.unicodeBidi = "normal|embed|bidi-override|initial|inherit"

        * `"normal"`: The element does not open an additional level of embedding. This is default
        * `"embed"`: For inline elements, this value opens an additional level of embedding
        * `"bidi-override"`: For inline elements, this creates an override. For block elements, this creates an override for inline-level descendants not within another block element
        * `"isolate"`: The element is isolated from its siblings
        * `"isolate-override"`:
        * `"plaintext"`:
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_unicode_bidi', None)

    @unicodeBidi.setter
    def unicodeBidi(self, value):
        setattr(self, '_unicode_bidi', value)

    @unicodeBidi.deleter
    def unicodeBidi(self):
        delattr(self, '_unicode_bidi')

    @property
    def userSelect(self):
        """
        user-select

        Specifies whether the text of an element can be selected

        object.style.userSelect = "auto|none|text|all"

        * `"auto"`: Default. Text can be selected if the browser allows it
        * `"none"`: Prevent text selection
        * `"text"`: The text can be selected by the user
        * `"all"`: Text selection is made with one click instead of a double-click
        """
        return getattr(self, '_user_select', None)

    @userSelect.setter
    def userSelect(self, value):
        setattr(self, '_user_select', value)

    @userSelect.deleter
    def userSelect(self):
        delattr(self, '_user_select')

    @property
    def verticalAlign(self):
        """
        vertical-align

        Sets the vertical alignment of an element

        object.style.verticalAlign = "baseline|length|sub|super|top|text-top|middle|bottom|text-bottom|initial|inherit"

        * `"baseline"`: The element is aligned with the baseline of the parent. This is default
        * `"length"`: Raises or lower an element by the specified length. Negative values are allowed. Read about length units
        * `"%"`: Raises or lower an element in a percent of the &quot;line-height&quot; property. Negative values are allowed
        * `"sub"`: The element is aligned with the subscript baseline of the parent
        * `"super"`: The element is aligned with the superscript baseline of the parent
        * `"top"`: The element is aligned with the top of the tallest element on the line
        * `"text-top"`: The element is aligned with the top of the parent element's font
        * `"middle"`: The element is placed in the middle of the parent element
        * `"bottom"`: The element is aligned with the lowest element on the line
        * `"text-bottom"`: The element is aligned with the bottom of the parent element's font
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_vertical_align', None)

    @verticalAlign.setter
    def verticalAlign(self, value):
        setattr(self, '_vertical_align', value)

    @verticalAlign.deleter
    def verticalAlign(self):
        delattr(self, '_vertical_align')

    @property
    def visibility(self):
        """
        visibility

        Specifies whether or not an element is visible

        object.style.visibility = "visible|hidden|collapse|initial|inherit"

        * `"visible"`: Default value. The element is visible
        * `"hidden"`: The element is hidden (but still takes up space)
        * `"collapse"`: Only for table rows (&lt;tr&gt;), row groups (&lt;tbody&gt;), columns (&lt;col&gt;), column groups (&lt;colgroup&gt;). This value removes a row or column, but it does not affect the table layout. The space taken up by the row or column will be available for other content.If collapse is used on other elements, it renders as &quot;hidden&quot;
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_visibility', None)

    @visibility.setter
    def visibility(self, value):
        setattr(self, '_visibility', value)

    @visibility.deleter
    def visibility(self):
        delattr(self, '_visibility')

    @property
    def whiteSpace(self):
        """
        white-space

        Specifies how white-space inside an element is handled

        object.style.whiteSpace = "normal|nowrap|pre|pre-line|pre-wrap|initial|inherit"

        * `"normal"`: Sequences of whitespace will collapse into a single whitespace. Text will wrap when necessary. This is default
        * `"nowrap"`: Sequences of whitespace will collapse into a single whitespace. Text will never wrap to the next line. The text continues on the same line until a &lt;br&gt; tag is encountered
        * `"pre"`: Whitespace is preserved by the browser. Text will only wrap on line breaks. Acts like the &lt;pre&gt; tag in HTML
        * `"pre-line"`: Sequences of whitespace will collapse into a single whitespace. Text will wrap when necessary, and on line breaks
        * `"pre-wrap"`: Whitespace is preserved by the browser. Text will wrap when necessary, and on line breaks
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_white_space', None)

    @whiteSpace.setter
    def whiteSpace(self, value):
        setattr(self, '_white_space', value)

    @whiteSpace.deleter
    def whiteSpace(self):
        delattr(self, '_white_space')

    @property
    def widows(self):
        """
        widows

        Sets the minimum number of lines that must be left at the top of a page when a page break occurs inside an element
        """
        return getattr(self, '_widows', None)

    @widows.setter
    def widows(self, value):
        setattr(self, '_widows', value)

    @widows.deleter
    def widows(self):
        delattr(self, '_widows')

    @property
    def width(self):
        """
        width

        Sets the width of an element

        object.style.width = "auto|value|initial|inherit"

        * `"auto"`: Default value. The browser calculates the width
        * `"length"`: Defines the width in px, cm, etc. Read about length units
        * `"%"`: Defines the width in percent of the containing block
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_width', None)

    @width.setter
    def width(self, value):
        setattr(self, '_width', value)

    @width.deleter
    def width(self):
        delattr(self, '_width')

    @property
    def wordBreak(self):
        """
        word-break

        Specifies how words should break when reaching the end of a line

        object.style.wordBreak = "normal|break-all|keep-all|break-word|initial|inherit"

        * `"normal"`: Default value. Uses default line break rules
        * `"break-all"`: To prevent overflow, word may be broken at any character
        * `"keep-all"`: Word breaks should not be used for Chinese/Japanese/Korean (CJK) text. Non-CJK text behavior is the same as value &quot;normal&quot;
        * `"break-word"`: To prevent overflow, word may be broken at arbitrary points
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_word_break', None)

    @wordBreak.setter
    def wordBreak(self, value):
        setattr(self, '_word_break', value)

    @wordBreak.deleter
    def wordBreak(self):
        delattr(self, '_word_break')

    @property
    def wordSpacing(self):
        """
        word-spacing

        Increases or decreases the space between words in a text

        object.style.wordSpacing = "normal|length|initial|inherit"

        * `"normal"`: Defines normal space between words (0.25em). This is default
        * `"length"`: Defines an additional space between words (in px, pt, cm, em, etc). Negative values are allowed. Read about length units
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_word_spacing', None)

    @wordSpacing.setter
    def wordSpacing(self, value):
        setattr(self, '_word_spacing', value)

    @wordSpacing.deleter
    def wordSpacing(self):
        delattr(self, '_word_spacing')

    @property
    def wordWrap(self):
        """
        word-wrap

        Allows long, unbreakable words to be broken and wrap to the next line

        object.style.wordWrap = "normal|break-word|initial|inherit"

        * `"normal"`: Break words only at allowed break points
        * `"break-word"`: Allows unbreakable words to be broken
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_word_wrap', None)

    @wordWrap.setter
    def wordWrap(self, value):
        setattr(self, '_word_wrap', value)

    @wordWrap.deleter
    def wordWrap(self):
        delattr(self, '_word_wrap')

    @property
    def writingMode(self):
        """
        writing-mode

        Specifies whether lines of text are laid out horizontally or vertically

        object.style.writingMode = "horizontal-tb|vertical-rl|vertical-lr"

        * `"horizontal-tb"`: Let the content flow horizontally from left to right, vertically from top to bottom
        * `"vertical-rl"`: Let the content flow vertically from top to bottom, horizontally from right to left
        * `"vertical-lr"`: Let the content flow vertically from top to bottom, horizontally from left to right
        """
        return getattr(self, '_writing_mode', None)

    @writingMode.setter
    def writingMode(self, value):
        setattr(self, '_writing_mode', value)

    @writingMode.deleter
    def writingMode(self):
        delattr(self, '_writing_mode')

    @property
    def zIndex(self):
        """
        z-index

        Sets the stack order of a positioned element

        object.style.zIndex = "auto|number|initial|inherit"

        * `"auto"`: Sets the stack order equal to its parents. This is default
        * `"number"`: Sets the stack order of the element. Negative numbers are allowed
        * `"initial"`: Sets this property to its default value. Read about initial
        * `"inherit"`: Inherits this property from its parent element. Read about inherit
        """
        return getattr(self, '_z_index', None)

    @zIndex.setter
    def zIndex(self, value):
        setattr(self, '_z_index', value)

    @zIndex.deleter
    def zIndex(self):
        delattr(self, '_z_index')


class media(css_base):
    def __init__(self):
        css_base.__init__(self)
        self._selector = '@media'
        self._media_type = 'screen'
        self._media_feature = None
        self._type_operator = 'only'

    @property
    def mediaType(self):
        return self._media_type

    @mediaType.setter
    def mediaType(self, value):
        """
        * `"all"`: Default. Used for all media type devices
        * `"print"`: Used for printers
        * `"screen"`: Used for computer screens, tablets, smart-phones etc.
        * `"speech"`: Used for screen readers that "reads" the page out loud
        """
        self._media_type = value

    @property
    def typeOperator(self):
        """
        * `"only"`
        * `"not"`
        """
        return self._type_operator

    @typeOperator.setter
    def typeOperator(self, value):
        self._type_operator = value

    @property
    def mediaFeature(self):
        """
        mediafeature and|or|not mediafeature

        `"any-hover"`: Does any available input mechanism allow the user to hover over elements? (added in Media Queries Level 4)
        `"any-pointer"`: Is any available input mechanism a pointing device, and if so, how accurate is it? (added in Media Queries Level 4)
        `"aspect-ratio"`: The ratio between the width and the height of the viewport
        `"color"`: The number of bits per color component for the output device
        `"color-gamut"`: The approximate range of colors that are supported by the user agent and output device (added in Media Queries Level 4)
        `"color-index"`: The number of colors the device can display
        `"grid"`: Whether the device is a grid or bitmap
        `"height"`: The viewport height
        `"hover"`: Does the primary input mechanism allow the user to hover over elements? (added in Media Queries Level 4)
        `"inverted-colors"`: Is the browser or underlying OS inverting colors? (added in Media Queries Level 4)
        `"light-level"`: Current ambient light level (added in Media Queries Level 4)
        `"max-aspect-ratio"`: The maximum ratio between the width and the height of the display area
        `"max-color"`: The maximum number of bits per color component for the output device
        `"max-color-index"`: The maximum number of colors the device can display
        `"max-height"`: The maximum height of the display area, such as a browser window
        `"max-monochrome"`: The maximum number of bits per "color" on a monochrome (greyscale) device
        `"max-resolution"`: The maximum resolution of the device, using dpi or dpcm
        `"max-width"`: The maximum width of the display area, such as a browser window
        `"min-aspect-ratio"`: The minimum ratio between the width and the height of the display area
        `"min-color"`: The minimum number of bits per color component for the output device
        `"min-color-index"`: The minimum number of colors the device can display
        `"min-height"`: The minimum height of the display area, such as a browser window
        `"min-monochrome"`: The minimum number of bits per "color" on a monochrome (greyscale) device
        `"min-resolution"`: The minimum resolution of the device, using dpi or dpcm
        `"min-width"`: The minimum width of the display area, such as a browser window
        `"monochrome"`: The number of bits per "color" on a monochrome (greyscale) device
        `"orientation"`: The orientation of the viewport (landscape or portrait mode)
        `"overflow-block"`: How does the output device handle content that overflows the viewport along the block axis (added in Media Queries Level 4)
        `"overflow-inline"`: Can content that overflows the viewport along the inline axis be scrolled (added in Media Queries Level 4)
        `"pointer"`: Is the primary input mechanism a pointing device, and if so, how accurate is it? (added in Media Queries Level 4)
        `"resolution"`: The resolution of the output device, using dpi or dpcm
        `"scan"`: The scanning process of the output device
        `"scripting"`: Is scripting (e.g. JavaScript) available? (added in Media Queries Level 4)
        `"update"`: How quickly can the output device modify the appearance of the content (added in Media Queries Level 4)
        `"width"`: The viewport width
        """
        return self._media_feature

    @mediaFeature.setter
    def mediaFeature(self, value):
        """
        mediafeature and|or|not mediafeature

        `"any-hover"`: Does any available input mechanism allow the user to hover over elements? (added in Media Queries Level 4)
        `"any-pointer"`: Is any available input mechanism a pointing device, and if so, how accurate is it? (added in Media Queries Level 4)
        `"aspect-ratio"`: The ratio between the width and the height of the viewport
        `"color"`: The number of bits per color component for the output device
        `"color-gamut"`: The approximate range of colors that are supported by the user agent and output device (added in Media Queries Level 4)
        `"color-index"`: The number of colors the device can display
        `"grid"`: Whether the device is a grid or bitmap
        `"height"`: The viewport height
        `"hover"`: Does the primary input mechanism allow the user to hover over elements? (added in Media Queries Level 4)
        `"inverted-colors"`: Is the browser or underlying OS inverting colors? (added in Media Queries Level 4)
        `"light-level"`: Current ambient light level (added in Media Queries Level 4)
        `"max-aspect-ratio"`: The maximum ratio between the width and the height of the display area
        `"max-color"`: The maximum number of bits per color component for the output device
        `"max-color-index"`: The maximum number of colors the device can display
        `"max-height"`: The maximum height of the display area, such as a browser window
        `"max-monochrome"`: The maximum number of bits per "color" on a monochrome (greyscale) device
        `"max-resolution"`: The maximum resolution of the device, using dpi or dpcm
        `"max-width"`: The maximum width of the display area, such as a browser window
        `"min-aspect-ratio"`: The minimum ratio between the width and the height of the display area
        `"min-color"`: The minimum number of bits per color component for the output device
        `"min-color-index"`: The minimum number of colors the device can display
        `"min-height"`: The minimum height of the display area, such as a browser window
        `"min-monochrome"`: The minimum number of bits per "color" on a monochrome (greyscale) device
        `"min-resolution"`: The minimum resolution of the device, using dpi or dpcm
        `"min-width"`: The minimum width of the display area, such as a browser window
        `"monochrome"`: The number of bits per "color" on a monochrome (greyscale) device
        `"orientation"`: The orientation of the viewport (landscape or portrait mode)
        `"overflow-block"`: How does the output device handle content that overflows the viewport along the block axis (added in Media Queries Level 4)
        `"overflow-inline"`: Can content that overflows the viewport along the inline axis be scrolled (added in Media Queries Level 4)
        `"pointer"`: Is the primary input mechanism a pointing device, and if so, how accurate is it? (added in Media Queries Level 4)
        `"resolution"`: The resolution of the output device, using dpi or dpcm
        `"scan"`: The scanning process of the output device
        `"scripting"`: Is scripting (e.g. JavaScript) available? (added in Media Queries Level 4)
        `"update"`: How quickly can the output device modify the appearance of the content (added in Media Queries Level 4)
        `"width"`: The viewport width
        """
        self._media_feature = value

    @mediaFeature.deleter
    def mediaFeature(self):
        self._media_feature = None


if __name__ == '__main__':
    _css = CSS('.console')

    _css.display = 'inline-block'
    _css.width = '100%'
    _css.height = '200px'
    _css.border = 'solid 1px #555573'
    _css.overflow = 'hidden'
    _css.margin_top = '30px'
    _css.box_sizing = 'border-box'

    _font_face = font_face()
    _font_face.fontFamily = 'Some Font'
    _font_face.fontStretch = 'semi-condensed'
    _css.fontFace = _font_face

    _print(css)

