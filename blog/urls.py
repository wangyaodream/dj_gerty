from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('articles/<int:article_id>/', views.article_detail, name="article_detail")
]
