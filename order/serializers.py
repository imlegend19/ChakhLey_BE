from rest_framework import serializers

from django.utils.text import gettext_lazy as _

from product.serializers import ProductSerializer


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Delivery

        fields = ('id', 'amount', 'area', 'unit_no', 'address_line_2', 'full_address')
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

    delivery = DeliverySerializer(many=False, read_only=True)
    suborder_set = SubOrderSerializer(many=True, read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'mobile', 'email', 'business', 'restaurant', 'preparation_time',
                  'status', 'order_date', 'total', 'payment_done', 'delivery', 'suborder_set')


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
        fields = ('id', 'name', 'mobile', 'email', 'business', 'restaurant', 'status',
                  'preparation_time', 'order_date', 'total', 'payment_done', 'delivery', 'suborder_set')
        read_only_fields = ('status', 'preparation_time', 'total', 'payment_done')


class OrderUpdateSerializer(serializers.ModelSerializer):

    suborder_set = SubOrderSerializer(many=True)
    restaurant = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='restauran:restaurant-detail',
        lookup_field='pk')
    delivery = DeliverySerializer(many=False)

    def update(self, instance, validated_data):
        from django.utils import timezone

        if 'preparation_time' in validated_data:
            preparation_time = validated_data.pop('preparation_time')
            now = timezone.now()
            etd = now + preparation_time
            preparation_time = etd - instance.create_date
            validated_data['preparation_time'] = preparation_time

        return super(OrderUpdateSerializer, self).update(
            instance=instance, validated_data=validated_data)

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'status',
                  'preparation_time', 'suborder_set', 'total', 'restaurant',
                  'order_date', 'payment_done', 'delivery')
        read_only_fields = ('id', 'name', 'mobile', 'email', 'suborder_set',
                            'total', 'restaurant', 'payment_done', 'delivery')
