
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAdminUser

from .models import Registration
from .serializers import RegistrationSerializer

class RegistrationPermission(BasePermission):

    def has_permission(self, request, view):

        # Allow public registration
        if request.method == 'POST':
            return True

        # Other operations require admin access
        return bool(
            request.user and request.user.is_staff
        )

class RegistrationViewSet(viewsets.ModelViewSet):

    queryset = Registration.objects.select_related(
        'participant',
        'event'
    )

    serializer_class = RegistrationSerializer

    permission_classes = [RegistrationPermission]

    # Filter registrations by event or status
    def get_queryset(self):

        queryset = Registration.objects.select_related(
            'participant',
            'event'
        )

        event_id = self.request.query_params.get('event')
        status = self.request.query_params.get('status')

        if event_id:
            queryset = queryset.filter(event_id=event_id)

        if status:
            queryset = queryset.filter(status=status)

        return queryset