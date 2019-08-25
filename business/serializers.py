from rest_framework import serializers


class BusinessSerializer(serializers.ModelSerializer):
    from location.serializers import CitySerializer

    city = CitySerializer(many=False, read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('city')
        return queryset

    class Meta:
        from .models import Business

        model = Business
        fields = ('id', 'name', 'type', 'city', 'latitude', 'longitude')
