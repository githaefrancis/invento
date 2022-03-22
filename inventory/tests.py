
from django.test import TestCase
from .models import Allocation, Category, Department, Employee, SupplyConsumption,Equipment
# Create your tests here.
class EmployeeTest(TestCase):
  '''
  EmployeeTest class to test the behaviour of the employee model
  '''
  def setUp(self):
    self.new_department=Department(department_name='IT',department_description='Tech department')
    self.new_employee=Employee(employee_fname='Francis',employee_lname='G',department=self.new_department)


  def test_instance(self):
    self.assertTrue(isinstance(self.new_employee,Employee))

  def test_save_employee(self):
    self.new_department.save_department()
    self.new_employee.save_employee()
    self.assertTrue(len(Employee.objects.all())>0)

  def test_deactivate_employee(self):
    self.new_department.save_department()
    self.new_employee.save_employee()
    self.target_employee=Employee.objects.first()
    self.result_employee=self.target_employee.deactivate_employee()
    self.assertEqual(self.result_employee.is_active,False)
  

  def test_update_employee(self):
    self.new_department.save_department()
    self.new_employee.save_employee()
    self.target_employee=Employee.objects.first()
    self.updated_employee=self.target_employee.update_employee(employee_lname='githae')
    self.assertEqual(self.updated_employee.employee_lname,'githae')
  
class DepartmentTest(TestCase):
  def setUp(self):
    self.new_department=Department(department_name='IT',department_description='Tech department')


  def test_instance(self):
    self.assertTrue(isinstance(self.new_department,Department))

  def test_save_department(self):
    self.new_department.save_department()
    self.assertTrue(len(Department.objects.all())>0)


class CategoryTest(TestCase):
  def setUp(self):
    self.new_category=Category(category_name='Laptop',category_description='personal computers')


  def test_instance(self):
    self.assertTrue(isinstance(self.new_category,Category))


  def save_category(self):
    self.new_category.save_category()
    self.assertTrue(len(Category.objects.all())>0)

class EquipmentTest(TestCase):
  def setUp(self):
    self.new_category=Category(category_name='Laptop',category_description='personal computers')
    self.new_equipment=Equipment(equipment_name='Hp Laptop',equipment_serial_number='67888FSD',equipment_code=123,equipment_model='Probook 14',category=self.new_category)


  def save_equipment(self):
    self.new_category.save_category()
    self.new_equipment.save_equipment()
    self.assertTrue(len(Equipment.objects.all())>0) 

class AllocationTest(TestCase):
  

  def setUp(self):
    self.new_category=Category(category_name='Laptop',category_description='personal computers')
    self.new_equipment=Equipment(equipment_name='Hp Laptop',equipment_serial_number='67888FSD',equipment_code=123,equipment_model='Probook 14',category=self.new_category)
    self.new_department=Department(department_name='IT',department_description='Tech department')
    self.new_employee=Employee(employee_fname='Francis',employee_lname='G',department=self.new_department)
    self.new_allocation=Allocation(employee_allocated=self.new_employee,equipment_allocated=self.new_equipment)
 
  def test_save_allocation(self):
    self.new_category.save_category()
    self.new_equipment.save_equipment()
    self.new_department.save_department()
    self.new_employee.save_employee()
    self.new_allocation.save_allocation()

    self.assertTrue(len(Allocation.objects.all())>0)

class SupplyConsumptionTest(TestCase):
  def setUp(self):
    self.new_category=Category(category_name='Laptop',category_description='personal computers')
    self.accessory_category=Category(category_name='accessory',category_description='computers accessory')
      
    self.new_equipment=Equipment(equipment_name='Hp Laptop',equipment_serial_number='67888FSD',equipment_code=123,equipment_model='Probook 14',category=self.new_category)
    self.new_accessory=Equipment(equipment_name='battery',equipment_serial_number='67888F6666SD',equipment_code=123332,equipment_model='hp',category=self.accessory_category)

  def test_save_supply_consumption(self):
      
    self.new_supply_consumption=SupplyConsumption(supply=self.new_accessory,consumer=self.new_equipment)
    self.new_category.save_category()
    self.accessory_category.save_category()
    self.new_equipment.save_equipment()
    self.new_accessory.save_equipment()
    self.new_supply_consumption.save_supply_consumption()

    self.assertTrue(len(SupplyConsumption.objects.all())>0)


