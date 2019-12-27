from rest_framework.serializers import ModelSerializer
from articles.models import Article

class PostListSerializer(ModelSerializer):
    class Meta:
        model  = Article
        fields = '__all__'