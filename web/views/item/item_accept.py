from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from web.models import Item


class AcceptRequest(LoginRequiredMixin, View):

    def get(self, request):
        messages.warning(self.request, "許可されていない操作です")
        return redirect('web:my_item_list')

    def post(self, request, *args, **kwargs):
        try:
            item = Item.objects.get(pk=request.POST['pk'])
            if item.status == "作成中":
                item.status = "承認待ち"
                item.save()
                messages.success(self.request, "承認依頼を発出しました。")
            else:
                messages.warning(self.request, "承認依頼対象外です。")
        except Exception as e:
            print(e)
            messages.error(self.request, e)
        finally:
            return redirect('web:my_item_list')