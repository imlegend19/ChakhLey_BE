from django.urls import path

from .views import *

app_name = "product"

urlpatterns = [
    path('category/', CategoryListView.as_view(), name="category_list"),
    path('product/', ProductListView.as_view(), name="products_list"),
]
