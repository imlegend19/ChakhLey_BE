from rest_framework import serializers

from restaurant.serializers import RestaurantSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Category

        model = Category
        fields = ('id', 'name', 'restaurant')


class ProductSerializer(serializers.ModelSerializer):

    restaurant = RestaurantSerializer(many=False, read_only=True)

    class Meta:
        from .models import Product

        model = Product
        fields = ('id', 'name', 'category', 'is_veg', 'price', 'restaurant')
