from rest_framework import serializers
from .models import Message
from django.contrib.auth import get_user_model


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'sender', 'receiver',
                  'subject', 'message', 'created_at')
        model = Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username')
        model = get_user_model()
