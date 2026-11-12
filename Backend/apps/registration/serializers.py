
from django.utils import timezone
from rest_framework import serializers

from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = '__all__'

        read_only_fields = [
            'id',
            'registration_date',
            'updated_at',
            'status'
        ]

    def validate(self, data):

        event = data.get(
            'event',
            self.instance.event if self.instance else None
        )

        if event:

            # Check whether registration is open
            if not event.is_registration_open:
                raise serializers.ValidationError(
                    "Registration is closed for this event."
                )

            # Check registration deadline
            if (
                event.registration_deadline
                and timezone.now() > event.registration_deadline
            ):
                raise serializers.ValidationError(
                    "Registration deadline has passed."
                )

            # Check maximum participant limit
            if event.max_participants is not None:

                total = Registration.objects.filter(
                    event=event,
                    status__in=['pending', 'confirmed']
                ).count()

                if not self.instance and total >= event.max_participants:
                    raise serializers.ValidationError(
                        "Event registration limit has been reached."
                    )

        return data