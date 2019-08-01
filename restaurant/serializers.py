from rest_framework import serializers

from business.serializers import BusinessSerializer
from location.serializers import AreaSerializer


class RestaurantImageSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import RestaurantImage

        model = RestaurantImage
        fields = ('id', 'image_type', 'restaurant', 'image')


class RestaurantSerializer(serializers.ModelSerializer):
    area = AreaSerializer(many=False, read_only=True)
    business = BusinessSerializer(many=False, read_only=True)

    class Meta:
        from .models import Restaurant

        model = Restaurant
        fields = ('id', 'name', 'area', 'unit', 'phone', 'business', 'email', 'website', 'is_active',
                  'cost_for_two', 'establishment', 'delivery_time', 'latitude', 'longitude', 'cuisine',
                  'is_veg', 'full_address', 'commission', 'open', 'category_count', 'discount', 'images')
