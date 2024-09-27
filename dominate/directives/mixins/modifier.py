

class BaseAttributeModifierMixin:

    separator = ":"
    modifier = None

    def __getitem__(self, key):
        self.modifier = key
        return self

    def __setitem__(self, key, value):
        self.modifier = key
        self.__call__(value)
        return self

    def full_directive(self):
        return super().full_directive() + f"{self.separator}{self.modifier}"
