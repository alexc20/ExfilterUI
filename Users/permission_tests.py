from django.db.models import Q


def is_admin(user):
    if user.groups.filter(name="Admin").exists():
        return True
    else:
        return False


def is_manager(user):
    if user.groups.filter(Q(name="Admin") | Q(name="Manager")).exists():
        return True
    else:
        return False