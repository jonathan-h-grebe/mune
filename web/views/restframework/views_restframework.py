# DjangoRestFramework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from web.serializer import ItemSerializer, CaseSerializer
from web.models import Item, Case


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_fields = ("name", )


class CaseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    filter_fields = ("id",)

