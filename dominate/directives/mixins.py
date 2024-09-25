

class JoinerMixin:

    SPLIT_DELIMETER = NotImplemented
    JOIN_DELIMETER = NotImplemented
    STRIP_AFTER_SPLIT = True

    def split_items(self):

        def strip(obj):
            if self.STRIP_AFTER_SPLIT is True:
                return obj.strip()
            elif self.STRIP_AFTER_SPLIT is False:
                return obj
            else:
                return obj.strip(self.STRIP_AFTER_SPLIT)

        return [
            strip(c)
            for c in (self.current_attr() or '').split(self.SPLIT_DELIMETER)
            if strip(c) != ''
        ]
    
    def join_items(self, *items, include_current=True):
        return self.JOIN_DELIMETER.join(
                self.split_items() + list(items) if include_current else list(items)
            )

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


class SpaceJoinerMixin(JoinerMixin):

    JOIN_DELIMETER = SPLIT_DELIMETER = ' '


class CommaJoinerMixin(JoinerMixin):

    SPLIT_DELIMETER = ','
    JOIN_DELIMETER = SPLIT_DELIMETER + ' '
