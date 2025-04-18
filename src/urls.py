from allauth.account.views import SignupView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", SignupView.as_view(), name="account_signup"),
    path(settings.ADMIN_URL, admin.site.urls),
    path("articles/", include("app.urls")),
    # path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", RedirectView.as_view(url="/", permanent=True)),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        # development
        path("__reload__/", include("django_browser_reload.urls")),
    ]
