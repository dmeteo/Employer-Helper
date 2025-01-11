from django.db import models
from app.users.models import User


class Notification(models.Model):
    TYPE_CHOICES = [
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('error', 'Error'),
    ]

    recipient = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='notifications')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='info')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient.email} - {self.type} - {self.created_at}"