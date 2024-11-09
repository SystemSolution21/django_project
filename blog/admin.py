from django.contrib import admin
from .models import Post

admin.site.register(model_or_iterable=Post)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
