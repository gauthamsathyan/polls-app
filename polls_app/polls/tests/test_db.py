from django.test import Client, TestCase
from django.urls import reverse


def test_database(self):
    response = self.client.get("/polls/")
    assert response.status_code == 200