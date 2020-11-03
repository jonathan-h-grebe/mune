from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from web.models import Item
from django.contrib import messages

class MyItemList(LoginRequiredMixin, ListView):
    model = Item
    template_name = "web/my_item_list.html"

    def get_queryset(self):
        try:
            query = Item.objects.filter(created_by=self.request.user)
            if self.request.GET:
                params = self.request.GET.copy()
                query = query.filter(**params.dict())
                return query
            else:
                return query
        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()
