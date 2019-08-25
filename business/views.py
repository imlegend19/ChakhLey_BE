from rest_framework.generics import ListAPIView


class BusinessView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter

    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import Business
    from .serializers import BusinessSerializer

    permission_classes = (AllowAny,)
    queryset = Business.objects.prefetch_related('city')
    serializer_class = BusinessSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter,)
    search_fields = ('id', 'name')
    filter_fields = ('city__id',)

    # def dispatch(self, *args, **kwargs):
    #     from django.db import connection
    #
    #     response = super().dispatch(*args, **kwargs)
    #     print('Queries Counted: {}'.format(len(connection.queries)))
    #     return response

