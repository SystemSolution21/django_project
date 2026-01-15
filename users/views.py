# users/views.py

# Import built-in libraries
import logging
import os

# Import django libraries
from django.contrib import messages
from django.contrib.auth import logout  # To handle GET method error
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

# Import local modules
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from .models import Profile

# Get an instance of a logger
logger: logging.Logger = logging.getLogger(name=__name__)


# users registration
def register(request) -> HttpResponseRedirect | HttpResponse:
    """User registration view."""

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request=request,
                message="Your account has been created! You are now able to login.",
            )
            return redirect(to="login")
    else:
        form = UserRegisterForm()
    return render(
        request=request, template_name="users/register.html", context={"form": form}
    )


# Django version 5 or above only support POST method for logout request.
# Instead, auth.logout() can use to remove authenticated user's
# GET method request and flush their session data.
def logout_view(request) -> HttpResponse:
    """Logout view."""

    logout(request=request)
    return render(request=request, template_name="users/logout.html")


# Login required to view profile
@login_required
def profile(request) -> HttpResponse:
    """User profile view."""

    if request.method == "POST":
        u_form = UserUpdateForm(data=request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            data=request.POST, files=request.FILES, instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            user_profile: Profile = Profile.objects.get(user=request.user)
            old_image_path: str = user_profile.image.path
            old_image_name: str = user_profile.image.name

            # Save new user and profile data
            u_form.save()
            p_form.save()

            # Delete old image if new image is uploaded
            if request.user.profile.image.path != old_image_path:
                if (
                    old_image_name
                    != Profile._meta.get_field(field_name="image").default
                ):
                    if os.path.exists(path=old_image_path):
                        os.remove(path=old_image_path)

            logger.info(
                msg=f"User '{request.user.username}' updated their profile successfully."
            )
            messages.success(request=request, message="Your account has been updated!")
            return redirect(to="profile")
    else:
        # GET request
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Create context
    context: dict[str, UserUpdateForm | ProfileUpdateForm] = {
        "u_form": u_form,
        "p_form": p_form,
    }

    return render(request=request, template_name="users/profile.html", context=context)
