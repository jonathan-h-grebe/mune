from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from web.models import *


class ViewsMainPageTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        u = get_user_model().objects.create_user('HogeTaro', 'taro@hoge.com', 'password')
        # print(u.id)

    def setUp(self) -> None:
        """
        Set Up
        各テストメソッド実行時に呼び出されます。
        """
        self.u = get_user_model().objects.first()
        # self.client.force_login(user=self.u)

    def test_main(self):
        """
        UnitTest for Main Page
        """
        url = reverse("web:main")
        self.assertEqual(url, "/")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/main.html")
