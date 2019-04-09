from django.contrib import admin

from user_rating.models import UserProductRating, UserRestaurantRating

admin.site.register(UserProductRating)
admin.site.register(UserRestaurantRating)
