from django.views.generic import TemplateView
from web.models import Item


class FavoriteItemList(TemplateView):
    template_name = "web/favorite_item_list.html"

    def get_context_data(self, **kwargs):
        idlist = self.request.session.get('idlist', list())
        context = {
            'object_list': Item.objects.filter(id__in=idlist),
        }
        return context

