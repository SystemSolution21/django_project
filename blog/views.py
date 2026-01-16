# blog/views.py

# Import built-in libraries
import logging
from typing import cast

from django.conf import settings

# Import django libraries
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Max
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

# Import third-party libraries
from markdown import markdown

# Import local modules
from .models import Post

# Get an instance of a logger
logger = logging.getLogger(__name__)


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
    template_name = "blog/index.html"
    context_object_name = "posts"
    ordering: list[str] = ["-date_posted"]
    paginate_by = 3


# List latest posts
class LatestPostListView(ListView):
    """List latest posts.
    Attributes:
        model (Post): Post model.
        template_name (str): Template name(<app>/<model>_<viewtype>.html).
        context_object_name (str): Context object name.
        ordering (list[str]): Ordering.
        paginate_by (int): Paginate by.
    """

    model = Post
    template_name = "blog/latest_posts.html"
    context_object_name = "posts"
    ordering: list[str] = ["-date_posted"]
    paginate_by = 3

    # Get latest posts
    def get_queryset(self) -> BaseManager[Post]:
        """Get latest posts."""

        # Get the latest post ID for each author
        latest_post_ids = (
            Post.objects.values("author")
            .annotate(latest_date=Max("date_posted"))
            .values_list("author", "latest_date")
        )

        # Get the actual posts and order by date_posted desc
        return Post.objects.filter(
            author__in=[item[0] for item in latest_post_ids],
            date_posted__in=[item[1] for item in latest_post_ids],
        ).order_by("-date_posted")


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
    paginate_by = 3

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
        response = super().form_valid(form=form)
        post = cast(Post, getattr(self, "object"))
        logger.info(
            f"User '{self.request.user.username}' created post titled '{post.title}' (ID: {post.pk})."
        )
        return response


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
        response = super().form_valid(form=form)
        post = cast(Post, getattr(self, "object"))
        logger.info(
            f"User '{self.request.user.username}' updated post titled '{post.title}' (ID: {post.pk})."
        )
        return response

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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        post = cast(Post, self.object)
        logger.info(
            f"User '{request.user.username}' deleted post titled '{post.title}' (ID: {post.pk})."
        )
        return super().delete(request, *args, **kwargs)

    # Check current user as author of post
    def test_func(self) -> bool:
        """Check current user as author of post."""
        post: Post = cast(
            Post, self.get_object()
        )  # casting to Post for static type checking
        if self.request.user == post.author:
            return True
        return False


# Home page
def home(request) -> HttpResponse:
    """Home page view."""
    # Construct the path to README.md
    file_path = settings.BASE_DIR / "README.md"

    # Read and convert to HTML
    try:
        markdown_text = file_path.read_text(encoding="utf-8")
        # 'fenced_code' extension supports the triple backticks used in markdown
        html_content = markdown(markdown_text, extensions=["fenced_code"])
    except FileNotFoundError:
        html_content = "<p>README.md file not found.</p>"

    return render(
        request=request,
        template_name="blog/home.html",
        context={"markdown_content": html_content},
    )


# Landing page for authenticated users
def landing_page(request) -> HttpResponse:
    """Dispatch view for the landing page.
    - Authenticated users -> PostListView (Blog Index)
    - Guests -> Home View (README)
    """
    if request.user.is_authenticated:
        return PostListView.as_view()(request)

    messages.info(
        request=request,
        message="Please login to view the blog. SignUp if you don't have an account.",
    )

    return home(request)


# About page
def about(request) -> HttpResponse:
    """About page view."""

    # Construct the path to DATABASE.md
    readme_path = settings.BASE_DIR / "DATABASE.md"

    # Read and convert to HTML
    try:
        markdown_text = readme_path.read_text(encoding="utf-8")
        # 'fenced_code' extension supports the triple backticks used in markdown
        html_content = markdown(markdown_text, extensions=["fenced_code"])
    except FileNotFoundError:
        html_content = "<p>DATABASE.md file not found.</p>"

    return render(
        request=request,
        template_name="blog/about.html",
        context={"markdown_content": html_content},
    )


# Calendar page
def calendar(request) -> HttpResponse:
    """Calendar page view."""
    return render(
        request=request,
        template_name="blog/calendar.html",
        context={"title": "Calendar"},
    )


# Database Ownership page
def database_ownership(request) -> HttpResponse:
    """Database Ownership page view."""
    # Construct the path to DATABASE_OWNERSHIP.md
    file_path = settings.BASE_DIR / "DATABASE_OWNERSHIP.md"

    # Read and convert to HTML
    try:
        markdown_text = file_path.read_text(encoding="utf-8")
        # 'fenced_code' extension supports the triple backticks used in markdown
        html_content = markdown(markdown_text, extensions=["fenced_code"])
    except FileNotFoundError:
        html_content = "<p>DATABASE_OWNERSHIP.md file not found.</p>"

    return render(
        request=request,
        template_name="blog/database_ownership.html",
        context={"markdown_content": html_content},
    )


# Debug Django Container page
def debug_django_container(request) -> HttpResponse:
    """Debug Django Container page view."""
    # Construct the path to DEBUG_DJANGO_CONTAINER.md
    file_path = settings.BASE_DIR / "DEBUG_DJANGO_CONTAINER.md"

    # Read and convert to HTML
    try:
        markdown_text = file_path.read_text(encoding="utf-8")
        # 'fenced_code' extension supports the triple backticks used in markdown
        html_content = markdown(markdown_text, extensions=["fenced_code"])
    except FileNotFoundError:
        html_content = "<p>DEBUG_DJANGO_CONTAINER.md file not found.</p>"

    return render(
        request=request,
        template_name="blog/debug_django_container.html",
        context={"markdown_content": html_content},
    )


# Docker Commands page
def docker_commands(request) -> HttpResponse:
    """Docker Commands page view."""
    # Construct the path to DOCKER_COMMANDS.md
    file_path = settings.BASE_DIR / "DOCKER_COMMANDS.md"

    # Read and convert to HTML
    try:
        markdown_text = file_path.read_text(encoding="utf-8")
        # 'fenced_code' extension supports the triple backticks used in markdown
        html_content = markdown(markdown_text, extensions=["fenced_code"])
    except FileNotFoundError:
        html_content = "<p>DOCKER_COMMANDS.md file not found.</p>"

    return render(
        request=request,
        template_name="blog/docker_commands.html",
        context={"markdown_content": html_content},
    )
