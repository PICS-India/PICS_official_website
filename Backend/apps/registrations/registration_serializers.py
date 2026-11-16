from rest_framework import serializers
from .registration_models import Registration


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = "__all__"

        read_only_fields = [
            "id",
            "status",
            "payment_status",
            "amount_paid",
            "created_at",
            "updated_at"
        ]

    def validate(self, data):

        participant = data.get(
            "participant",
            self.instance.participant if self.instance else None
        )

        event = data.get(
            "event",
            self.instance.event if self.instance else None
        )

        if participant and event:

            registrations = Registration.objects.filter(
                participant=participant,
                event=event
            )

            if self.instance:
                registrations = registrations.exclude(
                    id=self.instance.id
                )

            if registrations.exists():
                raise serializers.ValidationError(
                    "This participant is already registered for this event."
                )

        return data