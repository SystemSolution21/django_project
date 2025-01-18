from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout  # To handle GET method error
from .forms import UserRegisterForm


# users registration
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request=request,
                message=f"Your account has been created! You are now able to login.",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(
        request=request, template_name="users/register.html", context={"form": form}
    )


# Django version 5 or above only support POST method for logout request.
# Instead, auth.logout() can use to remove authenticated user's
# GET method request and flush their session data.
def logout_view(request):
    logout(request=request)
    return render(request=request, template_name="users/logout.html")


# users profile
@login_required
def profile(request):
    return render(request=request, template_name="users/profile.html")
