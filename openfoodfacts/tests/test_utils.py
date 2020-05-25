from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

from openfoodfacts.utils import get_json
import requests
import json


class TestUtils(TestCase):

    @patch("requests.get")
    def test_utils(self, Mockget):
        Mockget.return_value.json.return_value = {
            "products": [
                {
                    "code": 30176204294841,
                    "product_name": "nutella-ferrero",
                    "nutrition_grade_fr": "e",
                    "url": "https://fr.openfoodfacts.org/produit/3017620429484/nutella-ferrero",
                    "image_url": "https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.full.jpg",
                    "image_nutrition_url": "https://static.openfoodfacts.org/images/products/301/762/042/9484/nutrition_fr.106.200.jpg",
                },
                {
                    "code": 8032862870028,
                    "product_name": "gonuts-dailylife",
                    "nutrition_grade_fr": "b",
                    "url": "https://fr.openfoodfacts.org/produit/8032862870028/gonuts-dailylife",
                    "image_url": "https://static.openfoodfacts.org/images/products/803/286/287/0028/front_fr.4.200.full.jpg",
                    "image_nutrition_url": "https://static.openfoodfacts.org/images/products/803/286/287/0028/nutrition_fr.10.200.jpg",
                },
            ]
        }
        Mockget.return_value.status_code = 200
        util = get_json("category")

        self.assertEqual(len(util), 2)
        
        Mockget.return_value.status_code = 404