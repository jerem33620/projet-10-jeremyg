from django.test import TestCase
from django.urls import reverse

from autocomplete.views import complete


class AutocompletionTestViews(TestCase):
    
    def test_autocompletion_page(self):
        response = self.client.get(reverse("autocomplete:complete"), {"term": "nutella"})
        self.assertEqual(response.status_code, 200)