from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

from .spectacular import spectacular_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("", lambda request: redirect("admin/"))
] + spectacular_urls
