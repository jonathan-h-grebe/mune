from django.views.generic import ListView
from web.models import Area

class AreaList(ListView):
    model = Area
    template_name = "web/area_list.html"
