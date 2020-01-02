from articles.models import Article
from rest_framework import generics 
from articles.api.serializers import (
    PostListSerializer, 
    PostDetailSerializer, 
    PostCreateSerializer,
    PostDeleteSerializer,
    PostUpdateSerializer,
)

class PostListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = PostListSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'