from django.test import Client, TestCase
from django.urls import reverse

class TestIndex:
    def setUp(self):
        self.client = Client()

    def test_index(self):
        # Write a unit test to test a get requet on the index endpoint
        # Use a django client test as in this tutorial https://docs.djangoproject.com/en/5.0/intro/tutorial05/#:~:text=%3E%3E%3E%20from%20django.test%20import%20Client%0A%3E%3E%3E%20%23%20create%20an%20instance%20of%20the%20client%20for%20our%20use%0A%3E%3E%3E%20client%20%3D%20Client()
        # You should assert that your response is as expected and the status code is as expected.
        # e.g. assert resp.status_code == 200
        # assert resp.json() == expected_response
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls.html')