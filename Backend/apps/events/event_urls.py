from rest_framework.routers import DefaultRouter
from .event_views import EventViewSet

router = DefaultRouter()

router.register(
    r"",
    EventViewSet,
    basename="pics-events"
)

urlpatterns = router.urls
