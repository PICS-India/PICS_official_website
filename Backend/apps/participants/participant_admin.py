from django.contrib import admin

from .participant_models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
        "phone",
        "college_name",
        "department",
        "academic_year",
        "is_verified",
        "created_at",
    )

    list_filter = (
        "academic_year",
        "gender",
        "department",
        "is_verified",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "college_name",
    )

    list_editable = (
        "is_verified",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("-created_at",)

    list_per_page = 25
