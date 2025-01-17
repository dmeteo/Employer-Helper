from datetime import datetime, timedelta
from django.test import TestCase
from django.db.models.signals import post_save

from app.users.models import Role, User
from app.tasks.models import Task
from app.notifications.models import Notification
from app.notifications.signals import *


class NotificationTestCase(TestCase):
    def setUp(self):
        self.role1 = Role.objects.create(
            name = "1",
            level = 1
        )


        self.role2 = Role.objects.create(
            name = "2",
            level = 2
        )
        

        self.manager = User.objects.create(
            email="manager@example.com",
            first_name="Алексей",
            last_name="Большой",
            surname="Ментор",
            role_id=self.role2.id,
        )
        self.intern = User.objects.create(
            email="intern@example.com",
            first_name="Алиса",
            last_name="Русских",
            surname="Стажер",
            role_id=self.role1.id,
            manager=None
        )

    def test_notification_on_manager_assignment(self):
        post_save.connect(notify_intern_on_manager_assignment, sender=User)

        self.intern.manager = self.manager
        self.intern.save()

        notification = Notification.objects.filter(user=self.intern).first()
        self.assertIsNotNone(notification, "Уведомление не было создано.")
        self.assertEqual(
            notification.message,
            f"Вам назначен руководитель: {self.manager.last_name} {self.manager.first_name}.",
            "Сообщение уведомления некорректно."
        )

    def test_notification_on_intern_assignment(self):
        post_save.connect(notify_manager_on_intern_assignment, sender=User)

        self.intern.manager = self.manager
        self.intern.save()

        notification = Notification.objects.filter(user=self.manager).first()
        self.assertIsNotNone(notification, "Уведомление не было создано.")
        self.assertEqual(
            notification.message,
            f"Вам назначен стажёр: {self.intern.last_name} {self.intern.first_name}.",
            "Сообщение уведомления некорректно."
        )

    def test_no_notification_on_other_changes(self):
        post_save.connect(notify_intern_on_manager_assignment, sender=User)

        self.intern.first_name = "Новое имя"
        self.intern.save()

        notifications = Notification.objects.filter(user=self.intern)
        self.assertEqual(
            notifications.count(), 
            0, 
            "Уведомления не должны создаваться при изменении других полей."
        )

    def test_notification_create_task(self):
        post_save.connect(notify_create_task_to_intern, sender=Task)

        self.assertEqual(Task.objects.filter(worker=self.intern).count(), 0)

        task = Task.objects.create(
            author=self.manager,
            worker=self.intern,
            date_start = datetime.now(),
            deadline = datetime.now() + timedelta(days=1, hours=3),
            title="Задача 1",
            description="Задача",
            requirments="Требования",
            status=0,
        )
        self.assertEqual(Task.objects.filter(worker=self.intern).count(), 1)

        notification = Notification.objects.get(user=self.intern)
        expected_message = f"У вас новая задача: {task.title}"
        self.assertEqual(notification.message, expected_message)
        self.assertEqual(notification.type, "info")

        self.assertEqual(notification.user, self.intern)


        
