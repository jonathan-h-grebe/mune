from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from web.models import *


class ViewsSearchByTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        u = get_user_model().objects.create_user('HogeTaro', 'taro@hoge.com', 'password')
        # print(u.id)

    def setUp(self) -> None:
        """
        Set Up
        各テストメソッド実行時に呼び出されます。
        """
        # ログイン処理
        self.u = get_user_model().objects.first()
        res = self.client.login(username=self.u.username, password="password")
        self.client.get("/")
        # データ
        self.area = Area.objects.create(name="area", region="region")
        self.item_type = ItemType.objects.create(name="item_type")
        self.item = Item.objects.create(
            name="item", item_type=self.item_type,
            height=1, width=1, depth=1, status="作成中",
        )
        # self.client.force_login(user=self.u)

    def test_area_list(self):
        """
        UnitTest for Area List
        """
        url = reverse("web:area_list")
        self.assertEqual(url, "/item/area")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/area_list.html")

    def test_item_type_list(self):
        """
        UnitTest for Item Type List
        """
        url = reverse("web:item_type_list")
        self.assertEqual(url, "/item/type")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/itemtype_list.html")