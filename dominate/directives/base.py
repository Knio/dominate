from copy import copy


class DescriptorMixin:
    instance = None

    descriptor_name = None
    fixed_name = None

    fix_endswith_underscore = True
    fix_hyphen = True

    def __set_name__(self, owner, name):
        self.descriptor_name = name

        fixed_name = name

        if self.fix_endswith_underscore and fixed_name.endswith('_'):
            fixed_name = fixed_name[0:-1]
        
        if self.fix_hyphen:
            fixed_name = fixed_name.replace('_', '-')

        self.fixed_name = fixed_name

    def copied_self(self, instance):
        
        try:
            return instance.__dict__['__' + self.descriptor_name]
        except KeyError:
            copied_self = copy(self)
            copied_self.instance = instance
            instance.__dict__['__' + self.descriptor_name] = copied_self
            return copied_self

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.copied_self(instance)

    def __set__(self, instance, value):
        self.copied_self(instance).__call__(value)


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


class BaseModifierMixin:

    separator = ":"
    modifier = None

    def __getitem__(self, key):
        self.modifier = key
        return self

    def __setitem__(self, key, value):
        self.modifier = key
        self.__call__(value)
        return self

    def make_attr(self, value):
        attr = super().make_attr(value)
        
        if self.modifier:
            attr = {
                f"{key}{self.separator}{self.modifier}": value
                for key, value in attr.items()
            }
        
        return attr
