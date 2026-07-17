from .models import Notification


def notification_context(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            recipient=request.user
        ).order_by("-created_at")[:5]

        unread_count = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()

        return {
            "navbar_notifications": notifications,
            "unread_notifications": unread_count,
        }

    return {}