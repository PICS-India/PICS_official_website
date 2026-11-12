
from django.contrib import admin
from models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'full_name',
        'email',
        'phone',
        'college',
        'academic_year'
    )

    search_fields = (
        'full_name',
        'email',
        'college'
    )

    list_filter = (
        'academic_year',
        'department'
    )

    ordering = ('full_name',)