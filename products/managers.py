from django.db import models
from django.conf import settings


class ProductManager(models.Manager):
    """ Cette class sert à appelé les produits lors de la recherche sur le site """
    def find_products(self, searched_name):

        substitutes = []
        products = self.filter(product_name__icontains=searched_name)
        if products:
            product = products[0]
            substitutes = list(
                self.filter(
                    category=product.category, 
                    nutrition_grade_fr__lt=product.nutrition_grade_fr,
                )[:settings.MAX_RESULT]
            )
            return substitutes, product
        return [], None