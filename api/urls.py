from django.urls import path,re_path
from . import views

urlpatterns=[
  # re_path('^employees/',views.employee,name='employee'),
  re_path('^departments/$',views.DepartmentList.as_view()),
  # re_path('^equipment/',views.equipment,name='equipment'),
  # re_path('^category/',views.category,name='category'),
  # re_path('^allocation/',views.allocation,name='allocation'),
  # re_path('^consumption/',views.consumption,name='consumption'),
  
  ]