# Urls are Temp, after i will update it
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/events/", include("apps.events.event_urls")),
    path("api/participants/", include("apps.participants.participant_urls")),
    path("api/registrations/", include("apps.registrations.registration_urls")),
    path("api/accounts/", include("apps.accounts.account_urls")),
    path("api/payments/", include("apps.payments.payment_urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
