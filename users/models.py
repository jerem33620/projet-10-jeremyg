from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from products.models import Product


class User(AbstractUser):
    """ Cette class sert à utiliser AbstractUser pour obtenir tous ce qu'il nous faut pour un utilisateur """
    pass

#class Profile(models.Model):
#    user = models.OneToOneField('auth.User', on_delete=models.cascade)