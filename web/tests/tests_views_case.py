from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from web.models import *


class ViewsCaseTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        u = get_user_model().objects.create_user('HogeTaro1', 'taro@hoge.com', 'password')
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
        self.case_type = CaseType.objects.create(name="case_type")
        self.case = Case.objects.create(case_type=self.case_type)
        self.case.item_list.add(self.item)
        self.case.save()
        # if self.item_type.created_by:
        #     print(self.item_type.created_by.pk)
        # print(self.u.pk)
        self.client.logout()
        # self.client.force_login(user=self.u)

    def test_case_list(self):
        """
        UnitTest for Case List
        """
        url = reverse("web:case_list")
        self.assertEqual(url, "/case")
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしていればOK
        # self.client.force_login(user=self.u)
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/case_list.html")

    def test_case_detail(self):
        """
        UnitTest for Case Detail
        """
        url = reverse("web:case_detail", kwargs={"pk": self.case.pk})
        self.assertEqual(url, "/case/{}".format(self.case.pk))
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしていればOK
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/case_detail.html")

    def test_case_update(self):
        """
        UnitTest for Case Update
        """
        url = reverse("web:case_edit", kwargs={"pk": self.case.pk})
        self.assertEqual(url, "/case/{}/edit".format(self.case.pk))
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしていればOK
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/case_create.html")
        # updateするunittestも追記したい
        pass

    def test_case_create(self):
        """
        UnitTest for Case Create
        """
        url = reverse("web:case_create")
        self.assertEqual(url, "/case/create")
        # loginしていなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/case_create.html")
        # createするunittestも追記したい
        pass

    def test_case_my_list(self):
        """
        UnitTest for My Case List
        """
        url = reverse("web:my_case_list")
        self.assertEqual(url, "/my_case")
        # loginしていないとリダイレクトされる
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        # loginしていればOK
        self.client.login(username=self.u.username, password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/my_case_list.html")


