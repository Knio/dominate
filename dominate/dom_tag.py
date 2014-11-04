__license__ = '''
This file is part of Dominate.

Dominate is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.

Dominate is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General
Public License along with Dominate.  If not, see
<http://www.gnu.org/licenses/>.
'''

# pylint: disable=bad-indentation, bad-whitespace, missing-docstring

import copy
import numbers
from collections import defaultdict, namedtuple, Callable
from functools import wraps
import threading

try:
  basestring = basestring
except NameError: # py3
  basestring = str
  unicode = str


try:
  import greenlet
except ImportError:
  greenlet = None

def _get_thread_context():
  context = [threading.current_thread()]
  if greenlet:
    context.append(greenlet.getcurrent())
  return hash(tuple(context))


class dom_tag(object):
  TAB = '  '  # TODO make this a parameter to render(), and a tag.

  is_single = False  # Tag does not require matching end tag (ex. <hr/>)
  is_pretty = True   # Text inside the tag should be left as-is (ex. <pre>)
                     # otherwise, text will be escaped() and whitespace may be
                     # modified

  frame = namedtuple('frame', ['tag', 'items', 'used'])

  def __new__(_cls, *args, **kwargs):
    '''
    Check if bare tag is being used a a decorator.
    decorate the function and return
    '''
    if len(args) == 1 and isinstance(args[0], Callable) \
        and not isinstance(args[0], dom_tag) and not kwargs:
      wrapped = args[0]

      @wraps(wrapped)
      def f(*args, **kwargs):
        with _cls() as _tag:
          return wrapped(*args, **kwargs) or _tag
      return f
    return object.__new__(_cls)

  def __init__(self, *args, **kwargs):
    '''
    Creates a new tag. Child tags should be passed as aruguments and attributes
    should be passed as keyword arguments.

    There is a non-rendering attribute which controls how the tag renders:

    * `__inline` - Boolean value. If True renders all children tags on the same
                   line.
    '''

    self.attributes = {}
    self.children   = []
    self.parent     = None
    self.document   = None

    # Does not insert newlines on all children if True (recursive attribute)
    self.do_inline = kwargs.pop('__inline', False)

    #Add child elements
    if args:
      self.add(*args)

    for attr, value in kwargs.items():
      self.set_attribute(*dom_tag.clean_pair(attr, value))

    self._ctx = None
    self._add_to_ctx()

  def _add_to_ctx(self):
    ctx = dom_tag._with_contexts[_get_thread_context()]
    if ctx and ctx[-1]:
      self._ctx = ctx[-1]
      ctx[-1].items.append(self)

  # stack of (root_tag, [new_tags], set(used_tags))
  _with_contexts = defaultdict(list)

  def __enter__(self):
    ctx = dom_tag._with_contexts[_get_thread_context()]
    ctx.append(dom_tag.frame(self, [], set()))
    return self

  def __exit__(self, type, value, traceback):
    ctx = dom_tag._with_contexts[_get_thread_context()]
    slf, items, used = ctx[-1]
    ctx[-1] = None
    for item in items:
      if item in used: continue
      self.add(item)
    ctx.pop()

  def __call__(self, func):
    '''
    tag instance is being used as a decorator.
    wrap func to make a copy of this tag
    '''
    # remove decorator from its context so it doesn't
    # get added in where it was defined
    if self._ctx:
      assert False, self._ctx
      self._ctx.used.add(self)

    @wraps(func)
    def f(*args, **kwargs):
      tag = copy.deepcopy(self)
      tag._add_to_ctx()
      with tag:
        return func(*args, **kwargs) or tag
    return f

  def set_attribute(self, key, value):
    '''
    Add or update the value of an attribute.
    '''
    if isinstance(key, int):
      self.children[key] = value
    elif isinstance(key, basestring):
      self.attributes[key] = value
    else:
      raise TypeError('Only integer and string types are valid for assigning '
          'child tags and attributes, respectively.')
  __setitem__ = set_attribute

  def delete_attribute(self, key):
    if isinstance(key, int):
      del self.children[key:key+1]
    else:
      del self.attributes[key]
  __delitem__ = delete_attribute

  def setdocument(self, doc):
    '''
    Creates a reference to the parent document to allow for partial-tree
    validation.
    '''
    # assume that a document is correct in the subtree
    if self.document != doc:
      self.document = doc
      for i in self.children:
        if not isinstance(i, dom_tag): return
        i.setdocument(doc)

  def add(self, *args):
    '''
    Add new child tags.
    '''
    for obj in args:
      if isinstance(obj, numbers.Number):
        # Convert to string so we fall into next if block
        obj = str(obj)

      if isinstance(obj, basestring):
        obj = escape(obj)
        self.children.append(obj)

      elif isinstance(obj, dom_tag):
        ctx = dom_tag._with_contexts[_get_thread_context()]
        if ctx and ctx[-1]:
          ctx[-1].used.add(obj)
        self.children.append(obj)
        obj.parent = self
        obj.setdocument(self.document)

      elif isinstance(obj, dict):
        for attr, value in obj.items():
          self.set_attribute(*dom_tag.clean_pair(attr, value))

      elif hasattr(obj, '__iter__'):
        for subobj in obj:
          self.add(subobj)

      else:  # wtf is it?
        raise ValueError('%r not a tag or string.' % obj)

    if len(args) == 1:
      return args[0]

    return args

  def add_raw_string(self, s):
    self.children.append(s)

  def remove(self, obj):
    self.children.remove(obj)

  def clear(self):
    for i in self.children:
      if isinstance(i, dom_tag) and i.parent is self:
        i.parent = None
    self.children = []

  def get(self, tag=None, **kwargs):
    '''
    Recursively searches children for tags of a certain
    type with matching attributes.
    '''
    # Stupid workaround since we can not use dom_tag in the method declaration
    if tag is None: tag = dom_tag

    attrs = [(dom_tag.clean_attribute(attr), value)
        for attr, value in kwargs.items()]

    results = []
    for child in self.children:
      if (isinstance(tag, basestring) and type(child).__name__ == tag) or \
        (not isinstance(tag, basestring) and isinstance(child, tag)):

        if all(child.attributes.get(attribute) == value
            for attribute, value in attrs):
          # If the child is of correct type and has all attributes and values
          # in kwargs add as a result
          results.append(child)
      if isinstance(child, dom_tag):
        # If the child is a dom_tag extend the search down through its children
        results.extend(child.get(tag, **kwargs))
    return results

  def __getitem__(self, key):
    '''
    Returns the stored value of the specified attribute or child
    (if it exists).
    '''
    if isinstance(key, int):
      # Children are accessed using integers
      try:
        return object.__getattribute__(self, 'children')[key]
      except KeyError:
        raise IndexError('Child with index "%s" does not exist.' % key)
    elif isinstance(key, basestring):
      # Attributes are accessed using strings
      try:
        return object.__getattribute__(self, 'attributes')[key]
      except KeyError:
        raise AttributeError('Attribute "%s" does not exist.' % key)
    else:
      raise TypeError('Only integer and string types are valid for accessing '
          'child tags and attributes, respectively.')
  __getattr__ = __getitem__

  def __len__(self):
    '''
    Number of child elements.
    '''
    return len(self.children)

  def __bool__(self):
    '''
    Hack for "if x" and __len__
    '''
    return True
  __nonzero__ = __bool__

  def __iter__(self):
    '''
    Iterates over child elements.
    '''
    return self.children.__iter__()

  def __contains__(self, item):
    '''
    Checks recursively if item is in children tree.
    Accepts both a string and a class.
    '''
    return bool(self.get(item))

  def __iadd__(self, obj):
    '''
    Reflexive binary addition simply adds tag as a child.
    '''
    self.add(obj)
    return self

  def render(self, indent=1, inline=False):
    data = self._render([], indent, inline)
    return u''.join(data)

  def _render(self, rendered, indent=1, inline=False):
    '''
    Returns a well-formatted string representation of the tag and renderings
    of all its child tags.
    '''
    inline = self.do_inline or inline

    t = type(self)
    name = getattr(t, 'tagname', t.__name__)

    # Workaround for python keywords and standard classes/methods
    # (del, object, input)
    if name[-1] == '_':
      name = name[:-1]

    rendered.extend(['<', name])

    for attribute, value in sorted(self.attributes.items()):
      rendered.append(' %s="%s"' % (attribute, escape(unicode(value), True)))

    rendered.append('>')

    if not self.is_single:
      pretty = self._render_children(rendered, indent, inline)

      # don't add trailing whitespace after whitespace-sensitive elements
      if pretty:
        rendered.append('\n')
        rendered.append(dom_tag.TAB * (indent - 1))

      # close tag
      rendered.append('</')
      rendered.append(name)
      rendered.append('>')

    return rendered

  # String and unicode representations are the same as render()
  def __unicode__(self):
    return self.render()
  __str__ = __unicode__

  def _render_children(self, rendered, indent=1, inline=False):
    pretty = False
    for child in self.children:
      pretty = False
      if isinstance(child, dom_tag):
        if not inline and self.is_pretty and child.is_pretty:
          pretty = True
          rendered.append('\n')
          rendered.append(dom_tag.TAB * indent)
        child._render(rendered, indent + 1, inline)
      else:
        rendered.append(unicode(child))

    return pretty

  def __repr__(self):
    name = '%s.%s' % (self.__module__, type(self).__name__)

    attributes_len = len(self.attributes)
    attributes = '%s attribute' % attributes_len
    if attributes_len != 1: attributes += 's'

    children_len = len(self.children)
    children = '%s child' % children_len
    if children_len != 1: children += 'ren'

    return '<%s at %x: %s, %s>' % (name, id(self), attributes, children)

  @staticmethod
  def clean_attribute(attribute):
    '''
    Since some attributes match python keywords we prepend them with
    underscores. Python also does not support colons in keywords so underscores
    mid-attribute are replaced with colons.
    '''
    # shorthand
    attribute = {
      'cls': 'class',
      'className': 'class',
      'class_name': 'class',
      'fr': 'for',
      'html_for': 'for',
      'htmlFor': 'for',
    }.get(attribute, attribute)

    # Workaround for python's reserved words
    if attribute[0] == '_': attribute = attribute[1:]

    # Workaround for inability to use colon in python keywords
    if attribute in set(['http_equiv']) or attribute.startswith('data_'):
      return attribute.replace('_', '-').lower()
    return attribute.replace('_', ':').lower()

  @classmethod
  def clean_pair(cls, attribute, value):
    '''
    This will call `clean_attribute` on the attribute and also allows for the
    creation of boolean attributes.

    Ex. input(selected=True) is equivalent to input(selected="selected")
    '''
    attribute = cls.clean_attribute(attribute)

    # Check for boolean attributes
    # (i.e. selected=True becomes selected="selected")
    if value is True:
      value = attribute

    if value is False:
      value = "false"

    return (attribute, value)


def attr(*args, **kwargs):
  '''
  Set attributes on the current active tag context
  '''
  ctx = dom_tag._with_contexts[_get_thread_context()]
  if ctx and ctx[-1]:
    dicts = args + (kwargs,)
    for d in dicts:
      for attr, value in d.items():
        ctx[-1].tag.set_attribute(*dom_tag.clean_pair(attr, value))
  else:
    raise ValueError('not in a tag context')


# escape() is used in render
from .util import escape
