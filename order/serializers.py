from rest_framework import serializers

from django.utils.text import gettext_lazy as _
from restaurant.models import Restaurant


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Delivery

        fields = ('order', 'amount', 'area', 'unit_no', 'address_line_2', 'full_address')
        model = Delivery
        read_only_fields = ('full_address', )


class SubOrderSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import SubOrder

        model = SubOrder
        fields = ('order', 'item', 'product', 'quantity', 'sub_total')
        read_only_fields = ('product', 'sub_total')
        extra_kwargs = {
            "item": {"write_only": True}
        }


class OrderSerializer(serializers.ModelSerializer):
    suborder_set = SubOrderSerializer(many=True)
    status = serializers.CharField(source='get_status_display', read_only=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        source='restaurant', queryset=Restaurant.objects.all(), write_only=True
    )
    restaurant = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='restaurant:restaurant-detail', lookup_field='pk'
    )
    delivery = DeliverySerializer(many=False, default=None)

    @staticmethod
    def validate_suborder_set(value):
        if len(value) == 0:
            raise serializers.ValidationError(_("Minimum 1 item required to place an Order."))

        return value

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'status', 'preparation_time',
                  'restaurant_id', 'suborder_set', 'total', 'restaurant', 'create_date',
                  'update_date', 'delivery')
        read_only_fields = ('status', 'preparation_time', 'total', 'create_date', 'update_date')


class OrderListSerializer(serializers.ModelSerializer):
    restaurant = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='restaurant:restaurant-detail', lookup_field='pk'
    )
    detail = serializers.HyperlinkedRelatedField(
        source='id', many=False, read_only=True, view_name='order:order-retrieve', lookup_field='pk'
    )
    update = serializers.HyperlinkedRelatedField(
        source='id', many=False, read_only=True, view_name='order:order-update', lookup_field='pk'
    )
    status_display = serializers.CharField(source='get_status_display')
    phone = serializers.CharField(source='restaurant.phone', read_only=True)

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'status', 'create_date', 'preparation_time',
                  'total', 'restaurant', 'status_display', 'update_date', 'phone', 'detail', 'update')
        read_only_fields = fields


class OrderUpdateSerializer(serializers.ModelSerializer):
    suborder_set = SubOrderSerializer(many=True)
    restaurant = serializers.HyperlinkedRelatedField(
        many=False, read_only=True, view_name='restaurant:restaurant-detail', lookup_field='pk'
    )
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
            instance=instance, validated_data=validated_data
        )

    class Meta:
        from .models import Order

        model = Order
        fields = ('id', 'name', 'mobile', 'email', 'status', 'preparation_time',
                  'suborder_set', 'total', 'restaurant', 'create_date', 'update_date',
                  'delivery')
        read_only_fields = ('id', 'name', 'mobile', 'email', 'suborder_set',
                            'total', 'restaurant', 'delivery')

