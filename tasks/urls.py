from django.urls import path
from . import views

# namespace
app_name = 'tasks'

urlpatterns = [
    # create task
    path('create/', views.task_create, name='task_create'),
    # Retrieve task list
    path('', views.task_list, name='task_list'),
    # Retrieve single task object
    path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    # Update a task
    path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),
    # Delete a task
    path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),
]
