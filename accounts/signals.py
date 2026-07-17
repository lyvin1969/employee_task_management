# accounts/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser


@receiver(post_save, sender=CustomUser)
def user_post_save(sender, instance, created, **kwargs):
    """
    Handle actions after a CustomUser is saved.
    """

    if created:
        # Future enhancement:
        # Automatically create an Employee profile
        # when the employees app is implemented.
        pass