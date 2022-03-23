from rest_framework import serializers
from inventory.models import Employee,Category,Department,Equipment,SupplyConsumption,Allocation


class CategorySerializer(serializers.ModelSerializer):
  equipments=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  class Meta:
    mode=Category
    fields=('category_name','category_description')


class EquipmentSerializer(serializers.ModelSerializer):
  category=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
  equipment=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  supply=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  consumer=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  
  class Meta:
    model=Equipment
    fields=('equipment_name','equipment_serial_number','equipment_code','category')

class DepartmentSerializer(serializers.ModelSerializer):
  employees=serializers.PrimaryKeyRelatedField(many=True,read_only=True)

  class Meta:
    model=Department
    fields=('department_name','department_description','employees')


class AllocationSerializer(serializers.ModelSerializer):
  employee_allocated=serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),many=False)
  equipment_allocated=serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(),many=False)
  class Meta:
    model=Allocation
    fields=('employee_allocated','equipment_allocated')

class SupplyConsumptionSerializer(serializers.ModelSerializer):
  supply=serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(),many=False)
  consumer=serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(),many=False)
  

  class Meta:
    fields=('supply','consumer')

class EmployeeSerializer(serializers.ModelSerializer):
  # department=DepartmentSerializer(many=False)
  department=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
  employee=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  class Meta:
    model=Employee
    fields=('employee_fname','employee_lname','department','employee')

  # def to_representation(self, instance):
  #   response=super().to_representation(instance)
  #   response['department']=DepartmentSerializer(instance.employees).data
  #   return response