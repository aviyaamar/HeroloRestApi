from django.shortcuts import render
# from rest_framework import generics,permissions
from rest_framework import viewsets
from .models import Post, Message
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer, MessageSerializer
from .permissions import isAuthorOrReadOnly
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.

# class PostList(generics.ListCreateAPIView):
#     #permission_classes = (permissions.IsAuthenticated,)
#     #permission_classes =(isAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated,)
    #permission_classes =(isAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class MessageViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated,)
    #permission_classes =(isAuthorOrReadOnly,)
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

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     #permission_classes = (permissions.IsAuthenticated,)
#     permission_classes =(isAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListAPIView):
#     #permission_classes = (permissions.IsAuthenticated,)
#     #permission_classes =(isAuthorOrReadOnly,)
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = (permissions.IsAuthenticated,)
    #permission_classes =(isAuthorOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class = UserSerializer
