from .base import BaseDirective, BaseDominated, BaseModifierMixin
from .mixins import CommaJoinerMixin, SpaceJoinerMixin


class HtmxDirective(BaseDirective):
    prefix = 'hx-'
    

class HtmxModifier(BaseModifierMixin, HtmxDirective):
    pass


class HtmxSpaceDirective(SpaceJoinerMixin, HtmxDirective):
    pass


class HtmxCommaDirective(CommaJoinerMixin, HtmxDirective):
    pass


class HtmxDominated(BaseDominated):
    default_directive = 'on'

    get = HtmxDirective()
    post = HtmxDirective()
    on = HtmxModifier()
    push_url = HtmxDirective()
    select = HtmxCommaDirective()
    select_oob = HtmxCommaDirective()
    swap = HtmxSpaceDirective()
    swap_oob = HtmxDirective()
    target = HtmxDirective()
    trigger = HtmxCommaDirective()
    vals = HtmxDirective()

    boost = HtmxDirective()
    confirm = HtmxDirective()
    delete = HtmxDirective()
    disable = HtmxDirective()
    disabled_elt = HtmxCommaDirective()
    disinherit = HtmxSpaceDirective()
    encoding = HtmxDirective()
    ext = HtmxCommaDirective()
    headers = HtmxDirective()
    history = HtmxDirective()
    history_elt = HtmxDirective()
    include = HtmxCommaDirective()
    indicator = HtmxCommaDirective()
    inherit = HtmxSpaceDirective()
    params = HtmxCommaDirective()
    patch = HtmxDirective()
    preserve = HtmxDirective()
    prompt = HtmxDirective()
    put = HtmxDirective()
    replace_url = HtmxDirective()
    request = HtmxDirective()
    sync = HtmxCommaDirective()
    validate = HtmxDirective()
    vars = HtmxDirective()
