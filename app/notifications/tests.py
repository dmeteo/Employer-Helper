from django.test import TestCase
from django.db.models.signals import post_save

from app.users.models import Role, User
from app.notifications.models import Notification
from app.notifications.signals import notify_intern_on_manager_assignment, notify_manager_on_intern_assignment


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
