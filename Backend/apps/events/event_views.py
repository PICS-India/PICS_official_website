from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAdminUser

from .event_models import Event
from .event_serializers import EventSerializer


class EventManagementPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True

        return bool(
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [EventManagementPermission]

    lookup_field = "slug"

    filterset_fields = ["category", "status", "mode"]
    search_fields = ["title", "description", "category", "venue"]
    ordering_fields = ["start_date", "created_at", "registration_fee"]
    ordering = ["start_date"]
