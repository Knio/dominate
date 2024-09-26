import inspect
from .descriptor import DescriptorMixin


def strip(obj, characters):
    if characters is True:
        return obj.strip()
    elif characters is False:
        return obj
    else:
        return obj.strip(characters)


class DelemetedStringMixin:

    SPLIT_DELIMETER = NotImplemented
    JOIN_DELIMETER = NotImplemented
    STRIP_AFTER_SPLIT = True
    STRIP_AFTER_JOIN = True

    def split_items(self):
        return [
            strip(c, self.STRIP_AFTER_SPLIT)
            for c in (self.current_attr() or '').split(self.SPLIT_DELIMETER)
            if strip(c, self.STRIP_AFTER_SPLIT) != ''
        ]
    
    def join_items(self, *items, include_current=True):
        return self.JOIN_DELIMETER.join([
            strip(c, self.STRIP_AFTER_JOIN)
            for c in (self.split_items() + list(items) if include_current else list(items))
            if strip(c, self.STRIP_AFTER_JOIN) != ''
        ])


class DelemetedStringListMixin(DelemetedStringMixin):

    def add(self, *items):
        return self.__call__(
            self.join_items(*items)
        )

    def __add__(self, other):
        if type(other) is str:
            return self.join_items(other)
        else:
            return self.join_items(*other)

    def remove_items(self, *items):
        return self.join_items(*[c for c in self.split_items() if c not in items], include_current=False)

    def remove(self, *items):
        return self.__call__(
            self.remove_items(*items)
        )

    def replace(self, old, new):
        self.remove(old)
        return self.add(new)

    def exists(self, item):
        return item in self.split_items()

    def __sub__(self, other):
        if type(other) is str:
            return self.remove_items(other)
        else:
            return self.remove_items(*other)


class SpaceDelemetedStringListMixin(DelemetedStringListMixin):

    JOIN_DELIMETER = SPLIT_DELIMETER = ' '


class CommaDelemetedStringListMixin(DelemetedStringListMixin):

    SPLIT_DELIMETER = ','
    JOIN_DELIMETER = SPLIT_DELIMETER + ' '


class DelemetedStringDirectiveMixin(DelemetedStringMixin):
    
    def __getitem__(self, key):
        items = self.split_items()
        try:
            return items[key]
        except IndexError:
            return None

    def __setitem__(self, key, value):
        items = self.split_items()
        items += [''] * max(0, (key + 1) - len(items))
        items[key] = value
        self.__call__(self.join_items(*items, include_current=False))
        return self


class DelemetedSubstringDescriptorMixin(DescriptorMixin):

    def current_attr(self):
        return self.instance[self.directive_position()]
    
    def directive_position(self):
        return [
            key
            for key, obj in inspect.getmembers(
                type(self.instance),
                lambda o: issubclass(type(o), DelemetedSubstringDescriptorMixin)
            )
        ].index(self.descriptor_name)

    def __call__(self, value):
        self.instance[self.directive_position()] = value
        return self.instance
