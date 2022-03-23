from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from inventory.models import Department, Employee
from .serializer import DepartmentSerializer, EmployeeSerializer
from rest_framework import status
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