from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from web.models import *


class ViewsQuestionTest(TestCase):

    def setUp(self) -> None:
        """
        Set Up
        各テストメソッド実行時に呼び出されます。
        """
        self.u = get_user_model().objects.create_user('HogeTaro', 'taro@hoge.com', 'password')
        # self.client.force_login(user=self.u)

    def test_question(self):
        """
        UnitTest for Question Page
        """
        url = reverse("web:sell_question")
        self.assertEqual(url, "/sell/question")
        # loginしてなくてもOK
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("web/info_question.html")
