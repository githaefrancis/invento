from django.contrib import admin
from .models import Department,Employee,Equipment,SupplyConsumption,Allocation,Category
# Register your models here.

admin.site.register(Department,)
admin.site.register(Employee)
admin.site.register(Allocation)
admin.site.register(SupplyConsumption)
admin.site.register(Equipment)
admin.site.register(Category)