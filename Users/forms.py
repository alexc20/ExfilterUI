from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from Users.permission_tests import is_admin
from django.forms import ValidationError


class UserRegisterForm(UserCreationForm):
    account_type = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "account_type",
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    account_type = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "account_type",
            "username",
            "first_name",
            "last_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        """Let's do adding that account type fields for admins like this"""
        if is_admin(self.user) and self.user != self.instance:
            group = self.instance.groups.first()
            if group:
                self.fields["account_type"].initial = group
        else:
            self.fields.pop("account_type")
