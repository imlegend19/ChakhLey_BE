from rest_framework import serializers


class OfferSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        from .models import Offer

        model = Offer
        fields = ('code', 'title', 'type', 'description', 'free_delivery', 'discount', 'max_user_usage',
                  'day', 'expired')


class UserPromoCodeSerializers(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.name')
    user_mobile = serializers.CharField(source='user.mobile')

    class Meta:
        from .models import UserPromoCode
        model = UserPromoCode
        fields = ('id', 'code', 'description', 'user_id', 'user_name', 'user_mobile', 'discount', 'expired',
                  'free_delivery', 'asset')
