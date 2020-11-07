from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib import messages
from django.urls import reverse
from web.models import Item
from web.forms import ItemForm


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "web/item_create.html"
    # fields = [
    #     'name', 'item_type', 'area', "price_type", 'height', "width", "depth",
    #     "image01", "image02", "image03", "image04", "image05",
    # ]
    form_class = ItemForm

    def get_success_url(self):
        messages.success(self.request, "商品を更新しました")
        return reverse('web:item_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.last_updated_by_id = self.request.user.id
        return super(ItemUpdate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ItemUpdate, self).form_invalid(form)