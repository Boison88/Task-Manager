from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import NewUserCreationForm, UpdateForm
from task_manager.mixins import UserAuthenticateMixin, CheckUserPermissionMixin


class UserListView(SuccessMessageMixin, ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users/main.html'

class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = NewUserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _("Registration successful")

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(request=self.request,
                       message=_(
                           "Unsuccessful registration. Invalid information."))
        return super().form_invalid(form)

class UserUpdateView(UserAuthenticateMixin, CheckUserPermissionMixin,
                     SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User information successfully updated')
    permission_denied_message = _('You have no rights to change another user.')
    permission_forwarded_url = 'users'


class UserDeleteView(UserAuthenticateMixin, CheckUserPermissionMixin,
                     SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_message = _('User is successfully deleted')
    success_url = reverse_lazy('users')
    permission_denied_message = _('You have no rights to change another user.')
    permission_forwarded_url = 'users'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
