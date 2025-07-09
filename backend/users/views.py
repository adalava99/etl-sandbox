from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .models import *
import json
from django.contrib.auth.hashers import make_password
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        user = Users.objects.create(
            name= validated_data['name'],
            email = validated_data['email'],
            password=make_password(validated_data['password'])
        )
        return Response({
            'id' : user.id,
            'name': user.name,
            'email': user.email
        }, status=status.HTTP_201_CREATED)
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)