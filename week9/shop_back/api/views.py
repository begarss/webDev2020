from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from django.http.request import HttpRequest
from api.models import Product
# Create your views here.
def product_list(request):
    products = Product.objects.all()
    product_json = [product.to_json() for product in products]
    return JsonResponse(product_json,safe=False)
def product_details(request,p_id):

    try:
        product = Product.objects.get(id=p_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'Error':str(e)})
    return JsonResponse(product.to_json())
