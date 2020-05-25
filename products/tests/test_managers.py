from django.test import TestCase
from django.urls import reverse
from django import forms

from home.forms import SearchForm
from products.models import Product, Category
from products.managers import ProductManager


class TestManagersPageTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(
            name = "pâtes à tartiner",
        )

        category_2 = Category.objects.create(
            name = "pizza",
        )

        self.product_a = Product.objects.create(
            code = 30176204294841,
            product_name = "nutella-ferrero",
            nutrition_grade_fr = "e",
            url = "https://fr.openfoodfacts.org/produit/3017620429484/nutella-ferrero",
            image_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.full.jpg",
            image_nutrition_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/nutrition_fr.106.200.jpg",
            category = category,
        )

        self.product_b = Product.objects.create(
            code = 8032862870028,
            product_name = "gonuts-dailylife",
            nutrition_grade_fr = "b",
            url = "https://fr.openfoodfacts.org/produit/8032862870028/gonuts-dailylife",
            image_url = "https://static.openfoodfacts.org/images/products/803/286/287/0028/front_fr.4.200.full.jpg",
            image_nutrition_url = "https://static.openfoodfacts.org/images/products/803/286/287/0028/nutrition_fr.10.200.jpg",
            category = category,
        )

        self.product_c = Product.objects.create(
            code = 8032862870024,
            product_name = "pizza 4 fromages",
            nutrition_grade_fr = "a",
            url = "https://fr.openfoodfacts.org/produit/8032862870028/gonuts-dailylife",
            image_url = "https://static.openfoodfacts.org/images/products/803/286/287/0024/front_fr.4.200.full.jpg",
            image_nutrition_url = "https://static.openfoodfacts.org/images/products/803/286/287/0024/nutrition_fr.10.200.jpg",
            category = category_2,
        )

    def test_find_product_find_no_product(self):
        products, product = Product.objects.find_products("gonuts-dailylife")

        self.assertEqual(len(products), 0)
        self.assertEqual(product, self.product_b)

    def test_find_products_find_a_product(self):
        products, product = Product.objects.find_products("nutella-ferrero")

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0], self.product_b)
        self.assertEqual(product, self.product_a)