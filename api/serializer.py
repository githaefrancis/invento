from rest_framework import serializers
from inventory.models import Employee,Category,Department,Equipment,SupplyConsumption,Allocation

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Department
    fields=('department_name','department_description')


class EmployeeSerializer(serializers.ModelSerializer):
  department=DepartmentSerializer(many=False)
  class Meta:
    model=Employee
    fields=('employee_fname','employee_lname','department')
