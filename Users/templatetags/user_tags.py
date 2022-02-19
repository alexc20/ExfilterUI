from django import template

from ..permission_tests import is_admin, is_manager

register = template.Library()


@register.simple_tag
def check_group(user, target):
    if isinstance(user, str):
        return False
    if target == "Admin":
        return is_admin(user)
    elif target == "Manager":
        return is_manager(user)
    else:
        return False
