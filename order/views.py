from drfaddons.generics import OwnerCreateAPIView, OwnerRetrieveAPIView, OwnerListAPIView

from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView


class OrderListView(OwnerListAPIView):
    from .serializers import OrderListSerializer
    from .models import Order

    serializer_class = OrderListSerializer
    queryset = Order.objects.all()


class CreateOrderView(OwnerCreateAPIView):
    from .serializers import OrderSerializer
    from .models import Order

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class RetrieveOrderView(OwnerRetrieveAPIView):
    from .serializers import OrderSerializer
    from .models import Order

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


