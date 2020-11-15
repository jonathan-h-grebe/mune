from web.models import Item
from datetime import datetime, timedelta
from django.contrib import messages
from django.views.generic import ListView


class ItemList(ListView):
    model = Item
    template_name = "web/item_list.html"

    #一覧用Itemデータを抽出
    def get_queryset(self):
        try:
            query = Item.objects.exclude(status__in=("作成中", "承認待ち", "取り下げ"))
            if self.request.GET:
                area_list = self.request.GET.getlist("area_list", [])

                #「まとめて Check」ボタンが押下された場合
                if len(area_list) > 0:
                    query = query.filter(area__in=area_list)    
                #「まとめて Check」ボタン以外の条件有りの場合
                else:
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