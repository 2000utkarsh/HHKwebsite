from django.contrib import admin
from .import models

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
	list_display = ['reg_code', 'name', 'verified']
	list_filter = ['verified']



class StudentAdmin(admin.ModelAdmin):
	list_display = ['pk','roll_no', 'name', 'standard', 'section', 'school']
	list_filter = ['standard', 'section', 'school']


admin.site.register(models.School, SchoolAdmin)
admin.site.register(models.Student, StudentAdmin)

