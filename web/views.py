from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.views.generic import FormView, RedirectView, View
from django.urls import reverse
from django.shortcuts import get_object_or_404
from web.models import *
from web.forms import *
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
            query = Item.objects.exclude(status__in=("作成中", "承認待ち", "取り下げ"))
            if self.request.GET:
                params = self.request.GET.copy()
                query = query.filter(**params.dict())
                return query
            else:
                return query
        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    template_name = "web/item_create.html"
    fields = [
        'name', 'item_type', 'area', "price_type", 'height', "width", "depth",
        "image01",
    ]

    def get_success_url(self):
        return reverse('web:item_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.created_by_id = self.request.user.id
        # form.instance.last_updated_by_id = self.request.user.id
        return super(ItemCreate, self).form_valid(form)


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "web/item_create.html"
    fields = [
        'name', 'item_type', 'area', "price_type", 'height', "width", "depth",
        "image01",
    ]

    def get_success_url(self):
        return reverse('web:item_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.last_updated_by_id = self.request.user.id
        return super(ItemUpdate, self).form_valid(form)


class ItemDetail(DetailView):
    model = Item
    template_name = "web/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class CaseList(LoginRequiredMixin, ListView):
    model = Case
    template_name = "web/case_list.html"


class CaseCreate(CreateView):
    model = Case
    form_class = CaseForm
    template_name = "web/case_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        item_list = self.request.GET.getlist("item_list", [])
        status_list = ("商談中", "承認済み")
        context['items'] = Item.objects.filter(id__in=item_list, status__in=status_list)
        return context

    def get_initial(self):
        item_list = self.request.GET.getlist("item_list", [])
        res = {
            "item": None,
            "item_list": list(),
        }
        for i in item_list:
            item = get_object_or_404(Item, pk=i)
            res["item_list"].append(item)

        if self.request.user.is_authenticated:
            res["user_name"] = "{} {}".format(self.request.user.last_name, self.request.user.first_name)
            res["mail_address"] = self.request.user.email
            res["tel_number"] = self.request.user.tel_number
            res["company_name"] = self.request.user.company_name
            res["company_address"] = self.request.user.company_address
        return res

    def get_success_url(self):
        return reverse('web:case_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.created_by_id = self.request.user.id
        # form.instance.last_updated_by_id = self.request.user.id
        return super(CaseCreate, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            print(e)
            messages.error(request, e)
            return redirect('web:item_list')


class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    template_name = "web/case_create.html"
    fields = [
        # 'item',
        'case_type', "memo", "item_list",
        "user_name", "mail_address", "tel_number", "company_name", "company_address"
    ]

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


class MyItemList(LoginRequiredMixin, ListView):
    model = Item
    template_name = "web/my_item_list.html"

    def get_queryset(self):
        try:
            query = Item.objects.filter(created_by=self.request.user)
            if self.request.GET:
                params = self.request.GET.copy()
                query = query.filter(**params.dict())
                return query
            else:
                return query
        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()


class MyCaseList(LoginRequiredMixin, ListView):
    model = Case
    template_name = "web/my_case_list.html"

    def get_queryset(self):
        try:
            query = Case.objects.filter(created_by=self.request.user)
            if self.request.GET:
                params = self.request.GET.copy()
                query = query.filter(**params.dict())
                return query
            else:
                return query
        except Exception as e:
            messages.error(self.request, e)
            return super().get_queryset()


class AcceptRequest(LoginRequiredMixin, View):

    def get(self, request):
        messages.warning(self.request, "許可されていない操作です")
        return redirect('web:my_item_list')

    def post(self, request, *args, **kwargs):
        try:
            item = Item.objects.get(pk=request.POST['pk'])
            if item.status == "作成中":
                item.status = "承認待ち"
                item.save()
                messages.success(self.request, "承認依頼を発出しました。2")
            else:
                messages.warning(self.request, "承認依頼対象外です。")
        except Exception as e:
            print(e)
            messages.error(self.request, e)
        finally:
            return redirect('web:my_item_list')


class Favorite(View):
    def get(self, request):
        idlist = request.session.get('idlist', list())
        if request.GET.get('id', None):
            id = int(request.GET['id'])
            if not id in idlist:
                idlist.append(id)
        request.session['idlist'] = idlist
        request.COOKIES['idlist'] = idlist
        messages.info(request, "{}".format(request.session['idlist']))
        return redirect('web:item_list')


class FavoriteItemList(TemplateView):
    template_name = "web/favorite_item_list.html"

    def get_context_data(self, **kwargs):
        idlist = self.request.session.get('idlist', list())
        context = {
            'object_list': Item.objects.filter(id__in=idlist),
        }
        return context