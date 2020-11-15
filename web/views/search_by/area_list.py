from django.views.generic import ListView
from django.contrib import messages
from web.models import Area
from django.db.models import Q

class AreaList(ListView):
    model = Area
    template_name = "web/area_list.html"
