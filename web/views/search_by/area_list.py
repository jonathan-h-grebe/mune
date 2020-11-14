from django.views.generic import ListView
from django.contrib import messages
from web.models import Area
from django.db.models import Q

class AreaList(ListView):
    model = Area
    template_name = "web/area_list.html"

    #一覧用Areaデータを抽出
    def get_queryset(self):
        try:
            all_areas_query = Area.objects.all()
            #「フィルタ」ボタンが押下された場合
            if self.request.GET:
                params = self.request.GET.copy()

                #指定されたエリアでAreaを絞る
                queries = [Q(name=value) for value in params]
                query = Q()
                for item in queries:
                    query |= item
                selected_areas = all_areas_query.filter(query)

                return selected_areas
            
            else:
                return all_areas_query

        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()


    def get_context_data(self, **kwargs):
        all_areas = Area.objects.all()
        
        #デフォルトとして、各checkboxをクリアする
        area_checkbox_data = dict.fromkeys( list(map(lambda a : a.name,all_areas)),
             False )
        
        #フィルタ有の場合
        if len(all_areas) != len(self.object_list):
            #選択されたcheckboxをcheckした状態を維持する
            for selected_area in self.object_list:
                area_checkbox_data[selected_area.name] = True

        context = super().get_context_data()
        context['area_checkbox_data'] = area_checkbox_data

        return context
