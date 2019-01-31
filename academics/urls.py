from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'academics'

urlpatterns = [
	path('get_std_sec_maxattendance/<int:pk>/', views.get_std_sec_maxattendance, name = 'get_std_sec_maxattendance'),
	path('get_attendance/<int:pk>/<slug:standard>/<slug:section>/<slug:quarter>/<slug:session>/<int:max_attendance>/', views.get_attendance, name = 'get_attendance'),
	
]