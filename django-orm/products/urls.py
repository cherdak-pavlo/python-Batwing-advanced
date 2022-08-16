from django.urls import path
from .views import add_product, product_details, search_category

urlpatterns = [
    path("/add", add_product, name="add_product"),
    path("/<int:id>", product_details, name="product_details"),
    path("/category", search_category, name="search_category")
]