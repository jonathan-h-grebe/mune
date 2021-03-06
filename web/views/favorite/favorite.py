from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect


class Favorite(View):
    def get(self, request):
        idlist = request.session.get('idlist', list())
        if request.GET.get('id', None):
            id = int(request.GET['id'])
            if not id in idlist:
                idlist.append(id)
                request.session['idlist'] = idlist
                messages.success(request, "お気に入りに追加しました")
            else:
                messages.warning(request, "お気に入りに追加済みです")
        source = request.GET.get("source", None)
        if source == "item_detail":
            return redirect('web:item_detail', pk=id)
        elif source == "item_list" or not source:
            return redirect('web:item_list')
