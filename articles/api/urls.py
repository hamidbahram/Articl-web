from django.urls import path
from articles.api import views

app_name = 'api'

urlpatterns = [
    path(r'', views.PostListAPIView.as_view(), name="post-list"),
    
]
