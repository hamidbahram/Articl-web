from django.urls import path, re_path
from articles.api import views

app_name = 'api'

urlpatterns = [
    path(r'', views.PostListAPIView.as_view(), name="post-list"),
    re_path(r'detail/(?P<slug>[\w-]+)$', views.PostDetailAPIView.as_view(), name="detail-post"), 
    re_path(r'(?P<slug>[\w-]+)/delete', views.PostDeleteAPIView.as_view(), name="delete-post"),
]
