from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Category(models.Model):
  '''
  Model class that defines the table structure for the category table of inventory items
  '''
  category_name=models.CharField(max_length=100)
  category_description=models.CharField(max_length=500)

  def save_category(self):
    self.save()

  def __str__(self):
    return self.category_name

class Equipment(models.Model):
  equipment_name=models.CharField(max_length=250)
  equipment_serial_number=models.CharField(max_length=100)
  equipment_code=models.IntegerField(default=0)
  equipment_model=models.CharField(max_length=100, default=None)
  equipment_type=models.CharField(max_length=100, null=True,default=None)
  category=models.ForeignKey(Category,related_name='equipments',on_delete=models.CASCADE)
  equipment_cost=models.FloatField(default=None,null=True)
  available=models.BooleanField(default=True)
  notes=models.CharField(max_length=500,default=None,null=True)
  damaged=models.BooleanField(default=False)
  equipment_image=CloudinaryField('image',default=None,null=True)

  def save_equipment(self):
    self.save()

  def __str__(self):
    return self.equipment_name

  def assign_equipment(self):
    self.available=False
    self.save()
    return self

  def release_equipment(self):
    self.available=True
    self.save()
    return self()
class Department(models.Model):
  department_name=models.CharField(max_length=100)
  department_description=models.CharField(max_length=100)
  employee_count=models.IntegerField(default=0)

  def save_department(self):
    self.save()

  @classmethod
  def get_all_departments(cls):
    return Department.objects.all()
  
  @classmethod
  def get_department_by_id(cls,id):
    return cls.objects.filter(id=id).first()

  def __str__(self):
    return self.department_name

class Employee(models.Model):
  employee_fname=models.CharField(max_length=50)
  employee_lname=models.CharField(max_length=50)
  department=models.ForeignKey(Department,related_name='employees',on_delete=models.CASCADE)
  is_active=models.BooleanField(default=True)
  created_at=models.DateTimeField(auto_now_add=True)
  updated_on=models.DateTimeField(auto_now=True)

  def save_employee(self):
    self.save()
    return self


  def deactivate_employee(self):
    self.is_active=False
    self.save()
    return self
  
  def update_employee(self,**kwargs):
    for key,value in kwargs.items():
      setattr(self,key,value)
    self.save()
    return self

  @classmethod
  def get_all_employees(cls):
    return cls.objects.all()

  def __str__(self):
    return f"{self.employee_fname}  {self.employee_lname}"

class Allocation(models.Model):
  employee_allocated=models.ForeignKey(Employee,related_name='employee',on_delete=models.CASCADE)
  equipment_allocated=models.ForeignKey(Equipment,related_name='equipment',on_delete=models.CASCADE)
  allocation_date=models.DateField(auto_now_add=True)
  is_returned=models.BooleanField(default=False)
  date_returned=models.DateTimeField(default=None,null=True)
  notes=models.CharField(max_length=500,default=None,null=True)

  def save_allocation(self):
    self.save()
    return self

  def __str__(self):
    return self.date_returned


class SupplyConsumption(models.Model):
  supply=models.OneToOneField(Equipment,related_name='supply',on_delete=models.CASCADE)
  consumer=models.ForeignKey(Equipment,related_name='consumer',on_delete=models.CASCADE)
  installation_date=models.DateTimeField(auto_now_add=True)
  notes=models.CharField(max_length=500,default=None,null=True)

  def save_supply_consumption(self):
    self.save()

  def __str__(self):
    return self.installation_date
