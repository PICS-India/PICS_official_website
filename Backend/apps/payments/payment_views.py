from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .payment_models import Payment
from .payment_serializers import PaymentSerializer


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Payment.objects.select_related(
        "registration"
    ).all()

    serializer_class = PaymentSerializer

    permission_classes = [IsAdminUser]