from django.db import models
from django.conf import settings

from users.models import User
from products.models import Product


class Favorite(models.Model):
    """ Cette class sert à avoir une table de favoris pour enregistrer
        les utilisateurs, les produits recherchés et les substitues trouvés
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="favorites_as_product"
    )
    substitute = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="favorites_as_substitute"
    )
    
    def __str__(self):
        return self.substitute.product_name