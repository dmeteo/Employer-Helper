from django.db.models.signals import post_save
from django.dispatch import receiver
from app.users.models import User
from notifications.services import NotificationService


@receiver(post_save, sender=User)
def notify_intern_on_manager_assignment(sender, instance, created, **kwargs):
    if not instance.role or instance.role.level != 1:
        return

    if instance.manager:
        message = f"Вам назначен руководитель: {instance.manager.last_name} {instance.manager.first_name}."
        NotificationService.create_notification(
            recipient=instance,
            message=message,
            type="info"
        )
