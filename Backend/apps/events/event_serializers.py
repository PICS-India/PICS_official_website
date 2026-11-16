from rest_framework import serializers
from .event_models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = [
            "id",
            "slug",
            "created_at",
            "updated_at",
        ]

    def validate(self, data):
        start_date = data.get(
            "start_date",
            getattr(self.instance, "start_date", None)
        )

        end_date = data.get(
            "end_date",
            getattr(self.instance, "end_date", None)
        )

        registration_start = data.get(
            "registration_start",
            getattr(self.instance, "registration_start", None)
        )

        registration_end = data.get(
            "registration_end",
            getattr(self.instance, "registration_end", None)
        )

        if start_date and end_date and end_date <= start_date:
            raise serializers.ValidationError(
                "Event end date must be after start date."
            )

        if registration_start and registration_end:
            if registration_end <= registration_start:
                raise serializers.ValidationError(
                    "Registration end must be after registration start."
                )

        if registration_end and start_date:
            if registration_end > start_date:
                raise serializers.ValidationError(
                    "Registration must close before the event starts."
                )

        return data
