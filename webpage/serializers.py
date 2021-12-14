from rest_framework import serializers
from .models import Article
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'description', 'Email', 'last_modified')
    title= serializers.CharField()
    description = serializers.CharField()
    Email=serializers.EmailField()
    last_modified = serializers.DateTimeField()
    def create(self,validated_data):
        return Article.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.Email = validated_data.get('Email', instance.Email)
        instance.last_modified = validated_data.get('last_modified', instance.last_modified)
        instance.save()
        return instance


