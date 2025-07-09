from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'password']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = Users.objects.get(email=data['email'])
        except Users.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password")

        if not check_password(data['password'], user.password):
            raise serializers.ValidationError("Invalid email or password")

        refresh = RefreshToken.for_user(user)

        return {
            'access': str(refresh.access_token),
            'name': user.name,
            'email': user.email
        }