from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns: list[URLPattern] = [
    path(route="register/", view=views.register, name="register"),
    path(route="profile/", view=views.profile, name="profile"),
]
