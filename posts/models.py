from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#  message contains :
# 1. sender (owner)
# 2. receiver
# 3. message
# 4. subject
# 5. creation date

class Message(models.Model):
    sender = models.ForeignKey(
        User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(
        User, related_name="receiver", on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender+' '+self.message
