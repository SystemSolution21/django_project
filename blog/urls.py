# blog/urls.py

# Import django libraries
from django.urls import path
from django.urls.resolvers import URLPattern

# Import local modules
from . import views
from .views import PostDetailView, PostListView

# Define urlpatterns
urlpatterns: list[URLPattern] = [
    # path(route="", view=views.home, name="blog-home"), # function base view
    path(
        route="", view=PostListView.as_view(), name="blog-home"
    ),  # class base Post list view
    path(
        route="post/<int:pk>/", view=PostDetailView.as_view(), name="post-detail"
    ),  # Post detail view
    path(route="about/", view=views.about, name="blog-about"),
]
