from .models import Notification


class NotificationService:

    @staticmethod
    def create_notification(recipient, message, type='info'):
        if not recipient:
            raise ValueError("Пользователь не найден")

        notification = Notification.objects.create(
            recipient=recipient,
            message=message,
            type=type
        )
        return notification


    @staticmethod
    def mark_as_read(notification_id):
        notification = Notification.objects.filter(id=notification_id).first()
        if notification:
            notification.is_read = True
            notification.save()
            return notification
        return None


    @staticmethod
    def mark_all_as_read(user):
        Notification.objects.filter(recipient=user, is_read=False).update(is_read=True)
