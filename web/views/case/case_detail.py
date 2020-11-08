from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from web.models import Case


class CaseDetail(LoginRequiredMixin, DetailView):
    model = Case
    template_name = "web/case_detail.html"