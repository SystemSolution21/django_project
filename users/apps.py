# users/apps.py

# Import django libraries
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self) -> None:
        """Import signals.

        activates the signal handlers that automatically create user profiles
        when new users register.
        """
        import users.signals  # noqa: F401
