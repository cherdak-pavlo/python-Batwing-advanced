from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add.html")
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})


def search_category(request):
    if request.method == "GET":
        return render(request, "products/search_category.html")
    else:
        products = Product.objects.filter(display_on_main_page=True, approved=True,
                                          category__category_name=request.POST.get("category")).order_by("-id")
        return render(request, "products/search_category.html", {"products": products})


def own_products(request):
    if request.user.is_authenticated:
        name = User.objects.get(username=request.user)
        products = Product.objects.filter(user=name).order_by("-id")
        return render(request, "products/own_products.html", {"products": products})
    else:
        return redirect("/")


def edit_product(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=id)
        if product.user == User.objects.get(username=request.user):
            if request.method == "POST":
                product.title = request.POST.get("title")
                product.description = request.POST.get("description")
                product.save()
                return own_products(request)
            else:
                return render(request, "products/edit_product.html", {"product": product})
        else:
            return HttpResponseNotFound("Query does not exist")
    else:
        return redirect("/")
