from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.forms import ModelForm
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_restaurant')
    list_filter = ('category', 'category__restaurant', ('is_veg', admin.BooleanFieldListFilter))

    def get_restaurant(self, obj):
        return obj.category.restaurant

    get_restaurant.short_description = 'Restaurant'
    get_restaurant.admin_order_field = 'category__restaurant'


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductCombo)
