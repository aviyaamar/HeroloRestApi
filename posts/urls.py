from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, MessageViewSet, UserMessagesViewSet


router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('inbox', UserMessagesViewSet,
                base_name='user_messages')
router.register('', MessageViewSet, base_name='messages')


urlpatterns = router.urls
