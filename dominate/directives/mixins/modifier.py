

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
