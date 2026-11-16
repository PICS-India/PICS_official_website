from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .participant_models import Participant
from .participant_serializers import ParticipantSerializer


class ParticipantViewSet(viewsets.ModelViewSet):

    queryset = Participant.objects.all()

    serializer_class = ParticipantSerializer

    permission_classes = [IsAdminUser]

    filterset_fields = [
        "gender",
        "academic_year",
        "department",
        "college_name",
        "is_verified",
    ]

    search_fields = [
        "full_name",
        "email",
        "phone",
        "college_name",
        "department",
    ]

    ordering_fields = [
        "full_name",
        "created_at",
        "college_name",
    ]

    ordering = ["-created_at"]
