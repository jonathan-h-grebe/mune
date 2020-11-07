from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse
from web.models import Item
from web.forms import ItemForm


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "web/item_create.html"
    # fields = [
    #     'name', 'item_type', 'area', "price_type", 'height', "width", "depth",
    #     "image01", "image02", "image03", "image04", "image05",
    # ]
    form_class = ItemForm

    def get_success_url(self):
        messages.success(self.request, "商品を登録しました")
        return reverse('web:item_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.created_by_id = self.request.user.id
        # form.instance.last_updated_by_id = self.request.user.id
        return super(ItemCreate, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ItemCreate, self).form_invalid(form)