
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'event_date',
        'venue',
        'status',
        'is_registration_open'
    )

    list_filter = (
        'status',
        'event_date',
        'is_registration_open'
    )

    search_fields = (
        'title',
        'description',
        'venue'
    )

    ordering = ('-event_date',)