from django.views.generic import ListView
from web.models import ItemType

class ItemTypeList(ListView):
    model = ItemType
    template_name = "web/itemtype_list.html"