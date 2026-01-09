# blog/views.py

# Import django libraries
from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

# Import local modules
from .models import Post


# Home page view function base
def home(request) -> HttpResponse:
    """Home page view."""
    context: dict[str, BaseManager[Post]] = {"posts": Post.objects.all()}

    return render(request=request, template_name="blog/home.html", context=context)


# Home page view class base
class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering: list[str] = ["-date_posted"]


# Post detail page view
class PostDetailView(DetailView):
    model = Post


# About page view function base
def about(request) -> HttpResponse:
    """About page view."""
    return render(
        request=request, template_name="blog/about.html", context={"title": "About"}
    )
