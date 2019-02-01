from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
	path('school_detail/<int:pk>/<slug:username>/', views.SchoolDetail.as_view(), name='school_detail'),
	path('new/', views.CreateSchool.as_view(), name = 'create'),
	path('list/', views.SchoolList.as_view(), name = 'all'),
	path('update/<int:pk>/', views.UpdateSchool.as_view(), name = 'update'),
	path('create_student/<int:pk>', views.create_student, name='create_student'),
]