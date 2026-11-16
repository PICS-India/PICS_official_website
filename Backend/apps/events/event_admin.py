from django.contrib import admin
from .event_models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "mode",
        "start_date",
        "end_date",
        "status",
        "capacity",
        "registration_fee",
    )

    list_filter = (
        "status",
        "category",
        "mode",
    )

    search_fields = (
        "title",
        "description",
        "venue",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)
