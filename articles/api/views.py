# from django.shortcuts import render

from articles.models import Article
from rest_framework import generics
from articles.api.serializers import PostListSerializer
# from serializers import PostListSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = PostListSerializer
