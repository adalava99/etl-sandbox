from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Users
        fields = ['id', 'name', 'email', 'password']