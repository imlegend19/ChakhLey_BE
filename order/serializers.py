from django.core.exceptions import ValidationError
from django.utils.text import gettext_lazy as _
from rest_framework import serializers

from employee.serializers import EmployeeSerializer
from product.serializers import ProductSerializer


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Delivery

        fields = ('id', 'amount', 'location', 'unit_no', 'address_line_2', 'full_address', 'latitude', 'longitude')
        model = Delivery


class SubOrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        from .models import SubOrder

        model = SubOrder
        fields = ('id', 'item', 'product', 'quantity', 'sub_total')
        read_only_fields = ('product', 'sub_total')
        extra_kwargs = {
            "item": {"write_only": True}
        }


class OrderListSerializer(serializers.ModelSerializer):
    from restaurant.serializers import RestaurantSerializer

    delivery = DeliverySerializer(many=False, read_only=True)
    suborder_set = SubOrderSerializer(many=True, read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    restaurant = RestaurantSerializer(many=False, read_only=True)
    delivery_boy = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'business', 'restaurant', 'preparation_time',
                  'status', 'order_date', 'total', 'packaging_charge', 'payment_done', 'delivery', 'suborder_set',
                  'delivery_boy', 'has_delivery_boy')


class OrderCreateSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer(many=False)
    suborder_set = SubOrderSerializer(many=True)

    @staticmethod
    def validate_suborder_set(value):
        if len(value) is 0:
            raise serializers.ValidationError(_("Minimum 1 item required to place an order."))
        return value

    def create(self, validated_data):
        from .models import SubOrder, Delivery

        suborder_set = validated_data.pop('suborder_set')
        delivery = validated_data.pop('delivery')

        instance = super(OrderCreateSerializer, self).create(
            validated_data=validated_data
        )

        for so in suborder_set:
            SubOrder.objects.create(
                order=instance,
                **so
            )

        Delivery.objects.create(
            order=instance,
            **delivery
        )

        return instance

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'business', 'restaurant', 'status', 'delivery_boy',
                  'preparation_time', 'order_date', 'total', 'payment_done', 'delivery', 'suborder_set')
        read_only_fields = ('status', 'total', 'payment_done')


class OrderUpdateSerializer(serializers.ModelSerializer):
    from restaurant.serializers import RestaurantSerializer

    suborder_set = SubOrderSerializer(many=True)
    delivery = DeliverySerializer(many=False)
    restaurant = RestaurantSerializer(many=False)

    def update(self, instance, validated_data):
        from django.utils import timezone

        if 'preparation_time' in validated_data:
            preparation_time = validated_data.pop('preparation_time')
            now = timezone.now()
            etd = now + preparation_time
            preparation_time = etd - instance.create_date
            validated_data['preparation_time'] = preparation_time

        if 'status' in validated_data:
            status = validated_data.get('status')
            if status == 'Pr':
                try:
                    delivery_boy = validated_data.get('delivery_boy')
                    if delivery_boy is None:
                        raise ValidationError(_('Delivery Boy has to be assigned if status is Preparing!'))
                    elif delivery_boy.designation != 'DB':
                        raise ValidationError(_("Not a valid delivery boy!"))
                except KeyError:
                    raise ValidationError(_('Delivery Boy has to be assigned if status is Preparing!'))

        return super(OrderUpdateSerializer, self).update(
            instance=instance, validated_data=validated_data)

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'status', 'total',
                  'preparation_time', 'suborder_set', 'total', 'restaurant',
                  'order_date', 'payment_done', 'delivery', 'delivery_boy', 'has_delivery_boy')
        read_only_fields = ('id', 'name', 'mobile', 'email', 'suborder_set',
                            'total', 'restaurant', 'delivery', 'has_delivery_boy')


class OrderFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import OrderFeedback

        model = OrderFeedback
        fields = ('id', 'order_id', 'type', 'description', 'mobile')
        read_only_fields = ('id',)
