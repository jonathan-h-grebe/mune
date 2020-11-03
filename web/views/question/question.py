from django.views.generic import TemplateView

class Question(TemplateView):
    """装置を売る＞よくある質問"""
    template_name = "web/info_question.html"