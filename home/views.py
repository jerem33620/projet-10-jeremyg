from django.shortcuts import render
from django.contrib.auth import login

from products.models import Product, Category
from .forms import SearchForm


def home(request):
    """ Cette méthode sert à utiliser le formulaire pour la page home.html """
    form = SearchForm()
    return render(request, 'home.html', {
        "form":form
    })

def legales_notices(request):
    return render(request, "legales_notices.html")
