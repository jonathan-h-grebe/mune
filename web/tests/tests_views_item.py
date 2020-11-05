from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from web.models import *


class ViewsItemTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        u = get_user_model().objects.create_user('HogeTaro3', 'taro@hoge.com', 'password')
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
        self.item_type = ItemType.objects.create(name="item_type")
        self.item = Item.objects.create(
            name="item", item_type=self.item_type,
            height=1, width=1, depth=1, status="作成中",
        )
        # if self.item_type.created_by:
        #     print(self.item_type.created_by.pk)
        # print(self.u.pk)
        self.client.logout()
        # self.client.force_login(user=self.u)

    def test_item_list(self):
        """
        UnitTest for Item List
        """
        url = reverse("web:item_list")
        self.assertEqual(url, "/item")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/item_list.html")

    def test_item_detail(self):
        """
        UnitTest for Item Detail
        """
        url = reverse("web:item_detail", kwargs={"pk": self.item.pk})
        self.assertEqual(url, "/item/{}".format(self.item.pk))
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/item_detail.html")

    def test_item_update(self):
        """
        UnitTest for Item Update
        """
        url = reverse("web:item_edit", kwargs={"pk": self.item.pk})
        self.assertEqual(url, "/item/{}/edit".format(self.item.pk))
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしていればOK
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/item_create.html")
        # updateするunittestも追記したい
        pass

    def test_item_create(self):
        """
        UnitTest for Item Create
        """
        url = reverse("web:item_create")
        self.assertEqual(url, "/item/create")
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしていればOK
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/item_create.html")
        # createするunittestも追記したい
        pass

    def test_item_my_list(self):
        """
        UnitTest for My Item List
        """
        url = reverse("web:my_item_list")
        self.assertEqual(url, "/my_item")
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしていればOK
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/my_item_list.html")

    def test_item_new_list(self):
        """
        UnitTest for New Item List
        """
        url = reverse("web:new_item_list")
        self.assertEqual(url, "/new_info")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/item_list.html")

    def test_item_accept(self):
        """
        UnitTest for Accept Request
        """
        url = reverse("web:accept_request")
        self.assertEqual(url, "/item/accept_request")
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしてもgetはNG
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしてPOSTであればOK。my_item_listにリダイレクトされる＆itemのステータスが更新
        response = self.client.post(url, data={"pk": self.item.pk})
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed("web/my_item_list.html")
        self.item.refresh_from_db()
        self.assertEqual(self.item.status, "承認待ち")
