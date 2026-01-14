# mysite/urls.py
"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import django libraries
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.static import serve

# Import local modules
from blog import views as blog_views
from users import views as user_views

# Define urlpatterns
urlpatterns = [
    # path(route="admin/", view=admin.site.urls),
    path("secure-admin-portal/", view=admin.site.urls),
    path(route="register/", view=user_views.register, name="register"),
    path(route="profile/", view=user_views.profile, name="profile"),
    path(
        route="login/",
        view=auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        route="logout/",
        view=auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        route="password-reset/",
        view=auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        route="password-reset/done/",
        view=auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        route="password-reset-confirm/<uidb64>/<token>/",
        view=auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        route="password-reset-complete/",
        view=auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path(route="", view=blog_views.landing_page, name="landing-page"),
    path(route="", view=include(arg="blog.urls")),
]

#  This manual serving of media files via serve is suitable for local testing with DEBUG=False.
# In a real production environment (like AWS, Heroku, or a VPS),
# it would typically configure web server (Nginx/Apache) or a storage service (like AWS S3) to handle these files directly.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path("media/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
    ]
