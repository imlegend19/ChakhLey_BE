from rest_framework import serializers


class OrderPaymentSerializer(serializers.ModelSerializer):

    # def validate(self, data):
    #     from order.models import Order
    #
    #     amount = data['amount']
    #     order = Order.objects.get(id=data['order'].id)
    #
    #     if amount == order.total:
    #         order.payment_done = True
    #
    #     return data

    class Meta:
        from .models import OrderPayment

        model = OrderPayment
        fields = ('id', 'order', 'amount', 'is_credit', 'payment_type',
                  'payment_mode', 'accepted_by')
