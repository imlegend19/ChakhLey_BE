from django.urls import path

from .views import *

app_name = "product"

urlpatterns = [
    path('category/', CategoryListView.as_view(), name="category-list"),
    path('category/<int:pk>/', CategoryUpdateDestroyView.as_view(), name="category-update-destroy"),
    path('product/', ProductListView.as_view(), name="products-list"),
    path('product/<int:pk>/', ProductUpdateDestroyView.as_view(), name="product-update-destroy")
]
