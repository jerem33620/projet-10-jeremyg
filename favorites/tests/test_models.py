from django.test import TestCase
from django.urls import reverse

from favorites.models import Favorite
from users.models import User
from products.models import Product, Category


class TestModelFavoritePage(TestCase):

    def create_test_favorite(self, user=User, product="nutella-ferrero", substitute="gonuts-dailylife"):
        category = Category.objects.create(name="pâte à tartiner")
        product = Product.objects.create(
            code = 30176204294841, 
            product_name = "nutella-ferrero", 
            nutrition_grade_fr = "e", 
            url = "https://fr.openfoodfacts.org/produit/3017620429484/nutella-ferrero", 
            image_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/front_fr.204.full.jpg", 
            image_nutrition_url = "https://static.openfoodfacts.org/images/products/301/762/042/9484/nutrition_fr.106.200.jpg", 
            category = category,
        )
        substitute = Product.objects.create(
            code = 8032862870028, 
            product_name = "gonuts-dailylife", 
            nutrition_grade_fr = "b", 
            url = "https://fr.openfoodfacts.org/produit/8032862870028/gonuts-dailylife", 
            image_url = "https://static.openfoodfacts.org/images/products/803/286/287/0028/front_fr.4.200.full.jpg", 
            image_nutrition_url = "https://static.openfoodfacts.org/images/products/803/286/287/0028/nutrition_fr.10.200.jpg", 
            category = category,
        )
        user = User.objects.create_user(
            username = "blabla1", 
            password = "blabla", 
            email = "jeremy@orange.fr"
        )
        return Favorite.objects.create(
            user = user, 
            product = product, 
            substitute = substitute
        ), user, product, substitute

    def test_favorite_creation(self):
        w, user, product, substitute =  self.create_test_favorite()
        self.assertTrue(isinstance(w, Favorite))
        self.assertEqual(w.user, user)