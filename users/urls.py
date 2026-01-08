# users/urls.py

# Import django libraries
from django.urls import path
from django.urls.resolvers import URLPattern

# Import local modules
from . import views

# Define urlpatterns
urlpatterns: list[URLPattern] = [
    path(route="register/", view=views.register, name="register"),
    path(route="profile/", view=views.profile, name="profile"),
]
