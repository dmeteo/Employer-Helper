import os
from datetime import datetime
from django.db import models
from app.users.models import User


class Status(models.Model):
    name = models.CharField()
    level = models.SmallIntegerField()

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


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
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="status",
        null=False)
    worker = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="worker",
        null=False)
    task_end = models.DateTimeField(null=True, blank=True)

    def get_file_path(obj, fname):
        return os.path.join(
            'tasks',
            obj.id,
            fname,
        )
    
    class Meta:
        verbose_name_plural = "task"


class TaskFile(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_files')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_files')
    file = models.FileField(upload_to='task_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Файл в {self.task} загружен {self.user}"


class Category(models.Model):
    name = models.CharField()
    