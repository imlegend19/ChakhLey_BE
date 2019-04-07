from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Category

        model = Category
        fields = ('id', 'name', 'restaurant')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Product

        model = Product
        fields = ('id', 'name', 'category', 'is_veg', 'price')


class UserProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import UserProductRating

        model = UserProductRating
        fields = ('id', 'rating', 'product')


class UserRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import UserRestaurantRating

        model = UserRestaurantRating
        fields = ('id', 'rating', 'restaurant')
