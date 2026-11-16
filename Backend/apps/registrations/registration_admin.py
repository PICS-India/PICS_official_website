from django.contrib import admin
from .registration_models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "participant",
        "event",
        "status",
        "payment_status",
        "amount_paid",
        "created_at"
    )

    list_filter = (
        "status",
        "payment_status",
        "created_at"
    )

    search_fields = (
        "participant__full_name",
        "participant__email",
        "event__title"
    )

    readonly_fields = (
        "created_at",
        "updated_at"
    )