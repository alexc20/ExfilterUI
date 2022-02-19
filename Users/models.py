from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def display_name(self):
    if self.get_full_name():
        return self.get_full_name()
    else:
        return self.username


User.add_to_class("__str__", display_name)
