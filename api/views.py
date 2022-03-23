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

  def post(self,request,format=json):
    serializers=DepartmentSerializer(data=request.data)
    # department_id=request.POST.get('department')

    # current_department=Department.get_department_by_id(3)
    if serializers.is_valid():
      serializers.save()

      return Response(serializers.data,status=status.HTTP_201_CREATED)


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

class AllocationList(APIView):
  def get(self,request, format=None):
    all_allocation=Allocation.objects.all()
    serializers=AllocationSerializer(all_allocation,many=True)
    return Response(serializers.data)

