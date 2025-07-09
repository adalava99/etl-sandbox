from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('createUser/', create_user),
    path('login/', login)
]