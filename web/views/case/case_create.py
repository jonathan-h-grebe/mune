from django.views.generic import CreateView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from web.models import Case, Item
from web.forms import CaseForm
from django.core.mail import send_mail

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
        messages.success(self.request, "問い合わせを受け付けました")
        if self.request.user.is_authenticated:
            return reverse('web:case_detail', kwargs={'pk': self.object.pk})
        else:
            return reverse('web:views.main')

    def form_valid(self, form):
        res = super(CaseCreate, self).form_valid(form)
        text = "<p>問い合わせを受け付けました</p><br><p>問い合わせ商品：</p>"
        for i, item in enumerate(self.object.item_list.all()):
            text += '<p> {}. {}</p>'.format(i + 1, item.name)
        text += "<p>問い合わせ内容：{}</p>".format(self.object.case_type.name)
        text += "<p>問い合わせ詳細：{}</p>".format(self.object.memo)
        text += "<p>氏名：{}<br>".format(self.object.user_name)
        text += "<p>メールアドレス：{}</p>".format(self.object.mail_address)
        text += "<p>電話番号：{}</p>".format(self.object.tel_number)
        text += "<p>会社名：{}</p>".format(self.object.company_name)
        text += "<p>会社住所：{}</p>".format(self.object.company_address)
        if self.object.mail_address:
            send_mail(
                "【MachineMart】問い合わせを受け付けました",
                text,
                "no-reply@machine-mart.com",
                [self.object.mail_address, ],
                fail_silently=False,
                html_message=text
            )
        return res

    def get(self, request, *args, **kwargs):
        try:
            res = super().get(request, *args, **kwargs)
            return res
        except Exception as e:
            print(e)
            messages.error(request, e)
            return redirect('web:item_list')
