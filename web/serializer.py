# coding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import datetime
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    # def create(self, validated_data):
    #     item = Item(**validated_data)
    #     u = get_user_model().objects.first()
    #     item.save_from_shell(u)
    #     return item
    #
    # def update(self, instance, validated_data):
    #     for k, v in validated_data.items():
    #         setattr(instance, k, v)
    #     u = get_user_model().objects.first()
    #     instance.save_from_shell(u)
    #     return instance