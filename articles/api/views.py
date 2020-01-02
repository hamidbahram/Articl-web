from articles.models import Article
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView 
from articles.api.serializers import (
    PostListSerializer, 
    PostDetailSerializer, 
    PostDeleteSerializer,
)

class PostListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = PostListSerializer

class PostDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'slug'