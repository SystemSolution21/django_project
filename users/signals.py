# users/signals.py

# Import django libraries
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Import local modules
from .models import Profile


@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) -> None:
    """Create a profile for each new user."""
    if created and not kwargs.get("raw", False):
        Profile.objects.get_or_create(user=instance)


@receiver(signal=post_save, sender=User)
def save_profile(sender, instance, **kwargs) -> None:
    """Save a profile for each new user."""
    instance.profile.save()
