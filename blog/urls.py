# blog/urls.py

# Import django libraries
from django.urls import path
from django.urls.resolvers import URLPattern

# Import local modules
from . import views

# Define urlpatterns
urlpatterns: list[URLPattern] = [
    path(route="", view=views.home, name="blog-home"),
    path(route="about/", view=views.about, name="blog-about"),
]
