from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("products/", views.products, name="products"),
    path("tracker/", views.tracker, name="tracker"),
    path("checkout/", views.checkout, name="checkout"),
]
