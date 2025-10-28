from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth import authenticate
from .models import CustomUser


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "full_name",
            "date_of_birth",
            "address",
            "gender",
            "phone_number",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password_1 = serializers.CharField(write_only=True)
    password_2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "username",
            "full_name",
            "date_of_birth",
            "address",
            "gender",
            "phone_number",
            "password_1",
            "password_2",
        ]

    def validate(self, data):
        if data["password_1"] != data["password_2"]:
            raise ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        password = validated_data.pop("password_1")
        validated_data.pop("password_2")
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise ValidationError("No user found with this email")

        if not user.check_password(password):
            raise ValidationError("Wrong password.")

        data["user"] = user
        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        self.token = data.get("refresh")
        if not self.token:
            raise serializers.ValidationError({"refresh": "Refresh token is required."})
        return data

class TokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        token = data.get("refresh")
        try:
            refresh = RefreshToken(token)
            return {"access": str(refresh.access_token)}
        except TokenError:
            raise NotAuthenticated("Invalid or expired refresh token.")


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(write_only=True)
    new_password_1 = serializers.CharField(write_only=True)
    new_password_2 = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context["request"].user
        current_password = data.get("current_password")
        new_password_1 = data.get("new_password_1")
        new_password_2 = data.get("new_password_2")

        if not user.check_password(current_password):
            raise ValidationError(
                {"current_password": "Current password is incorrect."}
            )

        if new_password_1 != new_password_2:
            raise ValidationError({"new_password": "New passwords do not match."})

        return data
