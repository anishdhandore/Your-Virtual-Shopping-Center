from django.shortcuts import render, HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    slides = n//4 + 1

    # parameters = {'no_of_slides': slides, 'range': range(1, slides), 'product': products}
    allProducts = [[products, range(1, slides), slides], [products, range(1, slides), slides]]
    parameters = {'allProducts': allProducts}
    return render(request, "shop/index.html", context=parameters)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    return HttpResponse("Contact page")

def search(request):
    return HttpResponse("Search page")

def products(request):
    return HttpResponse("Products page")

def tracker(request):
    return HttpResponse("Tracker page")

def checkout(request):
    return HttpResponse("Checkout page")



    