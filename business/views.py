from rest_framework.generics import ListAPIView


class BusinessView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import Business
    from .serializers import BusinessSerializer

    permission_classes = (AllowAny, )

    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, )
    search_fields = ('id', 'name')
    filter_fields = ('city__id', )


class DeliveryBoysViews(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import DeliveryBoys
    from .serializers import DeliveryBoysSerializer

    permission_classes = (AllowAny, )

    queryset = DeliveryBoys.objects.all()
    serializer_class = DeliveryBoysSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, )
    search_fields = ('id', 'is_active')
    filter_fields = ('employee__name', 'employee__id')


class ManagerViews(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import Manager
    from .serializers import ManagerSerializer

    permission_classes = (AllowAny, )

    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter, )
    search_fields = ('id', )
    filter_fields = ('employee__name', 'employee__id', 'business__id')
