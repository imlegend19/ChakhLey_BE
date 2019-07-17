from django.urls import path

from .views import *

app_name = "location"

urlpatterns = [
    path('country/', CountryView.as_view(), name="country-list-create"),
    path('state/', StateView.as_view(), name="state-list-create"),
    path('city/', CityView.as_view(), name="city-list-create"),
    path('area/', AreaView.as_view(), name="area-list-create"),
    path('complex/', BuildingComplexView.as_view(), name="complex-list-create"),
]
