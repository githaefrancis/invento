from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from inventory.models import Department
from .serializer import DepartmentSerializer

# Create your views here.

class DepartmentList(APIView):
  def get(self,request,format=None):
    all_departments=Department.get_all_departments()
    serializers=DepartmentSerializer(all_departments,many=True)
    return Response(serializers.data)
