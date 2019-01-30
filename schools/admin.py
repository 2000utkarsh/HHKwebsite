from django.contrib import admin
from .import models

# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
	list_display = ['reg_code', 'name', 'verified']
	list_filter = ['verified']


admin.site.register(models.School, SchoolAdmin)
