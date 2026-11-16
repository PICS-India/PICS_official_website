from rest_framework.routers import DefaultRouter
from .registration_views import RegistrationViewSet


router = DefaultRouter()

router.register(
    r"",
    RegistrationViewSet,
    basename="pics-registrations"
)

urlpatterns = router.urls