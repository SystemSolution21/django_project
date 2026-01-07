from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users application configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self) -> None:
        import users.signals  # noqa: F401
