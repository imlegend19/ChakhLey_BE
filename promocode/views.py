from rest_framework.generics import ListCreateAPIView


class OfferView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .serializers import OfferSerializer
    from .models import Offer

    permission_classes = (AllowAny, )
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()

    filter_backends = (SearchFilter, DjangoFilterBackend, )
    filter_fields = ('id', 'type', 'business', 'max_user_usage')
    search_fields = ('id', 'code', 'business')
    ordering = ['-create_date']


class UserPromoCodeView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .serializers import UserPromoCodeSerializers
    from .models import UserPromoCode

    permission_classes = (AllowAny, )
    serializer_class = UserPromoCodeSerializers
    queryset = UserPromoCode.objects.all()

    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_fields = ('id', 'code', 'user', 'user__mobile', 'business')
    search_fields = ('id', 'code', 'business')
    ordering = ['-create_date']





