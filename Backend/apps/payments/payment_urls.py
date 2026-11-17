from rest_framework.routers import DefaultRouter

from .payment_views import PaymentViewSet


router = DefaultRouter()

router.register(
    "",
    PaymentViewSet,
    basename="pics-payments"
)

urlpatterns = router.urls