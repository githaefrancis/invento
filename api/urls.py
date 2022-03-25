from django.urls import path,re_path
from . import views

urlpatterns=[
  re_path('^employees/',views.EmployeeList.as_view()),
  re_path('^departments/$',views.DepartmentList.as_view()),
  re_path('^equipment/$',views.EquipmentList.as_view()),
  re_path('^equipment/available',views.EquipmentAvailableList.as_view()),

  re_path('^category/',views.CategoryList.as_view()),
  re_path('^allocation/$',views.AllocationList.as_view()),
  re_path('^consumption/',views.ConsumptionList.as_view()),
  re_path('^allocation/(?P<pk>[0-9]+)/$',views.AllocationDetails.as_view()),
  
  ]