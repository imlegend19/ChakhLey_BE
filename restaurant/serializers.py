from rest_framework import serializers

from business.serializers import BusinessSerializer
from location.serializers import AreaSerializer


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import RestaurantImage

        model = RestaurantImage
        fields = ('id', 'image_type', 'restaurant', 'image')


class RestaurantSerializer(serializers.ModelSerializer):
    business_id = serializers.IntegerField(source='business.id')

    class Meta:
        from .models import Restaurant

        model = Restaurant
        fields = ('id', 'name', 'is_active', 'business_id',
                  'cost_for_two', 'delivery_time', 'cuisine', 'full_address',
                  'is_veg', 'open', 'category_count', 'discount', 'images',
                  'packaging_charge', 'gst', 'ribbon')


class RestaurantAnalysis(serializers.ModelSerializer):
    class Meta:
        from .models import Restaurant

        model = Restaurant
        fields = ('id', 'name', 'total_income', 'total_orders', 'orders_today', 'income_today', 'commission',
                  'most_liked_product', 'top_10_products', 'income_month', 'orders_month', 'amount_after_commission')
