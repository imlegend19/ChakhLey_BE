from rest_framework.generics import ListAPIView, RetrieveAPIView


class RestaurantListView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from .serializers import RestaurantSerializer
    from .models import Restaurant

    permission_classes = (AllowAny, )
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

    filter_backends = (SearchFilter, )
    search_fields = ('name', 'id')


class RetrieveRestaurntView(RetrieveAPIView):
    from rest_framework.permissions import AllowAny

    from .models import Restaurant
    from .serializers import RestaurantSerializer

    permission_classes = (AllowAny, )
    queryset = Restaurant.objects.filter(is_active=True)
    serializer_class = RestaurantSerializer
    filter_backends = ()


class RestaurantImageListView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from .serializers import RestaurantImageSerializer
    from .models import RestaurantImage

    permission_classes = (AllowAny, )
    serializer_class = RestaurantImageSerializer
    queryset = RestaurantImage.objects.all()

    filter_backends = (SearchFilter, )
    search_fields = ('id', 'name')
