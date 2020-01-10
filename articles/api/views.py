from articles.models import Article
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import generics 
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from articles.api.serializers import (
    PostListSerializer, 
    PostDetailSerializer, 
    PostCreateSerializer,
    PostDeleteSerializer,
    PostUpdateSerializer,
    PostDeleteUpdateSerializer,
)
# custom persmission
from articles.api.permissions import AuthorCanManageOrReadOnly
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser, #request.user.is_staff == True
    IsAuthenticatedOrReadOnly,
)

class PostListAPIView(generics.ListAPIView):
    # queryset = Article.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend,]
    search_fields = ['title','body','author__username']
    ordering_fields = ['title', 'author__username', 'date', 'updatedatetime']
    filterset_fields = ['title','body','author__username']

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_superuser:
            # superuser can see all posts
            queryset = Article.objects.all()
        elif not self.request.user.is_anonymous:
            # otherwise every user can see his posts
            queryset = Article.objects.filter(author=self.request.user)
        else:
            return None
        # Custom search. It is not related to rest_framework
        query = self.request.GET.get('q')
        if query:
            # if user search for something by 'q' keyword
            queryset = queryset.filter(
                Q(title__icontains=query)|
                Q(slug__icontains=query)|
                Q(body__icontains=query)|
                Q(author__username__icontains=query)
                ).distinct().order_by('-date')
        return queryset

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = PostCreateSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        # you can send email here and etc. this email send when serializer create

class PostDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteSerializer
    lookup_field = 'slug'
    permission_classes = [AuthorCanManageOrReadOnly,]

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
    permission_classes = [AuthorCanManageOrReadOnly,]

    def partial_update(self, serializer):
        serializer.save(author=self.request.user)    
        # you can send email here and etc. this email send when serializer create
        
class PostDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = PostDeleteUpdateSerializer
    lookup_field = 'slug'
    permission_classes = [AuthorCanManageOrReadOnly,]


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