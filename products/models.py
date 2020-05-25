from django.db import models

from .managers import ProductManager


class Category(models.Model):
    """ Cette class sert à créer le nom de chaque catégories """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """ Cette class sert à créer dans la database les différents éléments qui la composent """
    code = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    nutrition_grade_fr = models.CharField(max_length=3)
    url = models.URLField(max_length=255)
    image_url = models.URLField(max_length=255)
    image_nutrition_url = models.URLField(max_length=255)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.product_name

    objects = ProductManager()