
from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    # Validate event timings
    def validate(self, data):

        start_time = data.get(
            'start_time',
            getattr(self.instance, 'start_time', None)
        )

        end_time = data.get(
            'end_time',
            getattr(self.instance, 'end_time', None)
        )

        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        return data
