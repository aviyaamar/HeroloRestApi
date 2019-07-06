from django.shortcuts import render
from rest_framework import viewsets
from .models import Message
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, MessageSerializer
from .permissions import isAuthorOrReadOnly
from rest_framework.response import Response
from django.db.models import Q


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UserMessagesViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing users Messages.
    """

    def list(self, request):
        user = get_user_model().objects.get(pk=request.user.id)
        print(user)
        queryset = Message.objects.filter(Q(sender=user) | Q(receiver=user))
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
