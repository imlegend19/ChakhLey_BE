from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class TransactionStaticVariableView(APIView):

    @staticmethod
    def get(request):
        from ChakhLey_BE.variables import PAYMENT_MODE_CHOICES
        from ChakhLey_BE.variables import PAYMENT_TYPE_CHOICES

        from drfaddons.utils import JsonResponse

        data = {'PAYMENT_TYPE': {}, 'PAYMENT_MODE': {}}
        for obj in PAYMENT_TYPE_CHOICES:
            data['PAYMENT_TYPE'][obj[1]] = obj[0]

        for obj in PAYMENT_MODE_CHOICES:
            data['PAYMENT_MODE'][obj[1]] = obj[0]

        return JsonResponse(content=data, status=200)


class TransactionListView(ListAPIView):
    from .serializers import OrderPaymentSerializer
    from .models import OrderPayment

    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    permission_classes = (AllowAny,)
    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('id', 'order', 'payment_mode', 'payment_type', 'is_credit')
    filter_fields = ('order', 'payment_mode', 'payment_type', 'is_credit')


class TransactionDestroyView(DestroyAPIView):
    from .serializers import OrderPaymentSerializer
    from .models import OrderPayment

    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer


class AcceptTransactionView(CreateAPIView):
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .serializers import OrderPaymentSerializer
    from .models import OrderPayment

    permission_classes = (AllowAny,)

    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('order', 'payment_mode', 'payment_type', 'is_credit',
                     'accepted_by', 'order__restaurant')
