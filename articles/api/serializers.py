from rest_framework.serializers import ModelSerializer
from articles.models import Article

class PostListSerializer(ModelSerializer):
    class Meta:
        model  = Article
        exclude = ('thumb',)
        # fields = '__all__'
        # fields = ('title', 'slug', 'id', 'author')

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        exclude = ('author',)
        # fields = '__all__'

class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        exclude = ('author',)
        # fields = '__all__'

class PostDeleteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'