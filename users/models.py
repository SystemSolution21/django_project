# users/models.py

# Import django libraries
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """User profile model.

    Attributes:
        user (User): User.
        image (ImageField): User profile image.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self) -> str:
        return f"{self.user.username} Profile"
