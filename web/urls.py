# coding:utf-8
# from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from web.views.main_page import main_page
from web.views.question import question
from web.views.basic_info import flow_info, advantage_info, company_info, price_info 
from web.views.case import case_create, case_detail, case_list, case_my_list, case_update
from web.views.item import item_accept, item_create, item_detail, item_list, item_my_list, item_new_list, item_update
from web.views.search_by import area_list, item_type_list
from web.views.favorite import favorite, favorite_list
from web.views.restframework.views_restframework import ItemViewSet, CaseViewSet


app_name = 'web'
urlpatterns = [
    # dashboard
    path('', main_page.Main.as_view(), name='main'),
    path('sell/question', question.Question.as_view(), name='sell_question'),

    # basic/static info
    path('sell/flow', flow_info.FlowInfo.as_view(), name='sell_flow'),
    path('sell/price', price_info.PriceInfo.as_view(), name='sell_price'),
    path('company/advantage', advantage_info.AdvantageInfo.as_view(), name='advantage'),
    path('company', company_info.CompanyInfo.as_view(), name='company'),

    # case
    path('case', case_list.CaseList.as_view(), name='case_list'),
    path('case/create', case_create.CaseCreate.as_view(), name='case_create'),
    path('case/<int:pk>', case_detail.CaseDetail.as_view(), name='case_detail'),
    path('case/<int:pk>/edit', case_update.CaseUpdate.as_view(), name='case_edit'),
    path('my_case', case_my_list.CaseMyList.as_view(), name='my_case_list'),
   
    # item  
    path('item', item_list.ItemList.as_view(), name='item_list'),
    path('my_item', item_my_list.MyItemList.as_view(), name='my_item_list'),
    path('new_info', item_new_list.NewItemList.as_view(), name='new_item_list'),
    path('item/create', item_create.ItemCreate.as_view(), name='item_create'),
    path('item/<int:pk>', item_detail.ItemDetail.as_view(), name='item_detail'),
    path('item/<int:pk>/edit', item_update.ItemUpdate.as_view(), name='item_edit'),
    path('item/accept_request', item_accept.AcceptRequest.as_view(), name='accept_request'),

    # search by
    path('item/area', area_list.AreaList.as_view(), name='area_list'),
    path('item/type', item_type_list.ItemTypeList.as_view(), name='item_type_list'),
 
    # favorite
    path('favorite', favorite.Favorite.as_view(), name='favorite'),
    path('favorite_item', favorite_list.FavoriteItemList.as_view(), name='favorite_item_list'),
]


router = routers.DefaultRouter()
router.register('item', ItemViewSet)
router.register('case', CaseViewSet)
