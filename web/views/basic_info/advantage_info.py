from django.views.generic import TemplateView


class AdvantageInfo(TemplateView):
    """XXXの強み"""
    template_name = "web/info_advantage.html"
