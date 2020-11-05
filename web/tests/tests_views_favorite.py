from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from web.models import *
from django_currentuser.middleware import get_current_authenticated_user


class ViewsFavoriteTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        u = get_user_model().objects.create_user('HogeTaro2', 'taro@hoge.com', 'password')
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
        self.item_type = ItemType.objects.create(name="item_type", created_by=self.u)
        self.item = Item.objects.create(
            name="item", item_type=self.item_type,
            height=1, width=1, depth=1, status="作成中",
        )
        # if self.item_type.created_by:
        #     print(self.item_type.created_by.pk)
        # print(self.u.pk)
        self.client.logout()
        # self.client.force_login(user=self.u)

    def test_favorite(self):
        """
        UnitTest for Favorite
        """
        url = reverse("web:favorite")
        self.assertEqual(url, "/favorite")
        # loginしてなくてもOK
        response = self.client.get("{}?id={}".format(url, self.item.pk))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['idlist'], [self.item.pk])

    def test_favorite_item_list(self):
        """
        UnitTest for Favorite List
        """
        url = reverse("web:favorite_item_list")
        self.assertEqual(url, "/favorite_item")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/favorite_item_list.html")

