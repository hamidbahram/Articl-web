from articles.models import Article
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from articles.api.serializers import (
    PostListSerializer, 
    PostDetailSerializer, 
    PostDeleteSerializer,
    PostUpdateSerializer,
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

class PostUpdateAPIView(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'