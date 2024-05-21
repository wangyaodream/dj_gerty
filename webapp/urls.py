from django.urls import path

from . import views

app_name = "webapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("my-login/", views.my_login, name="my-login"),
    path("user-logout/", views.user_logout, name="user-logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
