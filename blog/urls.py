from django.urls import URLPattern, path
from . import views


# name的作用主要体现在模板中直接使用这个名称引用这个url
urlpatterns = [
    path('', views.index, name="index"),
    path('articles/<int:article_id>/', views.article_detail, name="article_detail")
]
