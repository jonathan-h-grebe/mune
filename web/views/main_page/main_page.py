from django.views.generic import TemplateView

class Main(TemplateView):
    """トップページ"""
    template_name = "web/main.html"