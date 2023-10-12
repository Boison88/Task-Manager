from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .forms import StatusForm
from .models import Status
from task_manager.mixins import UserAuthenticateMixin


class StatusListView(ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/main.html'


class StatusCreateView(UserAuthenticateMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')


class StatusUpdateView(UserAuthenticateMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully updated')


class StatusDeleteView(UserAuthenticateMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_message = _('Status successfully deleted')
    success_url = reverse_lazy('statuses')
