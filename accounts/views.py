from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from accounts.serializer import CustomUserSerializer
from accounts.models import CustomUser
# Create your views here.


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_fields = ("username", )


class CustomUserViewSet2(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    filter_fields = ("username", )
