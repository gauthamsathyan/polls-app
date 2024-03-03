from django.test import Client, TestCase
from django.urls import reverse


class TestIndex(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("index"))
        assert response.status_code == 200
        self.assertTemplateUsed(response, "polls.html")
