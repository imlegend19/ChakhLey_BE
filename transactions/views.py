from rest_framework.views import APIView
from django.utils.text import gettext_lazy as _
from drfaddons.generics import OwnerListAPIView, OwnerListCreateAPIView


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


class AcceptTransactionView(OwnerListCreateAPIView):
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .serializers import OrderPaymentSerializer
    from .models import OrderPayment

    queryset = OrderPayment.objects.all()
    serializer_class = OrderPaymentSerializer

    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('order', 'payment_mode', 'payment_type', 'is_credit',
                     'accepted_by__employee', 'order__restaurant')

    def perform_create(self, serializer):
        from business.models import Manager

        from rest_framework.exceptions import PermissionDenied

        restaurant = serializer.validated_data['order'].restaurant

        try:
            manager = Manager.objects.get(
                business__manager__employee=self.request.user, business__employee__is_active=True,
                business__restaurant=restaurant
            )
        except Manager.DoesNotExist:
            raise PermissionDenied(
                _("User doesn't have permission on provided restaurant.")
            )

        serializer.save(accepted_by=manager)
