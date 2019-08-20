from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView


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
    filter_fields = ('name', 'restaurant__id', 'id', 'mobile', 'status', 'delivery_boy', 'delivery_boy__user__id')


class CreateOrderView(CreateAPIView):
    from .serializers import OrderCreateSerializer
    from .models import Order

    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


class RetrieveUpdateOrderView(RetrieveUpdateAPIView):
    from .serializers import OrderUpdateSerializer
    from .models import Order

    serializer_class = OrderUpdateSerializer
    queryset = Order.objects.all()


class ListCreateOrderFeedbackView(ListCreateAPIView):
    from .serializers import OrderFeedbackSerializer
    from .models import OrderFeedback

    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    permission_classes = (AllowAny,)
    serializer_class = OrderFeedbackSerializer
    queryset = OrderFeedback.objects.all()

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('type', 'mobile', 'order_id')
    filter_fields = ('id', 'type', 'mobile', 'order_id')
