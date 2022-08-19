from django.urls import path
from .views import add_product, product_details, search_category, own_products, edit_product

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/<int:id>", product_details, name="product_details"),
    path("/category", search_category, name="search_category"),
    path("/own", own_products, name="own_products"),
    path("/edit/<int:id>", edit_product, name="edit_product")
]