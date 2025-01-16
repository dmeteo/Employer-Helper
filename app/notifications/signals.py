from django.db.models.signals import post_save
from django.dispatch import receiver
from app.tasks.models import Task
from app.users.models import User
from app.notifications.services import NotificationService


@receiver(post_save, sender=User)
def notify_intern_on_manager_assignment(sender, instance, created, **kwargs):
    if not instance.role or instance.role.level != 1:
        return

    if not created and instance.tracker.has_changed('manager'):
        message = f"Вам назначен руководитель: {instance.manager.last_name} {instance.manager.first_name}."
        NotificationService.create_notification(
            user=instance,
            message=message,
            type="info"
        )


@receiver(post_save, sender=User)
def notify_manager_on_intern_assignment(sender, instance, created, **kwargs):
    if not instance.role or instance.role.level != 1:
        return

    if not created and instance.tracker.has_changed('manager'):
        message = f"Вам назначен стажёр: {instance.last_name} {instance.first_name}."
        NotificationService.create_notification(
            user=instance.manager,
            message=message,
            type="info"
        )


@receiver(post_save, sender=Task)
def notify_create_task_to_intern(sender, instance, created, **kwargs):
    if created:
        message = f"Вам назначена задача: {instance.title}"
        NotificationService.create_notification(
            user=instance.worker,
            message=message,
            type="info"
        )