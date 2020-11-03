from django.views.generic import TemplateView

class CompanyInfo(TemplateView):
    """会社情報"""
    template_name = "web/info_company.html"
