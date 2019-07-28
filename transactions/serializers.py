from rest_framework import serializers


class OrderPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import OrderPayment

        model = OrderPayment
        fields = ('id', 'order', 'amount', 'is_credit', 'payment_type',
                  'payment_mode', 'accepted_by')
