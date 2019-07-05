from django.urls import path
# from .views import PostDetail,PostList,UserList,UserDetail
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PostViewSet, MessageViewSet, UserMessagesViewSet

# urlpatterns = [
#     path('',PostList.as_view()),
#     path('<int:pk>/',PostDetail.as_view()),
#     path('users/',UserList.as_view()),
#     path('users/<int:pk>/',UserDetail.as_view()),

# ]

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('messages', MessageViewSet, base_name='messages')
router.register('inbox', UserMessagesViewSet,
                base_name='user_messages')
router.register('', PostViewSet, base_name='posts')

urlpatterns = router.urls
