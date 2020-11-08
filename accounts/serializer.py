# coding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import datetime
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
