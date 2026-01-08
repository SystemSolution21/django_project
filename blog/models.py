# blog/models.py

# Import django libraries
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """Post model.

    Attributes:
        title (str): Post title.
        content (str): Post content.
        date_posted (datetime): Post date posted.
        author (User): Post author."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
