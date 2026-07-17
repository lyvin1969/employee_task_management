from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Notification
from .services import NotificationService


@login_required
def notification_list(request):
    """
    Display all notifications.
    """

    notifications = NotificationService.all_notifications(
        request.user
    )

    return render(
        request,
        "notifications/notification_list.html",
        {
            "notifications": notifications,
        },
    )


@login_required
def mark_as_read(request, pk):
    """
    Mark one notification as read.
    """

    notification = get_object_or_404(
        Notification,
        pk=pk,
        recipient=request.user,
    )

    NotificationService.mark_as_read(notification)

    return redirect("notifications:notification_list")


@login_required
def mark_all_as_read(request):
    """
    Mark all notifications as read.
    """

    NotificationService.mark_all_as_read(
        request.user
    )

    return redirect("notifications:notification_list")