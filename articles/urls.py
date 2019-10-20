from django.urls import path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name="create"),
    path('aboutme/', views.article_aboutme, name="aboutme"),
    re_path(r'(?P<slug>[\w-]+)/', views.article_detail, name="detail"),
]
