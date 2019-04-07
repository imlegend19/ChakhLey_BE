from django.contrib import admin

from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(UserProductRating)
admin.site.register(UserRestaurantRating)
admin.site.register(ProductImage)
