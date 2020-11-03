from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from web.models import Case
class CaseList(LoginRequiredMixin, ListView):
    model = Case
    template_name = "web/case_list.html"
