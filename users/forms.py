# users/forms.py

# Import django libraries
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
        fields = ["username", "email", "password1", "password2"]
