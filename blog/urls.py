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
    path(route="calendar/", view=views.calendar, name="blog-calendar"),
    path(route="about/", view=views.about, name="blog-about"),
    path(route="announcements/", view=views.announcements, name="blog-announcements"),
    path(route="home/", view=views.home, name="blog-home"),
]
