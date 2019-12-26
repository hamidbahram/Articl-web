from django.urls import path, re_path
from .views import SearchResultsView
from . import views

app_name = 'articles'

urlpatterns = [
    path(r'', views.article_list, name="list"),
    path(r'create/', views.article_create, name="create"),
    path(r'aboutme/', views.article_aboutme, name="aboutme"),
    path(r'search/', SearchResultsView.as_view(), name="search_results"),
    re_path(r'(?P<id>[0-9]{1,3})/', views.article_detail, name="detail"),
    re_path(r'edit/(?P<id>[0-9]{1,3})', views.edit, name='edit'),
    re_path(r'delete/(?P<id>[0-9]{1,3})', views.delete, name='delete'),
    # re_path(r'(?P<slug>[\w-]+)/', views.article_detail, name="detail"),
    # re_path(r'delete(?P<slug>[\w-]+)', views.delete, name="delete"),
]