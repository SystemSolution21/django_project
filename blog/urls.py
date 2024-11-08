from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns: list[URLPattern] = [
    path(route="", view=views.home, name="blog-home"),
    path(route="about/", view=views.about, name="blog-about"),
]
