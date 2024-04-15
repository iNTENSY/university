from django.contrib import admin
from django.urls import path, include

from .spectacular import spectacular_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/", include("api.urls", namespace="api"))
] + spectacular_urls
