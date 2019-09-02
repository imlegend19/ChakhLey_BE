from rest_framework import serializers


class OfferSerializer(serializers.ModelSerializer):
    from .models import Offer

    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = Offer
        fields = ('code', 'title', 'type', 'description', 'free_delivery', 'discount', 'max_user_usage',
                  'day', 'expired')
