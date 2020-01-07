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

from django.core.exceptions import PermissionDenied

class PostListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = PostListSerializer

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        # you can send email here and etc. this email send when serializer create

class PostDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'slug'

    def perform_destroy(self, serializer):
        # just author can delet post
        if serializer.author != self.request.user:
            raise PermissionDenied
        else:
            serializer.delete()
        # you can send email here and etc. this email send when serializer create

class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'

    def partial_update(self, serializer):
        serializer.save(author=self.request.user)    
        # you can send email here and etc. this email send when serializer create
        
class PostDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteUpdateSerializer
    lookup_field = 'slug'

'''
data = {
    'title': 'this is my title',
    'slug': 'this_is_my_title',
    'body': 'this is my body',
    'author': 1
}

new_item = PostDetailSerializer(data=data)

if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

'''