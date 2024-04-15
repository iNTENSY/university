from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AttendanceViewSet

app_name = "api"

router = DefaultRouter()
router.register("attendance", AttendanceViewSet, basename="attendance")

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]