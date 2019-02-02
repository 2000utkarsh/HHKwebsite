from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'display'

urlpatterns = [
	path('get_display/', views.get_display, name = 'get_display'),
	path('get_display_score/', views.get_display_score, name = 'get_display_score'),
	path('get_display_school_score/', views.get_display_school_score, name = 'get_display_school_score'),
	path('get_display_school/', views.get_display_school, name = 'get_display_school'),
	path('display_attendance_stats/<slug:session>/<int:select_all_session>/<slug:quarter>/<int:select_all_quarter>/<int:school>/<int:select_all_school>/<slug:standard>/<int:select_all_standard>/<slug:section>/<int:select_all_section>/', views.display_attendance_stats, name = 'display_attendance_stats'),
	path('display_score_stats/<slug:session>/<int:select_all_session>/<slug:quarter>/<int:select_all_quarter>/<int:school>/<int:select_all_school>/<slug:standard>/<int:select_all_standard>/<slug:section>/<int:select_all_section>/<slug:subject>/<int:select_all_subject>/', views.display_score_stats, name = 'display_score_stats'),


	path('graph/attendance/get_analysis_type/', views.get_analysis_type,  name='get_analysis_type'),
	path('graph/attendance/get_analysis_type1_requirement/', views.get_analysis_type1_requirement, name='get_analysis_type1_requirement'),
	path('graph/attendance/get_analysis_type1/<slug:session>/<slug:quarter>/<int:school>/<slug:standard>/<slug:section>/', views.get_analysis_type1, name='get_analysis_type1'),
	path('graph/attendance/get_analysis_type2_requirement/', views.get_analysis_type2_requirement, name='get_analysis_type2_requirement'),
	path('graph/attendance/get_analysis_type2/<slug:session>/<slug:quarter>/<int:school>/<slug:standard>/', views.get_analysis_type2, name='get_analysis_type2'),
	path('graph/attendance/get_analysis_type3_requirement/', views.get_analysis_type3_requirement, name='get_analysis_type3_requirement'),
	path('graph/attendance/get_analysis_type3/<slug:session>/<slug:quarter>/<int:school>/<slug:standard>/', views.get_analysis_type3, name='get_analysis_type3'),
	path('graph/attendance/get_analysis_type4_requirement/', views.get_analysis_type4_requirement, name='get_analysis_type4_requirement'),
	path('graph/attendance/get_analysis_type4/<slug:session>/<slug:quarter>/', views.get_analysis_type4, name='get_analysis_type4'),
	path('graph/attendance/get_analysis_type5_requirement/', views.get_analysis_type5_requirement, name='get_analysis_type5_requirement'),
	path('graph/attendance/get_analysis_type5/<slug:session>/<slug:quarter>/<int:school>/', views.get_analysis_type5, name='get_analysis_type5'),
	path('graph/attendance/get_analysis_type6_requirement/', views.get_analysis_type6_requirement, name='get_analysis_type6_requirement'),
	path('graph/attendance/get_analysis_type6/<slug:session>/<int:school>/', views.get_analysis_type6, name='get_analysis_type6'),
	path('graph/attendance/get_analysis_type7_requirement/', views.get_analysis_type7_requirement, name='get_analysis_type7_requirement'),
	path('graph/attendance/get_analysis_type7/<int:school>/', views.get_analysis_type7, name='get_analysis_type7'),


	path('graph/attendance/get_analysis_type_school/', views.get_analysis_type_school,  name='get_analysis_type_school'),
	path('graph/attendance/get_analysis_type1_requirement_school/', views.get_analysis_type1_requirement_school, name='get_analysis_type1_requirement_school'),
	path('graph/attendance/get_analysis_type2_requirement_school/', views.get_analysis_type2_requirement_school, name='get_analysis_type2_requirement_school'),
	path('graph/attendance/get_analysis_type3_requirement_school/', views.get_analysis_type3_requirement_school, name='get_analysis_type3_requirement_school'),
	path('graph/attendance/get_analysis_type5_requirement_school/', views.get_analysis_type5_requirement_school, name='get_analysis_type5_requirement_school'),
	path('graph/attendance/get_analysis_type6_requirement_school/', views.get_analysis_type6_requirement_school, name='get_analysis_type6_requirement_school'),
	path('graph/attendance/get_analysis_type7_requirement_school/', views.get_analysis_type7_requirement_school, name='get_analysis_type7_requirement_school'),



	
	path('graph/score/get_score_analysis_type/', views.get_score_analysis_type, name = 'get_score_analysis_type'),
	path('graph/score/get_score_analysis_type1/<slug:session>/<slug:quarter>/<int:school>/<slug:standard>/<slug:section>/<slug:subject>/', views.get_score_analysis_type1, name='get_score_analysis_type1'),
	path('graph/score/get_score_analysis_type1_requirement/', views.get_score_analysis_type1_requirement, name='get_score_analysis_type1_requirement'),
	path('graph/score/get_score_analysis_type2/<slug:session>/<slug:quarter>/<int:school>/<slug:standard>/<slug:subject>/', views.get_score_analysis_type2, name='get_score_analysis_type2'),
	path('graph/score/get_score_analysis_type2_requirement/', views.get_score_analysis_type2_requirement, name='get_score_analysis_type2_requirement'),
	path('graph/score/get_score_analysis_type3/<slug:session>/<slug:quarter>/<int:school>/<slug:standard>/<slug:subject>/', views.get_score_analysis_type3, name='get_score_analysis_type3'),
	path('graph/score/get_score_analysis_type3_requirement/', views.get_score_analysis_type3_requirement, name='get_score_analysis_type3_requirement'),
	path('graph/score/get_score_analysis_type4/<slug:session>/<slug:quarter>/<slug:subject>/', views.get_score_analysis_type4, name='get_score_analysis_type4'),
	path('graph/score/get_score_analysis_type4_requirement/', views.get_score_analysis_type4_requirement, name='get_score_analysis_type4_requirement'),
	path('graph/score/get_score_analysis_type5/<slug:session>/<slug:quarter>/<int:school>/<slug:subject>/', views.get_score_analysis_type5, name='get_score_analysis_type5'),
	path('graph/score/get_score_analysis_type5_requirement/', views.get_score_analysis_type5_requirement, name='get_score_analysis_type5_requirement'),

]

