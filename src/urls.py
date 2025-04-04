from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="app.home")),
    path("admin/", admin.site.urls),
    path("articles/", include("app.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    # development
    path("__reload__/", include("django_browser_reload.urls")),
]
