from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny


class EmployeeView(ListAPIView):
    from rest_framework.filters import SearchFilter

    from .models import Employee
    from .serializers import EmployeeSerializer
    from django_filters.rest_framework.backends import DjangoFilterBackend

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.prefetch_related('business', 'user')
    permission_classes = (AllowAny,)

    filter_backends = (SearchFilter, DjangoFilterBackend,)
    search_fields = ('id', 'designation')
    filter_fields = ('designation',)

    # def dispatch(self, *args, **kwargs):
    #     from django.db import connection
    #
    #     response = super().dispatch(*args, **kwargs)
    #     print('Queries Counted: {}'.format(len(connection.queries)))
    #     return response


class RetrieveUpdateEmployeeView(RetrieveUpdateAPIView):
    from .serializers import EmployeeSerializer
    from .models import Employee

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.prefetch_related('user', 'business')


class EmployeeDocumentView(CreateAPIView):
    from .models import EmployeeDocument
    from .serializers import EmployeeDocumentSerializer

    serializer_class = EmployeeDocumentSerializer
    queryset = EmployeeDocument.objects.all()
