# DjangoRestFramework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from web.serializer import ItemSerializer
from web.models import Item


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_fields = ("name", )


