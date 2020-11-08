# coding:utf-8
from rest_framework import routers
from accounts.views import CustomUserViewSet, CustomUserViewSet2


router = routers.DefaultRouter()
router.register('user', CustomUserViewSet)
router.register('user2', CustomUserViewSet2)
