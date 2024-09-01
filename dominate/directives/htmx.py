from .base import BaseDirective, BaseDominated, BaseModifierMixin


class HtmxDirective(BaseDirective):
    prefix = 'hx-'
    

class HtmxModifier(BaseModifierMixin, HtmxDirective):
    pass


class HtmxDominated(BaseDominated):
    default_directive = 'on'

    get = HtmxDirective()
    post = HtmxDirective()
    on = HtmxModifier()
    push_url = HtmxDirective()
    select = HtmxDirective()
    select_oob = HtmxDirective()
    swap = HtmxDirective()
    swap_oob = HtmxDirective()
    target = HtmxDirective()
    trigger = HtmxDirective()
    vals = HtmxDirective()

    boost = HtmxDirective()
    confirm = HtmxDirective()
    delete = HtmxDirective()
    disable = HtmxDirective()
    disabled_elt = HtmxDirective()
    disinherit = HtmxDirective()
    encoding = HtmxDirective()
    ext = HtmxDirective()
    headers = HtmxDirective()
    history = HtmxDirective()
    history_elt = HtmxDirective()
    include = HtmxDirective()
    indicator = HtmxDirective()
    inherit = HtmxDirective()
    params = HtmxDirective()
    patch = HtmxDirective()
    preserve = HtmxDirective()
    prompt = HtmxDirective()
    put = HtmxDirective()
    replace_url = HtmxDirective()
    request = HtmxDirective()
    sync = HtmxDirective()
    validate = HtmxDirective()
    vars = HtmxDirective()
