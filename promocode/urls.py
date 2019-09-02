from django.urls import path

from .views import *

app_name = "promocode"

urlpatterns = [
    path('offer/', OfferView.as_view(), name="offer_list"),
    path('user-promo-code/', UserPromoCodeView.as_view(), name="user_promo_code_list")
]
