from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class CategoryListView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from .models import Category
    from django_filters.rest_framework.backends import DjangoFilterBackend
    from .serializers import CategorySerializer

    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'restaurant__id')
    filter_fields = ('name', 'restaurant__id', 'id')


class CategoryUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    from rest_framework.permissions import AllowAny

    from .models import Category
    from .serializers import CategorySerializer

    permission_classes = (AllowAny,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend
    from .models import Product
    from .serializers import ProductSerializer

    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('name', 'category__id', 'category__restaurant__id', 'is_veg')
    search_fields = ('name', 'category__id', 'is_veg')


class ProductUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    from rest_framework.permissions import AllowAny
    from .models import Product
    from .serializers import ProductSerializer

    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

