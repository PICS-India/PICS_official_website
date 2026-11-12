
from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'participant',
        'event',
        'status',
        'registration_date'
    )

    list_filter = (
        'status',
        'registration_date'
    )

    search_fields = (
        'participant__full_name',
        'participant__email',
        'event__title'
    )

    readonly_fields = (
        'registration_date',
        'updated_at'
    )

    ordering = ('-registration_date',)