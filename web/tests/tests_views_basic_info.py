from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from web.models import *


class ViewsBasicInfoTest(TestCase):

    def setUp(self) -> None:
        """
        Set Up
        各テストメソッド実行時に呼び出されます。
        """
        self.u = get_user_model().objects.create_user('HogeTaro', 'taro@hoge.com', 'password')
        # self.client.force_login(user=self.u)

    def test_advantage(self):
        """
        UnitTest for Advantage Page
        """
        url = reverse("web:advantage")
        self.assertEqual(url, "/company/advantage")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/info_advantage.html")

    def test_company(self):
        """
        UnitTest for Company Page
        """
        url = reverse("web:company")
        self.assertEqual(url, "/company")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/info_company.html")

    def test_flow(self):
        """
        UnitTest for Flow Page
        """
        url = reverse("web:sell_flow")
        self.assertEqual(url, "/sell/flow")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/info_flow.html")

    def test_price(self):
        """
        UnitTest for Main Page
        """
        url = reverse("web:sell_price")
        self.assertEqual(url, "/sell/price")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/info_price.html")
