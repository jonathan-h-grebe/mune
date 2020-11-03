from django.views.generic import TemplateView

class FlowInfo(TemplateView):
    """装置を売る＞掲載〜契約までの流れ"""
    template_name = "web/info_flow.html"