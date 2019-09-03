from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView


class OrderListView(ListAPIView):
    from .serializers import OrderListSerializer
    from .models import Order

    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    permission_classes = (AllowAny,)
    serializer_class = OrderListSerializer
    queryset = Order.objects.prefetch_related('delivery', 'suborder_set', 'restaurant', 'delivery_boy',
                                              'suborder_set__item')

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('name', 'restaurant__id', 'mobile', 'status')
    filter_fields = ('name', 'restaurant__id', 'id', 'mobile', 'status', 'delivery_boy', 'delivery_boy__user__id')

    # def dispatch(self, *args, **kwargs):
    #     from django.db import connection
    #
    #     response = super().dispatch(*args, **kwargs)
    #     print('Queries Counted: {}'.format(len(connection.queries)))
    #     return response


class CreateOrderView(CreateAPIView):
    from .serializers import OrderCreateSerializer
    from .models import Order

    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()

    def post(self, request, *args, **kwargs):
        from promocode.models import UserOfferUsage, UserPromoCode
        from django.http import JsonResponse

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data.get('mobile')
        offer = serializer.validated_data.get('offer')
        user_promo_code = serializer.validated_data.get('user_promo_code')

        if offer is not None:
            if offer.expired:
                return JsonResponse({'detail': "Offer has expired."}, status=400)
            else:
                usage_count = UserOfferUsage.objects.filter(user__mobile=mobile, offer=offer).count()
                if usage_count > offer.max_user_usage:
                    return JsonResponse({'detail': "Offer limit exceeded."}, status=400)

            # TODO : Update usage count

        if user_promo_code is not None:
            if user_promo_code.expired:
                return JsonResponse({'detail': "Promo Code has expired."}, status=400)
            else:
                obj = UserPromoCode.objects.get(user__mobile=mobile, id=user_promo_code)
                if obj.uses == obj.max_uses:
                    return JsonResponse({'detail': "Promo Code usage limit exceeded."})

            # TODO: Update usage count

        return super().post(request, *args, **kwargs)


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
