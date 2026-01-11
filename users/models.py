# users/models.py

# Import django libraries
from django.contrib.auth.models import User
from django.db import models

# Import third-party libraries
from PIL import Image
from PIL.ImageFile import ImageFile


class Profile(models.Model):
    """User profile model.

    Attributes:
        user (User): User.
        image (ImageField): User profile image.
    """

    user: models.OneToOneField[User] = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self) -> str:
        """Represent user profile."""
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs) -> None:
        """Save user profile image."""
        super().save(*args, **kwargs)

        img: ImageFile = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(size=output_size)
            img.save(fp=self.image.path)
