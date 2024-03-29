from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Country

        model = Country
        fields = ('id', 'name')


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False, read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('country')
        return queryset

    class Meta:
        from .models import State

        model = State
        fields = ('id', 'name', 'country')


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(many=False, read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('state')
        return queryset

    class Meta:
        from .models import City

        model = City
        fields = ('id', 'name', 'state')


class AreaSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('city')
        return queryset

    class Meta:
        from .models import Area

        model = Area
        fields = ('id', 'name', 'city', 'pincode')
