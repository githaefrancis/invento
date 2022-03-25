
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from inventory.models import Department, Employee,Category,Equipment,SupplyConsumption,Allocation
from .serializer import DepartmentSerializer, EmployeeSerializer,AllocationSerializer,CategorySerializer,EquipmentSerializer,SupplyConsumptionSerializer
from rest_framework import status
import json
# Create your views here.

class DepartmentList(APIView):
  def get(self,request,format=None):
    all_departments=Department.get_all_departments()
    serializers=DepartmentSerializer(all_departments,many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=DepartmentSerializer(data=request.data)
    
    if serializers.is_valid():
      serializers.save()

      return Response(serializers.data, status=status.HTTP_201_CREATED)

class EmployeeList(APIView):
  def get(self,request,format=None):
    all_employees=Employee.get_all_employees()
    serializers=EmployeeSerializer(all_employees,many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=EmployeeSerializer(data=request.data)
    department_id=request.data.get('department')

    target_department=Department.objects.get(pk=department_id)
    print(target_department)
    if serializers.is_valid():
      serializers.save(department=target_department)

      return Response(serializers.data,status=status.HTTP_201_CREATED)
    return serializers

class CategoryList(APIView):
  def get(self,request,format=None):
    all_categories=Category.objects.all()
    serializers=CategorySerializer(all_categories,many=True)
    return Response(serializers.data)


class ConsumptionList(APIView):
  def get(self,request, format=None):
    all_consumption=SupplyConsumption.objects.all()
    serializers=SupplyConsumptionSerializer(all_consumption,many=True)
    return Response(serializers.data)

class EquipmentList(APIView):
  def get(self,request, format=None):
    all_equipment=Equipment.objects.all()
    serializers=EquipmentSerializer(all_equipment,many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=EquipmentSerializer(data=request.data)
    category_id=request.data.get('category')
    
    target_category=Category.objects.get(pk=category_id)
  
    if serializers.is_valid():
      serializers.save(category=target_category)

      return Response(serializers.data,status=status.HTTP_201_CREATED)


class EquipmentAvailableList(APIView):
  def get(self,request, format=None):
    all_equipment=Equipment.objects.filter(available=True).all()
    serializers=EquipmentSerializer(all_equipment,many=True)
    return Response(serializers.data)


class AllocationList(APIView):
  def get(self,request, format=None):
    all_allocation=Allocation.objects.all()
    serializers=AllocationSerializer(all_allocation,many=True)
    return Response(serializers.data)

  def post(self,request,format=None):
    serializers=AllocationSerializer(data=request.data)
    equipment_id=request.data.get('equipment_allocated')
    target_equipment=Equipment.objects.filter(id=equipment_id).first()
    employee_id=request.data.get('employee_allocated')
    target_employee=Employee.objects.filter(id=employee_id).first()   
    target_equipment.assign_equipment()
  
    if serializers.is_valid():
      serializers.save(equipment_allocated=target_equipment,employee_allocated=target_employee)

      return Response(serializers.data,status=status.HTTP_201_CREATED)
  

