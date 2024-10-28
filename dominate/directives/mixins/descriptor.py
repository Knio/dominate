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

    def descriptor_key(self):
        return '__' + self.descriptor_name
    
    def copied_self(self, instance, append_key=''):
        try:
            return instance.__dict__[self.descriptor_key() + append_key]
        except KeyError:
            copied_self = copy(self)
            copied_self.instance = instance
            instance.__dict__[self.descriptor_key() + append_key] = copied_self
            return copied_self

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return self.copied_self(instance)

    def __set__(self, instance, value):
        self.copied_self(instance).__call__(value)

    def __delete__(self, instance):
        self.copied_self(instance).delete()

    def get_dom_tag(self):
        from ...dom_tag import get_current, dom_tag
        
        if self.instance is None:
            return get_current()
        elif isinstance(self.instance, dom_tag):
            return self.instance
        else:
            return self.instance.get_dom_tag()
