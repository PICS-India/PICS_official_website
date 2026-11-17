from rest_framework import serializers

from .payment_models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Payment

        fields = "__all__"

        read_only_fields = [
            "id",
            "payment_status",
            "transaction_id",
            "provider",
            "created_at",
            "updated_at"
        ]

    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Payment amount must be greater than zero."
            )

        return value