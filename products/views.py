from django.shortcuts import render

from home.forms import SearchForm
from .models import Product, Category


def research(request):
    """ Cette méthode sert à créer la requête en GET pour obtenir des substitues  """
    substitutes = []
    product = None
    form = SearchForm()
    if request.method == "GET":
        research_form = SearchForm(request.GET or None)
        if research_form.is_valid():
            search_name = research_form.cleaned_data["product"]
            substitutes, product = Product.objects.find_products(search_name)
            if product: 
                product.image_url = product.image_url.replace("400", "full")
    return render(request, "research.html", {"substitutes": substitutes, "product": product, "form": form})

def product_info(request, code):
    form = SearchForm()
    product = Product.objects.get(code=code)
    product.image_url = product.image_url.replace("400", "full")
    return render(request, "product_info.html", {
        "product": product, "form": form,
    })
