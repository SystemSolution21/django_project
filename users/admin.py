# users/admin.py

# Import django libraries
from django.contrib import admin

# Import local modules
from .models import Profile

# Register models
admin.site.register(model_or_iterable=Profile)
