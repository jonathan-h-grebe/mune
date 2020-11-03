from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from web.models import Item
from django.contrib import messages
from datetime import datetime, timedelta

class NewItemList(ListView):
    model = Item
    template_name = "web/item_list.html"

    def get_queryset(self):
        try:
            query = Item.objects.exclude(status__in=("作成中", "承認待ち", "取り下げ"))

            #TODO: periodパラメータにより、直近期間を調整すること
            earliest_date = datetime.now() -  timedelta(days=90)
            query = query.filter(created_at__gte= earliest_date)
            return query
            
        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()