

class BaseAttributeModifierMixin:

    separator = ":"
    modifier = None

    def __getitem__(self, key):
        self = self.copied_self(self.instance, f"{self.separator}{key}")
        self.modifier = key
        return self

    def __setitem__(self, key, value):
        self = self[key]
        self.__call__(value)
        return self

    def __delitem__(self, key):
        return self[key].delete()

    def full_directive(self):
        return super().full_directive() + f"{self.separator}{self.modifier}"

    def keys(self):
        if self.modifier is None:
            prefix = super().full_directive() + self.separator
            return [
                k[len(prefix):]
                for k in self.get_dom_tag().attributes
                if k.startswith(prefix)
            ]

