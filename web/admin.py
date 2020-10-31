from django.contrib import admin
from web.models import *
from web.forms import *
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ("pk", "name", "item_type", "status", "last_updated_at", "last_updated_by")
    readonly_fields = ("created_by", "created_at", "last_updated_by", "last_updated_at")
    list_filter = ["status"]


class CaseAdmin(admin.ModelAdmin):
    list_display = ("pk", "case_type", "memo", "last_updated_at", "last_updated_by")
    readonly_fields = ("created_by", "created_at", "last_updated_by", "last_updated_at")


admin.site.register(Area)
admin.site.register(ItemType)
admin.site.register(CaseType)
admin.site.register(Item, ItemAdmin)
admin.site.register(Case, CaseAdmin)