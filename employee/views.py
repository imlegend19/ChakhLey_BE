from rest_framework.generics import ListAPIView


class EmployeeView(ListAPIView):
    from rest_framework.filters import SearchFilter

    from .models import Employee
    from .serializers import EmployeeSerializer

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    filter_backends = (SearchFilter, )
    search_fields = ('id', 'designation')
