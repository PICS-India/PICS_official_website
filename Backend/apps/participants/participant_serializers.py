from rest_framework import serializers
from .participant_models import Participant


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "gender",
            "college_name",
            "department",
            "academic_year",
            "city",
            "state",
            "profile_image",
            "is_verified",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "is_verified",
            "created_at",
            "updated_at",
        ]

    def validate_phone(self, value):
        cleaned_phone = value.strip()

        if not cleaned_phone.replace("+", "").isdigit():
            raise serializers.ValidationError(
                "Enter a valid phone number."
            )

        if len(cleaned_phone.replace("+", "")) < 10:
            raise serializers.ValidationError(
                "Phone number must contain at least 10 digits."
            )

        return cleaned_phone

    def validate_full_name(self, value):
        if not value.strip():
            raise serializers.ValidationError(
                "Full name cannot be empty."
            )

        return value.strip()
