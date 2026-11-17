from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from .account_models import AccountProfile


class AccountSignupSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        validators=[validate_password]
    )

    confirm_password = serializers.CharField(write_only=True)

    phone = serializers.CharField(
        required=False,
        allow_blank=True
    )

    class Meta:
        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "confirm_password",
            "phone"
        ]

    def validate_email(self, value):

        email = value.strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError(
                "This email is already registered."
            )

        return email

    def validate(self, data):

        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError({
                "confirm_password": "Passwords do not match."
            })

        return data

    def create(self, validated_data):

        validated_data.pop("confirm_password")

        password = validated_data.pop("password")

        phone = validated_data.pop("phone", "")

        user = User.objects.create_user(
            password=password,
            **validated_data
        )

        AccountProfile.objects.create(
            user=user,
            phone=phone
        )

        return user


class AccountProfileSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(
        source="account_profile.phone",
        required=False
    )

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone"
        ]

        read_only_fields = ["id", "username", "email"]