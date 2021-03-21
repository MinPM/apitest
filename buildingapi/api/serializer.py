from .models import Article
from rest_framework import serializers
from django.contrib.auth.models import User

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='article-highlight', format='html')

    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    article = serializers.HyperlinkedRelatedField(many=True, view_name='article-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'article']
        