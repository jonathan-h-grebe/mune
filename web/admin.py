from django.contrib import admin
from web.models import *
# Register your models here.

#
# class ItemAdmin(admin.ModelAdmin):
#     list_display = ["__all__"]
#
#
# class CaseAdmin(admin.ModelAdmin):
#     list_display = ["__all__"]

admin.site.register(Area)
admin.site.register(ItemType)
admin.site.register(CaseType)
admin.site.register(Item)
admin.site.register(Case)