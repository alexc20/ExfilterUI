from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from Users.forms import *
from Users.permission_tests import *

User = get_user_model()


#################################################################################################
#                                           USERS                                               #
#################################################################################################


class UserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """
    Displays users.
    """

    queryset = User.objects.filter(is_superuser=False)
    context_object_name = "user_to_update"
    template_name = "users/user_list.html"
    ordering = "first_name"
    paginate_by = 10

    def test_func(self):
        return is_admin(self.request.user)


class UserCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    Creates users.
    """

    model = User
    context_object_name = "user_to_update"
    template_name = "users/user_form.html"
    form_class = UserRegisterForm

    def test_func(self):
        return is_admin(self.request.user)

    def get_success_url(self):
        return reverse("user-list")

    def form_valid(self, form):
        success_url = super().form_valid(form)

        group = form.cleaned_data["account_type"]
        self.object.groups.add(group)

        return success_url


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Updates user.
    """

    model = User
    context_object_name = "user_to_update"
    template_name = "users/user_form.html"
    form_class = UserUpdateForm

    def get_initial(self):
        initial = super().get_initial()
        initial.update({"accessing_user": self.request.user})
        return initial

    def get_form_kwargs(self):
        form_kwargs = super().get_form_kwargs()
        form_kwargs["user"] = self.request.user
        return form_kwargs

    def test_func(self):
        if self.request.user.pk == self.kwargs.get("pk"):
            return True
        else:
            return is_admin(self.request.user)

    def get_success_url(self):
        if not is_admin(self.request.user):
            return reverse("router")
        else:
            return reverse("user-list")

    def form_valid(self, form):
        success_url = super().form_valid(form)
        group = form.cleaned_data.get("account_type")
        if group:
            self.object.groups.clear()
            self.object.groups.add(group)

        return success_url


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Deletes user.
    """

    model = User
    context_object_name = "user_to_update"
    template_name = "users/user_confirm_delete.html"

    def test_func(self):
        return is_admin(self.request.user)

    def get_success_url(self):
        return reverse("user-list")
