from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from web.models import *
# Create your views here.


class Main(TemplateView):
    """トップページ"""
    template_name = "web/main.html"


class NewInfo(TemplateView):
    """装置を買う＞新着情報"""
    template_name = "web/main.html"


class FlowInfo(TemplateView):
    """装置を売る＞掲載〜契約までの流れ"""
    template_name = "web/info_flow.html"


class PriceInfo(TemplateView):
    """装置を売る＞利用料金"""
    template_name = "web/info_price.html"


class Question(TemplateView):
    """装置を売る＞よくある質問"""
    template_name = "web/info_question.html"


class CompanyInfo(TemplateView):
    """会社情報"""
    template_name = "web/info_company.html"


class AdvantageInfo(TemplateView):
    """XXXの強み"""
    template_name = "web/info_advantage.html"


class ItemList(ListView):
    model = Item
    template_name = "web/item_list.html"

    def get_queryset(self):
        try:
            if self.request.GET:
                params = self.request.GET.copy()
                query = Item.objects.filter(**params.dict())
                return query
            else:
                return super().get_queryset()
        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "web/item_create.html"
    fields = ['name', 'item_type', 'area', "price_type", 'height', "width", "depth", ]

    def get_success_url(self):
        return reverse('web:item_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.created_by_id = self.request.user.id
        # form.instance.last_updated_by_id = self.request.user.id
        return super(ItemCreate, self).form_valid(form)


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "web/item_create.html"
    fields = ['name', 'item_type', 'area', "price_type", 'height', "width", "depth", ]

    def get_success_url(self):
        return reverse('web:item_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.last_updated_by_id = self.request.user.id
        return super(ItemUpdate, self).form_valid(form)


class ItemDetail(DetailView):
    model = Item
    template_name = "web/item_detail.html"


class CaseList(LoginRequiredMixin, ListView):
    model = Case
    template_name = "web/case_list.html"


class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case
    template_name = "web/case_create.html"
    fields = ['item', 'case_type', "memo", ]

    def get_initial(self):
        item = get_object_or_404(Item, pk=self.request.GET.get('item'))
        res = {
            "item": item
        }
        return res

    def get_success_url(self):
        return reverse('web:case_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.created_by_id = self.request.user.id
        # form.instance.last_updated_by_id = self.request.user.id
        return super(CaseCreate, self).form_valid(form)


class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    template_name = "web/case_create.html"
    fields = ['item', 'case_type', "memo", ]

    def get_success_url(self):
        return reverse('web:case_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.last_updated_by_id = self.request.user.id
        return super(CaseUpdate, self).form_valid(form)


class CaseDetail(LoginRequiredMixin, DetailView):
    model = Case
    template_name = "web/case_detail.html"


class ItemTypeList(ListView):
    model = ItemType
    template_name = "web/itemtype_list.html"


class AreaList(ListView):
    model = Area
    template_name = "web/area_list.html"

