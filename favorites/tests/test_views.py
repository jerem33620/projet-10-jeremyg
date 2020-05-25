from django.test import TestCase
from django.urls import reverse

from users.models import User
from favorites.models import Favorite
from products.models import Category, Product
from favorites.views import favorite_list, favorite_save


class TestFavoritesPageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="blabla1", password="Viveme01", email="jeremyguy@orange.fr")
        category = Category.objects.create(
            name = "pâtes à tartiner",
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

    def test_favorite_list_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('favorite_list'))
        self.assertEqual(response.status_code, 200)

    def test_favorite_save_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('favorite_save'), follow=True)
        self.assertTemplateUsed("home.html")

    def test_favorite_save_page_post(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('favorite_save'), data={"product-code": "30176204294841", "substitute-code": "8032862870028"})
        favorites = Favorite.objects.all()
        self.assertEqual(len(favorites), 1)

    