from rest_framework import serializers

from business.serializers import BusinessSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    from drf_user.serializers import UserSerializer

    business = BusinessSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        from .models import Employee

        model = Employee
        fields = ('id', 'user', 'designation', 'business', 'is_active', 'joined_on', 'left_on', 'salary')
        ordering = ['-id']


class EmployeeOrderSerializer(serializers.ModelSerializer):
    from drf_user.serializers import UserSerializer

    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.name')

    class Meta:
        from .models import Employee

        model = Employee
        fields = ('id', 'user_id', 'user_name', 'designation', 'is_active')
        ordering = ['-id']


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import EmployeeDocument

        model = EmployeeDocument
        fields = ('id', 'employee', 'doc', 'doc_type', 'doc_value', 'is_verified', 'verified_by', 'verified_on')
        ordering = ['-id']
