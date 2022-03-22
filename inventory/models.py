from tkinter import CASCADE
from django.db import models

# Create your models here.

class Category(models.Model):
  '''
  Model class that defines the table structure for the category table of inventory items
  '''
  category_name=models.CharField(max_length=100)
  category_slug=models.CharField(max_length=100,default=None)
  category_description=models.CharField(max_length=500)


class Equipment(models.Model):
  equipment_name=models.CharField(max_length=250)
  equipment_serial_number=models.CharField(max_length=100)
  equipment_code=models.IntegerField(default=0)
  equipment_model=models.CharField(max_length=100, default=None)
  equipment_type=models.CharField(max_length=100, default=None)
  category=models.ForeignKey(Category,related_name='equipments',on_delete=models.CASCADE)
  equipment_cost=models.FloatField(default=None)
  available=models.BooleanField(default=True)
  notes=models.CharField(max_length=500,default=None)
  damaged=models.BooleanField(default=False)

class Department(models.Model):
  department_name=models.CharField(max_length=100)
  department_description=models.CharField(max_length=100)
  employee_count=models.IntegerField(default=0)

class Employee(models.Model):
  employee_fname=models.CharField(max_length=50)
  employee_lname=models.CharField(max_length=50)
  department=models.ForeignKey(Department,related_name='employees',on_delete=models.CASCADE)
  is_active=models.BooleanField(default=True)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_on=models.DateTimeField(auto_now=True)

class Allocation(models.Model):
  employee_allocated=models.ForeignKey(Employee,related_name='employee',on_delete=models.CASCADE)
  equipment_allocated=models.ForeignKey(Equipment,related_name='equipment',on_delete=models.CASCADE)
  allocation_date=models.DateField(auto_now_add=True)
  is_returned=models.BooleanField(default=False)
  date_returned=models.DateTimeField(default=None)
  notes=models.CharField(max_length=500,default=None)

class supply_consumption(models.Model):
  supply=models.OneToOneField(Equipment,related_name='supply',on_delete=models.CASCADE)
  consumer=models.ForeignKey(Equipment,related_name='consumer',on_delete=models.CASCADE)
  installation_date=models.DateTimeField(auto_now_add=True)
  notes=models.CharField(default=None)
