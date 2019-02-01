from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'academics'

urlpatterns = [
	
	path('create_subject/', views.CreateSubject.as_view(), name='create_subject'),
	path('get_std_sec_maxattendance/<int:pk>/', views.get_std_sec_maxattendance, name = 'get_std_sec_maxattendance'),
	path('get_attendance/<int:pk>/<slug:standard>/<slug:section>/<slug:quarter>/<slug:session>/<int:max_attendance>/', views.get_attendance, name = 'get_attendance'),
	path('get_sc_detail/<int:pk>/', views.get_sc_detail, name = 'get_sc_detail'),
	path('get_score/<int:pk>/<slug:standard>/<slug:section>/<slug:quarter>/<slug:session>/<int:max_score>/<slug:subject>/', views.get_score, name = 'get_score'),
	
]