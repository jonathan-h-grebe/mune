# coding:utf-8
# from django.conf.urls import url
from django.urls import include, path
from web import views


app_name = 'web'
urlpatterns = [
    # dashboard
    path('', views.Main.as_view(), name='main'),
    # item
    path('item', views.ItemList.as_view(), name='item_list'),
    path('item/create', views.ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
    path('item/<int:pk>/edit', views.ItemUpdate.as_view(), name='item_edit'),
    # case
    path('case', views.CaseList.as_view(), name='case_list'),
    path('case/create', views.CaseCreate.as_view(), name='case_create'),
    path('case/<int:pk>', views.CaseDetail.as_view(), name='case_detail'),
    path('case/<int:pk>/edit', views.CaseUpdate.as_view(), name='case_edit'),
    # item type
    path('item/type', views.ItemTypeList.as_view(), name='item_type_list'),
    #
    path('company', views.CompanyInfo.as_view(), name='company'),
    path('company/advantage', views.AdvantageInfo.as_view(), name='advantage'),
    path('buy/new', views.NewInfo.as_view(), name='buy_new'),
    path('sell/flow', views.FlowInfo.as_view(), name='sell_flow'),
    path('sell/question', views.Question.as_view(), name='sell_question'),
    path('sell/price', views.PriceInfo.as_view(), name='sell_price'),
]
