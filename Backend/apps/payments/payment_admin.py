from django.contrib import admin

from .payment_models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "registration",
        "amount",
        "payment_method",
        "payment_status",
        "transaction_id",
        "created_at"
    )

    list_filter = (
        "payment_status",
        "payment_method",
        "created_at"
    )

    search_fields = (
        "transaction_id",
        "provider"
    )

    readonly_fields = (
        "created_at",
        "updated_at"
    )