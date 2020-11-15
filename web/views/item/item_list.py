from web.models import Item
from datetime import datetime, timedelta
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q

class ItemList(ListView):
    model = Item
    template_name = "web/item_list.html"

    #一覧用Itemデータを抽出
    def get_queryset(self):
        try:
            all_items_query = Item.objects.all()
            #「フィルタ」ボタンが押下された場合
            if self.request.GET:
                params = self.request.GET.copy()

                query_condition = Q()
                #reqのurlパラメータから、Itemのfieldと該当するものを取得
                item_field_params = dict()
                for p in params:
                    try:
                        Item._meta.get_field(p)
                        item_field_params[p] = params[p]
                        #fieldと該当するqueryのOR条件を作成
                        query_condition |= Q( **{p:params[p]}  )

                    #Itemのfieldと該当しないurlパラメータを無視する
                    except Exception as e:
                        pass

                selected_items = all_items_query.filter(query_condition)

                return selected_items
            
            else:
                return all_items_query

        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()


