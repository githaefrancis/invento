
from rest_framework import serializers
from inventory.models import Employee,Category,Department,Equipment,SupplyConsumption,Allocation


class CategorySerializer(serializers.ModelSerializer):
  # equipments=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  class Meta:
    model=Category
    fields=('id','category_name','category_description')


class EquipmentSerializer(serializers.ModelSerializer):
  category=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
  category_name=serializers.CharField(source='category.category_name' ,read_only=True)
  # equipment=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  # supply=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  # consumer=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  # equipment=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  
  class Meta:
    model=Equipment
    fields=('id','equipment_name','equipment_serial_number','equipment_code','equipment_model','category','equipment_cost','notes','equipment_image','category_name','available')

class DepartmentSerializer(serializers.ModelSerializer):
  employees=serializers.PrimaryKeyRelatedField(many=True,read_only=True)

  class Meta:
    model=Department
    fields=('id','department_name','department_description','employees')


class AllocationSerializer(serializers.ModelSerializer):
  employee_allocated=serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(),many=False)
  
  equipment_allocated=serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(),many=False)
  
  # print(employee_allocated.employee_fname)

  employee_fname=serializers.CharField(source='employee_allocated.employee_fname',read_only=True)
  employee_lname=serializers.CharField(source='employee_allocated.employee_lname',read_only=True)
  equipment_name=serializers.CharField(source='equipment_allocated.equipment_name',read_only=True)
  equipment_serial_number=serializers.CharField(source='equipment_allocated.equipment_serial_number',read_only=True)
  equipment_code=serializers.CharField(source='equipment_allocated.equipment_code',read_only=True)
  
  class Meta:
    model=Allocation
    fields=('id','employee_allocated','equipment_allocated','equipment_name','employee_fname','employee_lname','equipment_serial_number','is_returned','equipment_code','allocation_date')
    depth=1
class SupplyConsumptionSerializer(serializers.ModelSerializer):
  supply=serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(),many=False)
  consumer=serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(),many=False)
  

  class Meta:
    fields=('supply','consumer')

class EmployeeSerializer(serializers.ModelSerializer):
  # department=DepartmentSerializer(many=False)
  department=serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),many=False)
  department_name=serializers.CharField(source='department.department_name',read_only=True)
  # employees=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  
  # employee=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
  class Meta:
    model=Employee
    fields=('id','employee_fname','employee_lname','department','department_name')

  # def to_representation(self, instance):
  #   response=super().to_representation(instance)
  #   response['department']=DepartmentSerializer(instance.employees).data
  #   return response