
from .. import tags

class HtmxTag:
  @classmethod
  def clean_attribute(cls, attribute):
    attribute = super().clean_attribute(attribute)
    if attribute.startswith('hx_'):
      attribute = attribute.replace('_', '-')
    return attribute

tags.html_tag.__bases__ = (HtmxTag,) + tags.html_tag.__bases__
