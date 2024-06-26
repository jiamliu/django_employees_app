from rest_framework.serializers import ModelSerializer

from .models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "fullname", "department", "birthdate", "salary", "created_at"]