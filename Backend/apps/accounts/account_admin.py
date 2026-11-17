from django.contrib import admin
from django.contrib.auth.models import User

from .account_models import AccountProfile


@admin.register(AccountProfile)
class AccountProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "phone",
        "is_email_verified",
        "created_at"
    )

    list_filter = (
        "is_email_verified",
        "created_at"
    )

    search_fields = (
        "user__username",
        "user__email",
        "phone"
    )

    readonly_fields = (
        "created_at",
        "updated_at"
    )