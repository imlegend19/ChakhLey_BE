from rest_framework.generics import ListAPIView


class UserProductRatingListView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend
    from .models import UserProductRating
    from .serializers import UserProductRatingSerializer

    permission_classes = (AllowAny,)
    queryset = UserProductRating.objects.all()
    serializer_class = UserProductRatingSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('rating', 'product__id')
    filter_fields = ('product__id', )


class UserRestaurantRatingListView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from .models import UserRestaurantRating
    from django_filters.rest_framework.backends import DjangoFilterBackend
    from .serializers import UserRestaurantSerializer

    permission_classes = (AllowAny,)
    queryset = UserRestaurantRating.objects.all()
    serializer_class = UserRestaurantSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('rating', 'restaurant__id')
    filter_fields = ('restaurant__id', )
