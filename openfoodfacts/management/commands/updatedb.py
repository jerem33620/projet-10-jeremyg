from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

import requests

from products.models import Category, Product
from openfoodfacts.utils import get_json


class Command(BaseCommand):
    help = (
        "Télécharge les produits à partir d’Openfoodfacts et les sauvegardes dans la base de données"
    )

    def handle(self, *args, **options):
        """ Cette méthode sert à appelé tous ce qu'il nous faudra pour la DB """
        self.codes=set()
        self.delete_all()
        for category in settings.OPENFOODFACTS_CATEGORIES:
            category, created = self.save_category(
                category
            )  # 0. Sauvegarder la catégories dans le modèle Category
            
            products = get_json(
                category.name
            )  # 1. downloader les produits pour chaque catégorie
            
<<<<<<< HEAD
            
            self.save_products_by_category(
                category, products
            )  # 3. Sauvegarder les produits dans la base
=======
            products = self.clean_products(
                products
            )  # 2. Eliminer les produits pour lesquels il manque des infos

            products = self.update_products(
                products
            )  # 3. Permet d'uploader les produits dans la base de donnée.
            
            self.save_products_by_category(
                category, products
            )  # 4. Sauvegarder les produits dans la base
>>>>>>> 87aa05b8e2cc47a6397e912eb64bf2873043dff3

    def save_category(self, category):
        """ cette méthode sert à sauvegarder dans la DB les catégories """
        return Category.objects.get_or_create(name=category.lower())

    def save_products_by_category(self, category, products):
        """ Cette méthode sert à sauvegarder dans la DB les données vouluent:
            code/product_name/nutrition_grade_fr/url/image_url/image_nutrition_url
        """
        for product in products:
            self.stdout.write(str(product["product_name"]))
            if product["code"] not in self.codes:
                self.codes.add(product["code"])
<<<<<<< HEAD
                Product.objects.get_or_create(
                    code=product["code"],
                    product_name=product["product_name"],
                    category=category,
                    nutrition_grade_fr=product["nutrition_grade_fr"],
                    url=product["url"],
                    image_url=product["image_url"],
                    image_nutrition_url=product["image_nutrition_url"],
                )
=======
                try:
                    myproduct = Product.objects.get(pk=productname["code"])
                except Product.DoesNoExist:
                    continue
                myproduct["product_name"] = productname.get("product_name")
                myproduct["nutrition_grade_fr"] = productname("nutrition_grade_fr")
                myproduct["url"] = productname["url"]
                myproduct["image_url"] = productname["image_url"]
                myproduct["image_nutrition_url"] = productname["image_nutrition_url"]
                myproduct.save()
>>>>>>> 87aa05b8e2cc47a6397e912eb64bf2873043dff3

    def _is_valid(self, product):
        """ Cette méthode sert à vérifier que toutes les infos nécessaires,
            sont présentes dans le dictionnaire product.
        """
        keys = ("code", "product_name", "nutrition_grade_fr",
                "url", "image_url", "image_nutrition_url")
        for key in keys:
            if key not in product or not product[key]:
                return False
        return True

<<<<<<< HEAD
=======
    def clean_products(self, products):
        """ Cette méthode sert à supprimé et vérifier les produits """
        cleaned_products = []

        for product in products:
            if self._is_valid(product):
                cleaned_products.append(product)

        return cleaned_products

>>>>>>> 87aa05b8e2cc47a6397e912eb64bf2873043dff3
    def delete_all(self):
        """ Cette méthode sert à supprimer les tables Product et Category """
        Product.objects.all().delete()
        Category.objects.all().delete()