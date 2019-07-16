from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from drfaddons.generics import OwnerListAPIView


class TransactionStaticVariableView(APIView):

    @staticmethod
    def get(request):
        from ChakhLe_BE.variables import PAYMENT_MODE_CHOICES
        from ChakhLe_BE.variables import PAYMENT_TYPE_CHOICES

        from drfaddons.utils import JsonResponse

        data = {'PAYMENT_TYPE': {}, 'PAYMENT_MODE': {}}
        for obj in PAYMENT_TYPE_CHOICES:
            data['PAYMENT_TYPE'][obj[1]] = obj[0]

        for obj in PAYMENT_MODE_CHOICES:
            data['PAYMENT_MODE'][obj[1]] = obj[0]

        return JsonResponse(content=data, status=200)


class TransactionListView(OwnerListAPIView):
    from .serializers import OrderPaymentSerializer
    from .models import OrderPayment

    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer

    filter_fields = ('order', 'payment_mode', 'payment_type', 'is_credit')


class AcceptTransactionView(CreateAPIView):
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .serializers import OrderPaymentSerializer
    from .models import OrderPayment

    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer

    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('order', 'payment_mode', 'payment_type', 'is_credit',
                     'accepted_by', 'order__restaurant')
