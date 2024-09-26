from .base import BaseDirective, BaseDominated, DescriptorMixin
from .mixins.delemeted_string import CommaDelemetedStringListMixin, DelemetedStringDirectiveMixin, DelemetedSubstringDescriptorMixin, SpaceDelemetedStringListMixin
from .mixins.modifier import BaseModifierMixin


class HtmxDirective(BaseDirective):
    prefix = 'hx-'
    

class HtmxModifier(BaseModifierMixin, HtmxDirective):
    pass


class HtmxSpaceListDirective(SpaceDelemetedStringListMixin, HtmxDirective):
    pass


class HtmxCommaListDirective(CommaDelemetedStringListMixin, HtmxDirective):
    pass


class HtmxColonDelemetedStringDirective(DelemetedStringDirectiveMixin, HtmxDirective):
    JOIN_DELIMETER = SPLIT_DELIMETER = ':'


class HtmxSubstring(DelemetedSubstringDescriptorMixin, DescriptorMixin):
    pass


class HtmxCommaListSubstring(CommaDelemetedStringListMixin, HtmxSubstring):
    pass


class HtmxSyncDirective(HtmxColonDelemetedStringDirective):
    selectors = HtmxCommaListSubstring()
    strategy = HtmxSubstring()


class HtmxDominated(BaseDominated):
    default_directive = 'on'

    get = HtmxDirective()
    post = HtmxDirective()
    on = HtmxModifier()
    push_url = HtmxDirective()
    select = HtmxCommaListDirective()
    select_oob = HtmxCommaListDirective()
    swap = HtmxSpaceListDirective()
    swap_oob = HtmxDirective()
    target = HtmxDirective()
    trigger = HtmxCommaListDirective()
    vals = HtmxDirective()

    boost = HtmxDirective()
    confirm = HtmxDirective()
    delete = HtmxDirective()
    disable = HtmxDirective()
    disabled_elt = HtmxCommaListDirective()
    disinherit = HtmxSpaceListDirective()
    encoding = HtmxDirective()
    ext = HtmxCommaListDirective()
    headers = HtmxDirective()
    history = HtmxDirective()
    history_elt = HtmxDirective()
    include = HtmxCommaListDirective()
    indicator = HtmxCommaListDirective()
    inherit = HtmxSpaceListDirective()
    params = HtmxCommaListDirective()
    patch = HtmxDirective()
    preserve = HtmxDirective()
    prompt = HtmxDirective()
    put = HtmxDirective()
    replace_url = HtmxDirective()
    request = HtmxDirective()
    sync = HtmxSyncDirective()
    validate = HtmxDirective()
    vars = HtmxDirective()
