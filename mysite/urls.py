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

# Import local modules
from users import views as user_views

# Define urlpatterns
urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route="register/", view=user_views.register, name="register"),
    path(route="profile/", view=user_views.profile, name="profile"),
    path(
        route="login/",
        view=auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    # path(
    #     route="logout/",
    #     view=auth_views.LogoutView.as_view(template_name="users/logout.html"),
    #     name="logout",
    # ),
    # use users defined logout_view to handle logout 'GET' method
    path(route="logout/", view=user_views.logout_view, name="logout"),
    path(route="", view=include(arg="blog.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
