from django.urls import path

from .views import *

app_name = "business"

urlpatterns = [
    path('business/', BusinessView.as_view(), name="business_list"),
    path('delivery-boys/', DeliveryBoysViews.as_view(), name="delivery_boys_list"),
    path('manager/', ManagerViews.as_view(), name="managers_list"),
]
