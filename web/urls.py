# coding:utf-8
# from django.conf.urls import url
from django.urls import include, path
from web import views
from web.views import basic_info
from web.views import search_by
from web.views import case
from web.views import item
from web.views import favorite

app_name = 'web'
urlpatterns = [
    # dashboard
    path('', views.Main.as_view(), name='views.main'),
    path('sell/question', views.Question.as_view(), name='sell_question'),

    # basic/static info
    path('sell/flow', basic_info.flow_info.FlowInfo.as_view(), name='sell_flow'),
    path('sell/price', basic_info.price_info.PriceInfo.as_view(), name='sell_price'),
    path('company/advantage', basic_info.advantage_info.AdvantageInfo.as_view(), name='advantage'),
    path('company', basic_info.CompanyInfo.as_view(), name='company'),

    # case
    path('case', case.CaseList.as_view(), name='case_list'),
    path('case/create', case.CaseCreate.as_view(), name='case_create'),
    path('case/<int:pk>', case.CaseDetail.as_view(), name='case_detail'),
    path('case/<int:pk>/edit', case.CaseUpdate.as_view(), name='case_edit'),
    path('my_case', case.CaseMyList.as_view(), name='my_case_list'),
   
    # item  
    path('item', item.ItemList.as_view(), name='item_list'),
    path('my_item', item.MyItemList.as_view(), name='my_item_list'),
    path('new_info', item.NewItemList.as_view(), name='new_item_list'),
    path('item/create', item.ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>', item.ItemDetail.as_view(), name='item_detail'),
    path('item/<int:pk>/edit', item.ItemUpdate.as_view(), name='item_edit'),
    path('item/accept_request', item.AcceptRequest.as_view(), name='accept_request'),

    # search by
    path('item/area', search_by.AreaList.as_view(), name='area_list'),
    path('item/type', search_by.ItemTypeList.as_view(), name='item_type_list'),
 
    # favorite
    path('favorite', favorite.Favorite.as_view(), name='favorite'),
    path('favorite_item', favorite.FavoriteItemList.as_view(), name='favorite_item_list'),
]
