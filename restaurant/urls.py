from django.urls import path

from .views import *

app_name = "restaurant"

urlpatterns = [
    path('', RestaurantListView.as_view(), name="restaurant_list"),
    path('<int:pk>/', RetrieveRestaurantView.as_view(), name="restaurant_data_read"),
    path('image/', RestaurantImageListView.as_view(), name="restaurant_image_list"),
]
