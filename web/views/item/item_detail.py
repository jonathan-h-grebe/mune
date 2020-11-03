from django.views.generic import DetailView
from web.models import Item

class ItemDetail(DetailView):
    model = Item
    template_name = "web/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context