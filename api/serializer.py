from rest_framework import serializers
from inventory.models import Employee,Category,Department,Equipment,SupplyConsumption,Allocation

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Department
    fields=('department_name','department_description')