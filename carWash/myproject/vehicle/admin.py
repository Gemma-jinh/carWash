from django.contrib import admin
from .models import Vehicle
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_number', 'model') #Admin 페이지에서 보일 필드 설정
