from django.urls import path

from .views import *

app_name = "restaurant"

urlpatterns = [
    path('public/restaurant/', RestaurantListView.as_view(), name="restaurant_list"),
    path('public/restaurant/<int:pk>/', RetrieveRestaurntView.as_view(), name="restaurant_data_read"),
    path('public/restaurant/image', RestaurantImageListView.as_view(), name="restaurant_image_list"),
]
