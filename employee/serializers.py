from rest_framework import serializers

from business.serializers import BusinessSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    from drf_user.serializers import UserShowSerializer

    business = BusinessSerializer(many=False, read_only=True)
    user = UserShowSerializer(many=False, read_only=True)

    class Meta:
        from .models import Employee

        model = Employee
        fields = ('id', 'user', 'designation', 'business', 'is_active', 'joined_on', 'left_on', 'salary')
        ordering = ['-id']


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import EmployeeDocument

        model = EmployeeDocument
        fields = ('id', 'employee', 'doc', 'doc_type', 'doc_value', 'is_verified', 'verified_by', 'verified_on')
        ordering = ['-id']
