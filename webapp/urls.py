from django.urls import path

from . import views

app_name = "webapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("my-login/", views.my_login, name="my-login"),
]
