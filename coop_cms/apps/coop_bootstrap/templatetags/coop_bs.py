from django import template

from coop_cms.templatetags.coop_utils import is_checkbox as _is_checkbox
from coop_cms.templatetags.coop_navigation import NavigationAsNestedUlNode

register = template.Library()

#Just for compatibility

@register.filter(name='is_checkbox')
def is_checkbox(field):
  return _is_checkbox(field)

@register.tag
def navigation_bootstrap(parser, token):
    return NavigationAsNestedUlNode(li_node="coop_bootstrap/li_node.html")