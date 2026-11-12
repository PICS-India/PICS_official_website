
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from models import Participant
from .serializers import ParticipantSerializer

class ParticipantViewSet(viewsets.ModelViewSet):

    queryset = Participant.objects.all()

    serializer_class = ParticipantSerializer

    # Only administrators can manage participant records
    permission_classes = [IsAdminUser]

    # Search participants by name, email or college
    def get_queryset(self):

        queryset = Participant.objects.all()

        search = self.request.query_params.get('search')

        if search:
            queryset = queryset.filter(
                full_name__icontains=search
            ) | queryset.filter(
                email__icontains=search
            ) | queryset.filter(
                college__icontains=search
            )

        return queryset