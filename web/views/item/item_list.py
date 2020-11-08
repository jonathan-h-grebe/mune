from web.models import Item
from datetime import datetime, timedelta
from django.contrib import messages
from django.views.generic import ListView


class ItemList(ListView):
    model = Item
    template_name = "web/item_list.html"

    def get_queryset(self):
        try:
            query = Item.objects.exclude(status__in=("作成中", "承認待ち", "取り下げ"))
            if self.request.GET:
                params = self.request.GET.copy()
                #reqのurlパラメータから、Itemのfieldと該当するものを取得
                item_field_params = dict()
                for p in params:
                    try:
                        Item._meta.get_field(p)
                        item_field_params[p] = params[p]
                    except Exception as e:
                        pass
                query = query.filter(**item_field_params)

            return query
            
        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()

