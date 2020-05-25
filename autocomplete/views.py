from django.shortcuts import render
from django.http import JsonResponse

from products.models import Product


def complete(request):
    searched_name_product = request.GET.get("term")
    products = Product.objects.filter(product_name__icontains=searched_name_product).order_by("-nutrition_grade_fr")[:20]
    products = [product.product_name for product in products]

    return JsonResponse(products, safe=False)
