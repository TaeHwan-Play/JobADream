from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Board

class WriterSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['email']

class BoardSerializer(serializers.ModelSerializer):
    writer = WriterSerializer
    
    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'content',
            'tag_set',
            'image',
            'writer',
            'created_at',
        ]