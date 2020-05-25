from django.test import TestCase
from django.urls import reverse

from products.models import Product, Category
from products.views import research, product_info


class TestProductsPageTestCase(TestCase):

    def test_research(self):
        response = self.client.get(reverse('research'))
        self.assertEqual(response.status_code, 200)

    def test_product_info(self):
        category = Category.objects.create(
            name = "pâtes à tartiner",
        )
        product = Product.objects.create(
            product_name = "nutella-ferrero",
            code = 3017620429484,
            url = "https://fr.openfoodfacts.org/produit/3017620429484/nutella-ferrero",
            nutrition_grade_fr = "e",
            category = category,
            image_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.full.jpg",
            image_nutrition_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/nutrition_fr.106.200.jpg",
        )

        response = self.client.get(reverse("product_info", kwargs={"code": product.code}))
        self.assertEqual(response.status_code, 200)