from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from .models import Board, Tag

class WriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email']

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ['name']

class BoardSerializer(serializers.ModelSerializer):
    # writer = WriterSerializer
    tag = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    update_tag = serializers.ListField(
        child=serializers.CharField(max_length=10), write_only=True
    )

    def create(self, validated_data):
        tag_name = validated_data.pop('update_tag')
        instance = super().create(validated_data)
        writer = self.context['request'].user
        tags = []
        for name in tag_name:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        instance.tag.set(tags)
        return instance
    
    def update(self, instance, validated_data):
        tag_name = validated_data.pop('update_tag')
        instance = super().update(instance, validated_data)
        writer = self.context['request'].user
        tags = []
        for name in tag_name:
            tag, created = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        instance.tag.set(tags)
        return instance

    class Meta:
        model = Board
        exclude = []