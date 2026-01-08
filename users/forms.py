# users/forms.py

# Import django libraries
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Import local modules
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """User registration form.

    Attributes:
        email (EmailField): User email.
        password1 (CharField): User password.
        password2 (CharField): User password confirmation.
        Meta (class): User registration form meta data.

    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields: list[str] = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    """User update form.

    Attributes:
        email (EmailField): User email.
        Meta (class): User update form meta data.

    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields: list[str] = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    """Profile update form.

    Attributes:
        image (ImageField): User profile image.
        Meta (class): Profile update form meta data.

    """

    class Meta:
        model = Profile
        fields: list[str] = ["image"]
