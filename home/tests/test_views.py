from django.test import TestCase
from django.urls import reverse

from home import views


class TestIndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class TestIndexPageTestCase(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('legales_notices'))
        self.assertEqual(response.status_code, 200)