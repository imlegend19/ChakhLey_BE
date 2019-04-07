from rest_framework import serializers

from location.serializers import CountrySerializer, StateSerializer, AreaSerializer


class RestaurantSerializer(serializers.ModelSerializer):
    area = AreaSerializer(many=False, read_only=True)

    class Meta:
        from .models import Restaurant

        model = Restaurant
        fields = ('id', 'name', 'pincode', 'area',
                  'unit', 'phone', 'email', 'website', 'is_active',
                  'cost_for_two', 'cuisine', 'establishment', 'delivery_time',
                  'is_veg', 'full_address')


class RestaurantImageSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(many=False, read_only=True)

    class Meta:
        from .models import RestaurantImage

        model = RestaurantImage
        fields = ('id', 'name', 'restaurant', 'image')
