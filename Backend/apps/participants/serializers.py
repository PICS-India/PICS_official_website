
from rest_framework import serializers
from models import Participant

class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    # Validate participant phone number
    def validate_phone(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError(
                "Phone number must contain 10 to 15 digits."
            )

        return value