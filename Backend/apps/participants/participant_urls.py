from rest_framework.routers import DefaultRouter

from .participant_views import ParticipantViewSet


router = DefaultRouter()

router.register(
    r"",
    ParticipantViewSet,
    basename="pics-participants"
)

urlpatterns = router.urls
