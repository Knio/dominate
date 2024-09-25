import cssutils

from .base import BaseDirective
from .mixins import SpaceJoinerMixin


class KlassDirective(SpaceJoinerMixin, BaseDirective):
    pass


class StyleDirective(BaseDirective):

    encoding='utf-8'
    normalize = True

    @property
    def css(self):
        return cssutils.parseStyle(self.current_attr() or '', self.encoding)

    @css.setter
    def css(self, css):
        super().__call__(css.getCssText(' '))

    def reset_style(self, **properties):
        return self.make_style(False, **properties)

    def make_style(self, __include_current=True, __replace=True, __is_pythonic_key=True, **properties):
        css = self.css if __include_current else cssutils.css.CSSStyleDeclaration()

        for name, value in properties.items():
            value, priority = value if type(value) is tuple else (value, '')

            if __is_pythonic_key:
                name = name.replace('_', '-')

            css.setProperty(name, value, priority, self.normalize, __replace)
        
        return css.getCssText(' ')
    
    def reset(self, **properties):
        return super().__call__(
            self.reset_style(**properties)
        )

    def add(self, __replace=True, **properties):
        return super().__call__(
            self.make_style(True, __replace, **properties)
        )

    def add_extra(self, **properties):
        return self.add(False, **properties)

    def __add__(self, other):
        return self.make_style(True, True, **other)

    def __setitem__(self, key, value):
        return super().__call__(
            self.make_style(True, True, False, **{key: value})
        )

    def __set__(self, instance, value):
        if type(value) is dict:
            self.copied_self(instance).__call__(**value)
        elif type(value) is cssutils.css.CSSStyleDeclaration:
            super(StyleDirective, self.copied_self(instance)).__call__(value.getCssText(' '))
        else:
            super(StyleDirective, self.copied_self(instance)).__call__(value)

    def remove_properties(self, *properties):
        css = self.css

        for name in properties:
            css.removeProperty(name, self.normalize)
        
        return css.getCssText(' ')
    
    def remove(self, *properties):
        return super().__call__(self.remove_properties(*properties))

    def __delitem__(self, key):
        return self.remove(key)

    def __sub__(self, other):
        if type(other) is str:
            return self.remove_properties(other)
        else:
            return self.remove_properties(*other)

    def __call__(self, **properties):
        super().__call__(self.reset_style(**properties))
