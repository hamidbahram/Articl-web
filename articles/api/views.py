from articles.models import Article
from rest_framework import generics 
from articles.api.serializers import (
    PostListSerializer, 
    PostDetailSerializer, 
    PostCreateSerializer,
    PostDeleteSerializer,
    PostUpdateSerializer,
    PostDeleteUpdateSerializer,
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

class PostDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'slug'

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'

class PostDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteUpdateSerializer
    lookup_field = 'slug'