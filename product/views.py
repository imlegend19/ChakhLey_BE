from rest_framework.generics import ListAPIView


class CategoryListView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from .models import Category
    from django_filters.rest_framework.backends import DjangoFilterBackend
    from .serializers import CategorySerializer

    permission_classes = (AllowAny, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, )
    search_fields = ('name', 'restaurant')
    filter_fields = ('name', 'restaurant')


class ProductListView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend
    from .models import Product
    from .serializers import ProductSerializer

    permission_classes = (AllowAny, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, )
    filter_fields = ('name', 'category', 'is_veg')
    search_fields = ('name', 'category', 'is_veg')


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
    search_fields = ('rating', 'product')
    filter_fields = ('product', )


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
    search_fields = ('rating', 'restaurant')
    filter_fields = ('restaurant', )
