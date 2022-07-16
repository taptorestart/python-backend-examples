from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response.pop('password')
        return response

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'created_at', 'updated_at']
