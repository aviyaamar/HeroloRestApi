from rest_framework import serializers
from .models import Post, Message
from django.contrib.auth import get_user_model


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = Post


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'sender', 'receiver',
                  'subject', 'message', 'created_at')
        model = Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = get_user_model()
