from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/v1/accounts/",
        include("apps.accounts.account_urls"),
    ),
    path(
        "api/v1/events/",
        include("apps.events.event_urls"),
    ),
    path(
        "api/v1/participants/",
        include("apps.participants.participant_urls"),
    ),
    path(
        "api/v1/registrations/",
        include("apps.registrations.registration_urls"),
    ),
    path(
        "api/v1/payments/",
        include("apps.payments.payment_urls"),
    ),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
