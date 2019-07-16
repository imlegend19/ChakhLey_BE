from rest_framework import serializers


class BusinessSerializer(serializers.ModelSerializer):
    from location.serializers import CitySerializer

    city = CitySerializer(many=False, read_only=True)

    class Meta:
        from .models import Business

        model = Business
        fields = ('id', 'name', 'type', 'city')
