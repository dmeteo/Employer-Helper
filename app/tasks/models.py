from datetime import datetime
from django.db import models
from django.forms import ValidationError
from app.users.models import User
from config import settings


class Task(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="author",
        null=False)
    date_start = models.DateField(default=datetime.now)
    deadline = models.DateField()
    title = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    requirments = models.TextField(max_length=1000, null=True)
    status = models.BooleanField()
    worker = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="worker",
        null=False)
    task_end = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "task"


class TaskStatus(models.Model):
    name = models.CharField()
    