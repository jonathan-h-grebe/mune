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
        request.COOKIES['idlist'] = idlist
        messages.success(request, "お気に入りに追加しました")
        return redirect('web:item_list')
