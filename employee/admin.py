from django.contrib import admin
from drfaddons.admin import CreateUpdateAdmin

from employee.models import Employee


class EmployeeDocumentInLine(admin.TabularInline):
    from .models import EmployeeDocument

    model = EmployeeDocument
    extra = 0
    fk_name = 'employee'


class EmployeeAdmin(CreateUpdateAdmin):
    inlines = (EmployeeDocumentInLine, )


admin.site.register(Employee, EmployeeAdmin)
