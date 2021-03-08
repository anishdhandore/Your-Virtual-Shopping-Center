from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "shop/index.html")

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



    