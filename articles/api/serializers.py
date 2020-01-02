from rest_framework.serializers import ModelSerializer
from articles.models import Article

class PostListSerializer(ModelSerializer):
    class Meta:
        model  = Article
        fields = ('title','slug','id')
        # fields = '__all__'

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class PostDeleteSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'