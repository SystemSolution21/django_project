# blog/urls.py

# Import django libraries
from django.urls import path
from django.urls.resolvers import URLPattern

# Import local modules
from . import views
from .views import (
    LatestPostListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    UserPostListView,
)

# Define urlpatterns
urlpatterns: list[URLPattern] = [
    # path(route="", view=views.home, name="blog-home"), # function base view
    path(route="", view=PostListView.as_view(), name="blog-index"),
    path(route="latest/", view=LatestPostListView.as_view(), name="post-latest"),
    path(
        route="user/<str:username>/", view=UserPostListView.as_view(), name="user-posts"
    ),
    path(route="post/<int:pk>/", view=PostDetailView.as_view(), name="post-detail"),
    path(route="post/new/", view=PostCreateView.as_view(), name="post-create"),
    path(
        route="post/<int:pk>/update/", view=PostUpdateView.as_view(), name="post-update"
    ),
    path(
        route="post/<int:pk>/delete/", view=PostDeleteView.as_view(), name="post-delete"
    ),
    path(route="home/", view=views.home, name="blog-home"),
    path(route="about/", view=views.about, name="blog-about"),
    path(route="calendar/", view=views.calendar, name="blog-calendar"),
    path(
        route="database-ownership/",
        view=views.database_ownership,
        name="blog-database_ownership",
    ),
    path(
        route="debug-django-container/",
        view=views.debug_django_container,
        name="blog-debug_django_container",
    ),
    path(
        route="docker-commands/",
        view=views.docker_commands,
        name="blog-docker_commands",
    ),
]
