from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def home(request) -> HttpResponse:
    context: dict[str, BaseManager[Post]] = {"posts": Post.objects.all()}

    return render(request=request, template_name="blog/home.html", context=context)


def about(request) -> HttpResponse:
    return render(
        request=request, template_name="blog/about.html", context={"title": "About"}
    )
