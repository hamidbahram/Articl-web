from django.urls import path, re_path
from articles.api import views

app_name = 'api'

urlpatterns = [
    path(r'', views.PostListAPIView.as_view(), name="post-list"),
    path(r'create', views.PostCreateAPIView.as_view(), name="post-create"),
    re_path(r'detail/(?P<slug>[\w-]+)$', views.PostDetailAPIView.as_view(), name="detail-post"), 
    re_path(r'(?P<slug>[\w-]+)/delete', views.PostDeleteAPIView.as_view(), name="delete-post"),
    re_path(r'(?P<slug>[\w-]+)/edit', views.PostUpdateAPIView.as_view(), name="edit-post"),
    re_path(r'(?P<slug>[\w-]+)/manage', views.PostDeleteUpdateAPIView.as_view(), name="manage-post"),
]
