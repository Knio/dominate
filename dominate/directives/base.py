from .mixins.descriptor import DescriptorMixin


class BaseDominated(DescriptorMixin):

    default_directive = None

    def __getitem__(self, key):
        if self.default_directive:
            return getattr(self, self.default_directive)[key]
        else:
            raise NotImplementedError(f"`{self.__class__.__name__}` does not support a default directive.")

    def __setitem__(self, key, value):
        if self.default_directive:
            return getattr(self, self.default_directive)[key](value)
        else:
            raise NotImplementedError(f"`{self.__class__.__name__}` does not support a default directive.")

    def __call__(self, value):
        if self.default_directive:
            return getattr(self, self.default_directive)(value)
        else:
            raise NotImplementedError(f"`{self.__class__.__name__}` does not support a default directive.")


class BaseDirective(DescriptorMixin):
    
    def prepend(self, string):
        return self.__call__(
            self.__radd__(string)
        )

    def append(self, string):
        return self.__call__(
            self.__add__(string)
        )

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    def __str__(self):
        return self.current_attr() or ''


    prefix = ''
    
    @property
    def directive(self):
        return self.fixed_name

    def full_directive(self):
        return f"{self.prefix}{self.directive}"

    def make_attr(self, value):
        return {
            self.full_directive(): value
        }

    def current_attr(self):
        from ..dom_tag import get_current, dom_tag
        return (self.instance if isinstance(self.instance, dom_tag) else get_current()).attributes.get(self.full_directive(), None)

    def __call__(self, value):
        from ..dom_tag import get_current
        attributes = self.make_attr(value)
        dom_tag_obj = (self.instance.instance if isinstance(self.instance, BaseDominated) else self.instance) or get_current()
        for a, v in attributes.items():
            dom_tag_obj.set_attribute(a, v, clean_pair=True)
        return self.instance
