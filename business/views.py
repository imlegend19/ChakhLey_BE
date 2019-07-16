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
