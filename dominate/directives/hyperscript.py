from .base import BaseAttributeDirective, BaseDominated


class HyperscriptDirective(BaseAttributeDirective):
    pass


class HyperscriptDominated(BaseDominated):
    default_directive = 'script'

    script = HyperscriptDirective()
