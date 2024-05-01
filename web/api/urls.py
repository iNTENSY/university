from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AttendanceViewSet, CardsViewSet, GroupsViewSet, GroupAttendanceViewSets

app_name = "api"

router = DefaultRouter()
router.register("attendance", AttendanceViewSet, basename="attendance")
router.register("groups", GroupsViewSet, basename="groups")
router.register(r"groups/(?P<title>[a-zA-Zа-яА-Я0-9-]+)/attendance", GroupAttendanceViewSets, basename="group-attendance")
router.register("cards", CardsViewSet, basename="cards")

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]