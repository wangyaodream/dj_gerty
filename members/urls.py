from django.urls import path
from . import views


app_name = "members"

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/list', views.get_list, name='list'),
    path('', views.index, name='index')
]