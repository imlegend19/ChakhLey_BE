from rest_framework import serializers

from business.serializers import BusinessSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    from drf_user.serializers import UserShowSerializer

    business_id = serializers.IntegerField(source='business.id')
    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.name')
    user_mobile = serializers.CharField(source='user.mobile')

    class Meta:
        from .models import Employee

        model = Employee
        fields = ('id', 'user_id', 'user_name', 'user_mobile', 'business_id', 'is_active')
        ordering = ['-id']


class EmployeeOrderSerializer(serializers.ModelSerializer):
    from drf_user.serializers import UserSerializer

    user_id = serializers.IntegerField(source='user.id')
    user_name = serializers.CharField(source='user.name')
    user_mobile = serializers.CharField(source='user.mobile')

    class Meta:
        from .models import Employee

        model = Employee
        fields = ('id', 'user_id', 'user_name', 'designation', 'user_mobile', 'is_active')
        ordering = ['-id']


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import EmployeeDocument

        model = EmployeeDocument
        fields = ('id', 'employee', 'doc', 'doc_type', 'doc_value', 'is_verified', 'verified_by', 'verified_on')
        ordering = ['-id']
