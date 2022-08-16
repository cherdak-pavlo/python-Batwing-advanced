from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


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
        products = Product.objects.filter(display_on_main_page=True, approved=True, category__category_name=request.POST.get("category")).order_by("-id")
        return render(request, "products/search_category.html", {"products": products})