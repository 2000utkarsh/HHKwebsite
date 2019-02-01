from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'display'

urlpatterns = [
	path('get_display/', views.get_display, name = 'get_display'),
	path('get_display_school/', views.get_display_school, name = 'get_display_school'),
	path('display_attendance_stats/<slug:session>/<int:select_all_session>/<slug:quarter>/<int:select_all_quarter>/<int:school>/<int:select_all_school>/<slug:standard>/<int:select_all_standard>/<slug:section>/<int:select_all_section>/', views.display_attendance_stats, name = 'display_attendance_stats'),
]

