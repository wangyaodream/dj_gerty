from django.contrib import admin
from django.urls import path, include

from webapp import views

urlpatterns = [
    path("", views.home),
    path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    path('webapp/', include('webapp.urls')),
    path('todo/', include('todo.urls')),
]
