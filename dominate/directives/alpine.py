from .base import BaseDirective, BaseDominated
from .mixins.modifier import BaseModifierMixin


class AlpineDirective(BaseDirective):
    prefix = 'x-'
    

class AlpineModifier(BaseModifierMixin, AlpineDirective):
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
