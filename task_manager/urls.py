from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import UserLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserLoginView.as_view(), name='login'),
    path('', TemplateView.as_view(template_name='index.html'), name='main'),
    path('users/', include('task_manager.apps.users.urls')),
]
