from rest_framework import serializers


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
