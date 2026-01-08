# blog/views.py

# Import django libraries
from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render

# Import local modules
from .models import Post


def home(request) -> HttpResponse:
    """Home page view."""
    context: dict[str, BaseManager[Post]] = {"posts": Post.objects.all()}

    return render(request=request, template_name="blog/home.html", context=context)


def about(request) -> HttpResponse:
    """About page view."""
    return render(
        request=request, template_name="blog/about.html", context={"title": "About"}
    )
