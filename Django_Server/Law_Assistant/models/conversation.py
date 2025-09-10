from django.db import models
from django.utils import timezone
from .user import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_name = models.CharField(max_length=100)
    create_date = models.DateTimeField()


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    sender = models.CharField(max_length=4)
    text = models.TextField()


