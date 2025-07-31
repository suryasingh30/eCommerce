from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

import re
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    email = serializers.EmailField()
    full_name = serializers.CharField(min_length=3, max_length=100)

    class Meta:
        model = User
        fields = ['email', 'full_name', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    def validate_password(self, value):
        # 1 letter and 1 digiit
        if not re.search(r'[A-Za-z]', value) or not re.search(r'\d', value):
            raise serializers.ValidationError("Password must include letters and numbers.")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid email or password.")
