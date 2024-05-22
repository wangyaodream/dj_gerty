from django.urls import path

from . import views

app_name = "webapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("my-login/", views.my_login, name="my-login"),
    path("user-logout/", views.user_logout, name="user-logout"),
    # CRUD
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create-record", views.create_record, name="create-record"),
    path("update-record/<int:pk>", views.update_record, name="update-record"),
    path("record/<int:pk>", views.view_record, name="view-record")
]
