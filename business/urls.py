from django.urls import path

from .views import *

app_name = "business"

urlpatterns = [
    path('', BusinessView.as_view(), name="business_list"),
]
