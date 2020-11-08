from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView
from web.models import Case


class CaseMyList(LoginRequiredMixin, ListView):
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