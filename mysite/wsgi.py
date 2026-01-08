# mysite/wsgi.py
"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# Import built-in libraries
import os

# Import django libraries
from django.core.wsgi import get_wsgi_application

# Set environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

# Get WSGI application
application = get_wsgi_application()
