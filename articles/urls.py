from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.article_list),
    re_path(r'(?P<slug>[\w-]+)/', views.article_detail),
]
