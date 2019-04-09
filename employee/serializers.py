from rest_framework import serializers

from business.serializers import BusinessSerializer


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        from .models import Employee

        business = BusinessSerializer(many=False, read_only=True)

        model = Employee
        fields = ('id', 'name', 'designation', 'business', 'is_active',
                  'joined_on', 'left_on', 'salary')
