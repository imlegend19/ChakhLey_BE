from rest_framework import serializers


class OrderPaymentSerializer(serializers.ModelSerializer):
    from employee.serializers import EmployeeSerializer

    accepted_by = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        from .models import OrderPayment

        model = OrderPayment
        fields = ('id', 'order', 'amount', 'is_credit', 'payment_type',
                  'payment_mode', 'accepted_by')


class AcceptOrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import OrderPayment

        model = OrderPayment
        fields = ('id', 'order', 'amount', 'is_credit', 'payment_type',
                  'payment_mode', 'accepted_by')
