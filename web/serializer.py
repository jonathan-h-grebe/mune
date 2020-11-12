# coding: utf-8
from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import datetime
from .models import Item, Case, ItemType, CaseType


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'


class CaseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseType
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    item_type = ItemTypeSerializer()

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


class CaseSerializer(serializers.ModelSerializer):
    item_list = ItemSerializer(many=True)
    case_type = CaseTypeSerializer()

    class Meta:
        model = Case
        fields = '__all__'
