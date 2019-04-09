from django.urls import path

from .views import *

app_name = "user rating"

urlpatterns = [
    path('product_rating/', UserProductRatingListView.as_view(), name="product_rating"),
    path('restaurant_rating/', UserRestaurantRatingListView.as_view(), name="restaurant_rating"),
]
