from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.Attendance)

admin.site.register(models.Score)

admin.site.register(models.Subject)