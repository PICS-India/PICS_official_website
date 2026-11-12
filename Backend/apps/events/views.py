
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()

    serializer_class = EventSerializer

    # Anyone can view events.
    # Only authenticated users can modify events.
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filter events using their status.
    def get_queryset(self):

        queryset = Event.objects.all()

        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status=status)

        return queryset
