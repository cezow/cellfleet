from django.contrib import admin
from .models import Employee, MobileNumber, Device, Supplier
from import_export.admin import ImportExportModelAdmin


class CellfleetEmployee(ImportExportModelAdmin):
    list_display = ('first_name', 'second_name', 'email', 'mpk', 'position')


class CellfleetMobileNumber(ImportExportModelAdmin):
    list_display = ('number', 'sim', 'pin', 'puk', 'tariff', 'date_added', 'event_date', 'employee')


class CellfleetDevice(ImportExportModelAdmin):
    list_display = ('mark', 'model', 'serial_number', 'price', 'warranty', 'delivery_date', 'event_date')


admin.site.register(Employee, CellfleetEmployee)
admin.site.register(MobileNumber, CellfleetMobileNumber)
admin.site.register(Device, CellfleetDevice)
admin.site.register(Supplier)


