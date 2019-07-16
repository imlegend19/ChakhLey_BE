from django.urls import path

from .views import *

app_name = "business"

urlpatterns = [
    path('business/', BusinessView.as_view(), name="business_list"),
]
