from .base import BaseAttributeDirective, BaseDelemetedSubstringDirective, BaseDominated
from .mixins.delemeted_string import CommaDelemetedStringListMixin, DelemetedStringDirectiveMixin, SpaceDelemetedStringListMixin
from .mixins.modifier import BaseAttributeModifierMixin


class HtmxAttributeDirective(BaseAttributeDirective):
    prefix = 'hx-'
    

class HtmxAttributeModifier(BaseAttributeModifierMixin, HtmxAttributeDirective):
    pass


class HtmxSpaceListAttributeDirective(SpaceDelemetedStringListMixin, HtmxAttributeDirective):
    pass


class HtmxCommaListAttributeDirective(CommaDelemetedStringListMixin, HtmxAttributeDirective):
    pass


class HtmxColonAttributeDirective(DelemetedStringDirectiveMixin, HtmxAttributeDirective):
    JOIN_DELIMETER = SPLIT_DELIMETER = ':'


class HtmxSubstring(BaseDelemetedSubstringDirective):
    pass


class HtmxCommaListSubstring(CommaDelemetedStringListMixin, HtmxSubstring):
    pass


class HtmxSyncDirective(HtmxColonAttributeDirective):
    selectors = HtmxCommaListSubstring()
    strategy = HtmxSubstring()


class HtmxDominated(BaseDominated):
    default_directive = 'on'

    get = HtmxAttributeDirective()
    post = HtmxAttributeDirective()
    on = HtmxAttributeModifier()
    push_url = HtmxAttributeDirective()
    select = HtmxCommaListAttributeDirective()
    select_oob = HtmxCommaListAttributeDirective()
    swap = HtmxSpaceListAttributeDirective()
    swap_oob = HtmxAttributeDirective()
    target = HtmxAttributeDirective()
    trigger = HtmxCommaListAttributeDirective()
    vals = HtmxAttributeDirective()

    boost = HtmxAttributeDirective()
    confirm = HtmxAttributeDirective()
    delete = HtmxAttributeDirective()
    disable = HtmxAttributeDirective()
    disabled_elt = HtmxCommaListAttributeDirective()
    disinherit = HtmxSpaceListAttributeDirective()
    encoding = HtmxAttributeDirective()
    ext = HtmxCommaListAttributeDirective()
    headers = HtmxAttributeDirective()
    history = HtmxAttributeDirective()
    history_elt = HtmxAttributeDirective()
    include = HtmxCommaListAttributeDirective()
    indicator = HtmxCommaListAttributeDirective()
    inherit = HtmxSpaceListAttributeDirective()
    params = HtmxCommaListAttributeDirective()
    patch = HtmxAttributeDirective()
    preserve = HtmxAttributeDirective()
    prompt = HtmxAttributeDirective()
    put = HtmxAttributeDirective()
    replace_url = HtmxAttributeDirective()
    request = HtmxAttributeDirective()
    sync = HtmxSyncDirective()
    validate = HtmxAttributeDirective()
    vars = HtmxAttributeDirective()
