from django.test import TestCase
from django.urls import reverse

from products.models import Category, Product


class TestProductsCategoryPage(TestCase):

    def product_test(self):
        category = Category.objects.create(name="pâte à tartiner")
        product = Product.objects.create(
            code = 3017620429484, 
            product_name = "nutella-ferrero", 
            nutrition_grade_fr = "e", 
            url = "https://fr.openfoodfacts.org/produit/3017620429484/nutella-ferrero", 
            image_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.full.jpg", 
            image_nutrition_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/nutrition_fr.106.200.jpg", 
            category = category
        )
        return Product.objects.create(product=product, category=category)

        self.assertEqual(product.code, 3017620429484)
        self.assertEqual(product.product_name, "nutella-ferrero")
        self.assertEqual(product.nutrition_grade_fr, "e")
        self.assertEqual(product.url, "https://fr.openfoodfacts.org/produit/3017620429484/nutella-ferrero")
        self.assertEqual(product.image_url, "https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.full.jpg")
        self.assertEqual(product.image_nutrition_url, "https://static.openfoodfacts.org/images/products/301/762/042/9484/nutrition_fr.106.200.jpg")
        self.assertEqual(product.category, category)
        