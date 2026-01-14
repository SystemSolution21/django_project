# users/signals.py

# Import built-in libraries
import logging

# Import django libraries
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db.models.signals import post_save
from django.dispatch import receiver

# Import local modules
from .models import Profile

# Get an instance of a logger
logger = logging.getLogger(__name__)


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) -> None:
    """Create a profile for each new user."""
    if created and not kwargs.get("raw", False):
        Profile.objects.get_or_create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs) -> None:
    """Save a profile for each new user."""
    instance.profile.save()


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    logger.info(
        f"User '{user.username}' logged in from IP: {request.META.get('REMOTE_ADDR')}"
    )


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    logger.info(f"User '{user.username}' logged out.")
