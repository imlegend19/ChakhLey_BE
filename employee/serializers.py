from rest_framework import serializers

from business.serializers import BusinessSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        from drf_user.serializers import UserSerializer
        from .models import Employee

        business = BusinessSerializer(many=False, read_only=True)
        user = UserSerializer(many=False, read_only=True)

        model = Employee
        fields = ('id', 'user', 'designation', 'business', 'is_active', 'joined_on', 'left_on', 'salary')
        ordering = ['-id']


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import EmployeeDocument

        model = EmployeeDocument
        fields = ('id', 'employee', 'doc', 'doc_type', 'doc_value', 'is_verified', 'verified_by', 'verified_on')
        ordering = ['-id']
