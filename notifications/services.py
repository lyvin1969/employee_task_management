from .models import Notification


class NotificationService:
    """
    Handles all notification-related operations.
    """

    @staticmethod
    def create_notification(
        recipient,
        title,
        message,
        notification_type=Notification.NotificationType.SYSTEM,
    ):
        """
        Create a new notification.
        """
        return Notification.objects.create(
            recipient=recipient,
            title=title,
            message=message,
            notification_type=notification_type,
        )

    @staticmethod
    def unread_notifications(user):
        """
        Return unread notifications.
        """
        return Notification.objects.filter(
            recipient=user,
            is_read=False
        )

    @staticmethod
    def all_notifications(user):
        """
        Return all notifications.
        """
        return Notification.objects.filter(
            recipient=user
        )

    @staticmethod
    def mark_as_read(notification):
        """
        Mark one notification as read.
        """
        notification.is_read = True
        notification.save()

    @staticmethod
    def mark_all_as_read(user):
        """
        Mark every notification as read.
        """
        Notification.objects.filter(
            recipient=user,
            is_read=False
        ).update(is_read=True)