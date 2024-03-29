from rest_framework.generics import ListCreateAPIView


class CountryView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from .models import Country
    from .serializers import CountrySerializer

    permission_classes = (AllowAny,)
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class StateView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import State
    from .serializers import StateSerializer

    permission_classes = (AllowAny,)

    queryset = State.objects.prefetch_related('country')
    serializer_class = StateSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('country__name',)
    search_fields = ('name', 'country__name')


class CityView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import City
    from .serializers import CitySerializer

    permission_classes = (AllowAny,)
    queryset = City.objects.prefetch_related('state')
    serializer_class = CitySerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('state__country__name', 'state__name')
    search_fields = ('name', 'state__country__name', 'state__name')


class AreaView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import Area
    from .serializers import AreaSerializer

    permission_classes = (AllowAny,)
    queryset = Area.objects.prefetch_related('city')
    serializer_class = AreaSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('city', 'city__name', 'pincode')
    search_fields = ('name', 'pincode', 'city__name')
