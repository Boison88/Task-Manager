from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .forms import UserCreationForm


class UserListView(SuccessMessageMixin, ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users/main.html'

class UserCreateView(SuccessMessageMixin, CreateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _("Registration successful")

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = UserCreationForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User information successfully updated')

    def form_valid(self, form):
        messages.success(request=self.request,
                         message=self.success_message)
        return super(UserCreationForm, self).form_valid(form)


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'users/delete.html'
    success_message = _('User is successfully deleted')
    success_url = reverse_lazy('users')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
