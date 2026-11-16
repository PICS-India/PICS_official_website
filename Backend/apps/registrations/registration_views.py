from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .registration_models import Registration
from .registration_serializers import RegistrationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):

    queryset = Registration.objects.select_related(
        "participant",
        "event"
    ).all()

    serializer_class = RegistrationSerializer

    def get_permissions(self):

        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]