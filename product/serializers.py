from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Category

        model = Category
        fields = ('id', 'name', 'restaurant', 'active', 'product_count', 'products', 'combos')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Product

        model = Product
        fields = ('id', 'name', 'category', 'is_veg', 'price', 'discount', 'restaurant', 'active',
                  'recommended_product', 'image', 'display_price')


class ProductOrderSerializer(serializers.ModelSerializer):

    class Meta:
        from .models import Product

        model = Product
        fields = ('id', 'name', 'is_veg', 'price', 'discount', 'active', 'display_price')
