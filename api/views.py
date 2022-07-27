
from functools import partial
from logging import exception
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from inventory.models import Department, Employee,Category,Equipment,SupplyConsumption,Allocation
from .serializer import DepartmentSerializer, EmployeeSerializer,AllocationSerializer,CategorySerializer,EquipmentSerializer,SupplyConsumptionSerializer
from rest_framework import status
import json
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
# Create your views here.
import jwt

class Login(APIView):
  def post(self,request,*args,**kwargs):
    if not request.data:
      return Response({'Error',"Please provide username and password"},status="400")

    username=request.data['username']
    password=request.data['password']
    try:
      user=User.objects.get(username=username)
      

    except User.DoesNotExist:
      return Response({'Error':"Invalid username/password"},status="400")

    if check_password(password,user.password):

      payload={
        'id':user.id,
        'email':user.email
      }
      jwt_token={'token':jwt.encode(payload,"SECRET_KEY")}
      return HttpResponse(
        json.dumps(jwt_token),
        status=200,
        content_type="application/json"
      )

    else:
      return Response(
        json.dumps({'Error':"Invalid credentials"}),
        status=400,
        content_type="application/json"
      )

class Register(APIView):
  def post(self,request,*args, **kwargs):
    if not request.data:
      return Response({'Error':"Please provide the required fields"}, status="400")
    try:
      print(request.data)
      username=request.data['username']
      email=request.data['email']
      password=request.data['password']
      first_name=request.data['first_name']
      last_name=request.data['last_name']

      new_user=User.objects.create(username=username,email=email,first_name=first_name,last_name=last_name)
      print(new_user)
      new_user.set_password(password)
      new_user.save()

      return HttpResponse("account created successfully",status=201,content_type="application/json")

    except:
      return Response({'Error':"Email or username already exists"},status="400")

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
  

class AllocationDetails(APIView):

  def get_allocation(self,pk):
    try:
      return Allocation.objects.get(pk=pk)
    except Allocation.DoesNotExist:
      return Http404
      
  def put(self,request,pk,format=None):
    allocation=self.get_allocation(pk)
    serializers=AllocationSerializer(allocation,request.data,partial=True) 
    equipment_id=allocation.equipment_allocated.id
    target_equipment=Equipment.objects.filter(id=equipment_id).first()
    print(target_equipment)
    if serializers.is_valid():
      target_equipment.release_equipment()

      serializers.save()

      return Response(serializers.data)
    
    else:
      return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)