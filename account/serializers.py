from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all(), message='Username already exist!!!')]
    )
    password1 = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    def validate(self, data):
        """
        Check if password match.
        """
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Password does not match!!!")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
                username=validated_data['username'],
                password=validated_data['password1'],
            )
        return user
