# blog/admin.py

# Import django libraries
from django.contrib import admin

# Import local modules
from .models import Post

# Register your models here.
admin.site.register(model_or_iterable=Post)
