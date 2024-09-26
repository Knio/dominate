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
