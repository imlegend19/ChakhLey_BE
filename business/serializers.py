from drf_user.serializers import UserSerializer
from rest_framework import serializers

from location.serializers import CitySerializer


class BusinessSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, read_only=True)

    class Meta:
        from .models import Business

        model = Business
        fields = ('id', 'name', 'type', 'city')


class DeliveryBoysSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        from .models import DeliveryBoys

        model = DeliveryBoys
        fields = ('id', 'user', 'salary', 'is_active', 'start_time', 'end_time')


class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    business = BusinessSerializer(many=False, read_only=True)

    class Meta:
        from .models import Manager

        model = Manager
        fields = ('user', 'business')
