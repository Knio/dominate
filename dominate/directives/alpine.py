from .base import BaseAttributeDirective, BaseDominated
from .mixins.modifier import BaseAttributeModifierMixin


class AlpineDirective(BaseAttributeDirective):
    prefix = 'x-'
    

class AlpineModifier(BaseAttributeModifierMixin, AlpineDirective):
    pass


class AlpineDominated(BaseDominated):
    default_directive = 'bind'

    data = AlpineDirective()
    init = AlpineDirective()
    show = AlpineDirective()
    bind = AlpineModifier()
    on = AlpineModifier()
    text = AlpineDirective()
    html = AlpineDirective()
    model = AlpineDirective()
    modelable = AlpineDirective()
    for_ = AlpineDirective()
    transition = AlpineDirective()
    effect = AlpineDirective()
    ignore = AlpineDirective()
    ref = AlpineDirective()
    cloak = AlpineDirective()
    teleport = AlpineDirective()
    if_ = AlpineDirective()
    id = AlpineDirective()
