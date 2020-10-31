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
    path('item/type', views.ItemTypeList.as_view(), name='item_type_list'),
    path('item/area', views.AreaList.as_view(), name='area_list'),
    # case
    path('case', views.CaseList.as_view(), name='case_list'),
    path('case/create', views.CaseCreate.as_view(), name='case_create'),
    path('case/<int:pk>', views.CaseDetail.as_view(), name='case_detail'),
    path('case/<int:pk>/edit', views.CaseUpdate.as_view(), name='case_edit'),

    #
    path('company', views.CompanyInfo.as_view(), name='company'),
    path('company/advantage', views.AdvantageInfo.as_view(), name='advantage'),

    path('sell/flow', views.FlowInfo.as_view(), name='sell_flow'),
    path('sell/question', views.Question.as_view(), name='sell_question'),
    path('sell/price', views.PriceInfo.as_view(), name='sell_price'),
    # user
    path('my_item', views.MyItemList.as_view(), name='my_item_list'),
    path('my_case', views.MyCaseList.as_view(), name='my_case_list'),
    path('item/accept_request', views.AcceptRequest.as_view(), name='accept_request'),
    #
    path('favorite', views.Favorite.as_view(), name='favorite'),
    path('favorite_item', views.FavoriteItemList.as_view(), name='favorite_item_list'),
]
