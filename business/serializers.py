from rest_framework import serializers


class BusinessSerializer(serializers.ModelSerializer):
    from location.serializers import CitySerializer

    city = CitySerializer(many=False, read_only=True)

    class Meta:
        from .models import Business

        model = Business
        fields = ('id', 'name', 'type', 'city')


class DeliveryBoysSerializer(serializers.ModelSerializer):
    from employee.serializers import EmployeeSerializer

    employee = EmployeeSerializer(many=False, read_only=True)

    class Meta:
        from .models import DeliveryBoys

        model = DeliveryBoys
        fields = ('id', 'employee', 'salary', 'is_active', 'start_time', 'end_time')


class ManagerSerializer(serializers.ModelSerializer):
    from employee.serializers import EmployeeSerializer

    employee = EmployeeSerializer(many=False, read_only=True)
    business = BusinessSerializer(many=False, read_only=True)

    class Meta:
        from .models import Manager

        model = Manager
        fields = ('employee', 'business')
