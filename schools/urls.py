from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
	path('new/', views.CreateSchool.as_view(), name = 'create'),
	path('list/', views.SchoolList.as_view(), name = 'all'),
]