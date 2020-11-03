from django.views.generic import TemplateView

class PriceInfo(TemplateView):
    """装置を売る＞利用料金"""
    template_name = "web/info_price.html"
