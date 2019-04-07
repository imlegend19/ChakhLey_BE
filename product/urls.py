from django.urls import path

from .views import *

app_name = "product"

urlpatterns = [
    path('category/', CategoryListView.as_view(), name="category_list"),
    path('product/', ProductListView.as_view(), name="products_list"),
    path('product_rating/', UserProductRatingListView.as_view(), name="product_rating"),
    path('restaurant_rating/', UserRestaurantRatingListView.as_view(), name="restaurant_rating"),
]
