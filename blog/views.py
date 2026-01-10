# blog/views.py

# Import built-in libraries
from typing import cast

# Import django libraries
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models.manager import BaseManager
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

# Import local modules
from .models import Post


# Home page view function base (Only for testing)
def home(request) -> HttpResponse:
    """Home page view."""
    context: dict[str, BaseManager[Post]] = {"posts": Post.objects.all()}

    return render(request=request, template_name="blog/home.html", context=context)


# List all posts
class PostListView(ListView):
    """List all posts.
    Attributes:
        model (Post): Post model.
        template_name (str): Template name(<app>/<model>_<viewtype>.html).
        context_object_name (str): Context object name.
        ordering (list[str]): Ordering.
        paginate_by (int): Paginate by.
    """

    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering: list[str] = ["-date_posted"]
    paginate_by = 5


# List user's posts
class UserPostListView(ListView):
    """List all posts.
    Attributes:
        model (Post): Post model.
        template_name (str): Template name(<app>/<model>_<viewtype>.html).
        context_object_name (str): Context object name.
        ordering (list[str]): Ordering.
        paginate_by (int): Paginate by.
    """

    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    # Get user's posts
    def get_queryset(self) -> BaseManager[Post]:
        """Get user's posts."""
        user: User = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


# Post detail
class PostDetailView(DetailView):
    """Post detail.
    Attributes:
        model (Post): Post model."""

    model = Post


# Create post
class PostCreateView(LoginRequiredMixin, CreateView):
    """Create post.
    Attributes:
        model (Post): Post model.
        fields (list[str]): Fields.
    """

    model = Post
    fields: list[str] = ["title", "content"]

    # Set current user as author of post and validate form
    def form_valid(self, form) -> HttpResponse:
        """Validate form."""
        form.instance.author = self.request.user
        return super().form_valid(form=form)


# Update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Update post.
    Attributes:
        model (Post): Post model.
        fields (list[str]): Fields.
    """

    model = Post
    fields: list[str] = ["title", "content"]

    # Set current user as author of post and validate form
    def form_valid(self, form) -> HttpResponse:
        """Validate form."""
        form.instance.author = self.request.user
        return super().form_valid(form=form)

    # Check current user as author of post
    def test_func(self) -> bool:
        """Check current user as author of post."""
        post: Post = cast(
            Post, self.get_object()
        )  # casting to Post for static type checking
        if self.request.user == post.author:
            return True
        return False


# Delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete post.
    Attributes:
        model (Post): Post model.
        success_url (str): Success url.
    """

    model = Post
    success_url = "/"

    # Check current user as author of post
    def test_func(self) -> bool:
        """Check current user as author of post."""
        post: Post = cast(
            Post, self.get_object()
        )  # casting to Post for static type checking
        if self.request.user == post.author:
            return True
        return False


# About page view function base
def about(request) -> HttpResponse:
    """About page view."""
    return render(
        request=request, template_name="blog/about.html", context={"title": "About"}
    )
