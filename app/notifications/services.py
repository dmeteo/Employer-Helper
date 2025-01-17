from .models import Notification


class NotificationService:

    @staticmethod
    def create_notification(user, message, type='info'):
        if not user:
            raise ValueError("Пользователь не найден")

        notification = Notification.objects.create(
            user=user,
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
        Notification.objects.filter(user=user, is_read=False).update(is_read=True)
