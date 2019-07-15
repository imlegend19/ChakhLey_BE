from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView


class OrderListView(ListAPIView):
    from .serializers import OrderListSerializer
    from .models import Order

    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    permission_classes = (AllowAny,)
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'restaurant__id', 'mobile', 'status')
    filter_fields = ('name', 'restaurant__id', 'id', 'mobile', 'status')


class CreateOrderView(CreateAPIView):
    from .serializers import OrderCreateSerializer
    from .models import Order

    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


class RetrieveOrderView(RetrieveUpdateAPIView):
    from .serializers import OrderUpdateSerializer
    from .models import Order

    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()
