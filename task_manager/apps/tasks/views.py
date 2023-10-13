from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django_filters.views import FilterView
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from .filters import TaskFilter
from .forms import TaskForm
from .models import Task
from task_manager.mixins import UserAuthenticateMixin, CheckTaskAuthorPermissionMixin


class TaskFilterListView(UserAuthenticateMixin, FilterView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/main.html'
    filterset_class = TaskFilter


class TaskDetailView(UserAuthenticateMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(UserAuthenticateMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = get_user_model().objects.get(pk=user.pk)
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(UserAuthenticateMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully updated')


class TaskDeleteView(UserAuthenticateMixin, SuccessMessageMixin,
                     CheckTaskAuthorPermissionMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_message = _('Task successfully deleted')
    success_url = reverse_lazy('tasks')
    permission_denied_message = _('A task can only be deleted by its author.')
    permission_forwarded_url = reverse_lazy('tasks')
