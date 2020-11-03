from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse
from web.models import Case


class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    template_name = "web/case_create.html"
    fields = [
        # 'item',
        'case_type', "memo", "item_list",
        "user_name", "mail_address", "tel_number", "company_name", "company_address"
    ]

    def get_success_url(self):
        messages.success(self.request, "問い合わせを更新しました")
        return reverse('web:case_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # form.instance.last_updated_by_id = self.request.user.id
        return super(CaseUpdate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['items'] = self.object.item_list.all()
        return context