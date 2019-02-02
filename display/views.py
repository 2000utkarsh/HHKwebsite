from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
import math


import json

from .import forms
from schools import models as s_models
from academics import models as ac_models


# Create your views here.
################################ ATTENDANCE FOR ADMIN ####################

@login_required
def get_display(request):
	if request.method == 'POST':
		form = forms.get_display_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			select_all_session = form.cleaned_data['select_all_session']
			quarter = form.cleaned_data['quarter']
			select_all_quarter = form.cleaned_data['select_all_quarter']
			school = form.cleaned_data['school']
			select_all_school = form.cleaned_data['select_all_school']
			standard = form.cleaned_data['standard']
			select_all_standard = form.cleaned_data['select_all_standard']
			section = form.cleaned_data['section']
			select_all_section = form.cleaned_data['select_all_section']
			school = int(school)
			select_all_session=int(select_all_session)
			select_all_quarter=int(select_all_quarter)
			select_all_school=int(select_all_school)
			select_all_standard=int(select_all_standard)
			select_all_section=int(select_all_section)


			return redirect('display:display_attendance_stats', session=session, select_all_session=select_all_session, quarter=quarter, select_all_quarter=select_all_quarter, school=school, select_all_school=select_all_school, standard=standard, select_all_standard=select_all_standard,section=section, select_all_section=select_all_section)
			
	else:
		form = forms.get_display_form()

	return render(request, 'display/get_display_form.html', {'form': form})


def display_attendance_stats(request, session, select_all_session, quarter, select_all_quarter, school, select_all_school, standard, select_all_standard,section, select_all_section):
	
	if select_all_school == 0:
		student_queryset = s_models.Student.objects.all().filter(school__pk__iexact=school)
	else:
		student_queryset = s_models.Student.objects.all()

	if select_all_standard == 0:
		student_queryset = student_queryset.filter(standard__iexact=standard)

	if select_all_section == 0:
		student_queryset = student_queryset.filter(section__iexact=section)


	dict = {}
	for stud in student_queryset:
		
		attendance_queryset = ac_models.Attendance.objects.all().filter(student__pk__iexact=stud.pk)
		
		if select_all_session == 0:
			attendance_queryset = attendance_queryset.filter(session__iexact=session)
		if select_all_quarter == 0:
			attendance_queryset = attendance_queryset.filter(quarter__iexact=quarter)

		for att in attendance_queryset:
			key = f'{att.session} {att.quarter} {stud.school.name} {stud.standard} {stud.section} {stud.name}'
			value = f'{att.attendance} out of {att.attendance_max}'
			dict[key]=value



	return render(request, 'display/display_attendance.html', {'dict':dict})


############ ATTENDANCE FOR SCHOOLS ##################

@login_required
def get_display_school(request):
	if request.method == 'POST':
		form = forms.get_display_school_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			select_all_session = form.cleaned_data['select_all_session']
			quarter = form.cleaned_data['quarter']
			select_all_quarter = form.cleaned_data['select_all_quarter']
			standard = form.cleaned_data['standard']
			select_all_standard = form.cleaned_data['select_all_standard']
			section = form.cleaned_data['section']
			select_all_section = form.cleaned_data['select_all_section']
			school = request.user.school.pk
			select_all_school = 0
			select_all_session=int(select_all_session)
			select_all_quarter=int(select_all_quarter)
			select_all_standard=int(select_all_standard)
			select_all_section=int(select_all_section)


			return redirect('display:display_attendance_stats', session=session, select_all_session=select_all_session, quarter=quarter, select_all_quarter=select_all_quarter, school=school, select_all_school=select_all_school, standard=standard, select_all_standard=select_all_standard,section=section, select_all_section=select_all_section)
			
	else:
		form = forms.get_display_school_form()

	return render(request, 'display/get_display_school_form.html', {'form': form})

##################################### SCORE FOR ADMIN ################################

@login_required
def get_display_score(request):
	if request.method == 'POST':
		form = forms.get_display_score_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			select_all_session = form.cleaned_data['select_all_session']
			quarter = form.cleaned_data['quarter']
			select_all_quarter = form.cleaned_data['select_all_quarter']
			school = form.cleaned_data['school']
			select_all_school = form.cleaned_data['select_all_school']
			standard = form.cleaned_data['standard']
			select_all_standard = form.cleaned_data['select_all_standard']
			section = form.cleaned_data['section']
			select_all_section = form.cleaned_data['select_all_section']
			subject = form.cleaned_data['subject']
			select_all_subject = form.cleaned_data['select_all_subject']
			school = int(school)
			select_all_session=int(select_all_session)
			select_all_quarter=int(select_all_quarter)
			select_all_school=int(select_all_school)
			select_all_standard=int(select_all_standard)
			select_all_section=int(select_all_section)
			select_all_subject=int(select_all_subject)


			return redirect('display:display_score_stats', session=session, select_all_session=select_all_session, quarter=quarter, select_all_quarter=select_all_quarter, school=school, select_all_school=select_all_school, standard=standard, select_all_standard=select_all_standard,section=section, select_all_section=select_all_section, subject=subject, select_all_subject=select_all_subject)
			
	else:
		form = forms.get_display_score_form()

	return render(request, 'display/get_display_score_form.html', {'form': form})


def display_score_stats(request, session, select_all_session, quarter, select_all_quarter, school, select_all_school, standard, select_all_standard,section, select_all_section, subject, select_all_subject):
	
	if select_all_school == 0:
		student_queryset = s_models.Student.objects.all().filter(school__pk__iexact=school)
	else:
		student_queryset = s_models.Student.objects.all()

	if select_all_standard == 0:
		student_queryset = student_queryset.filter(standard__iexact=standard)

	if select_all_section == 0:
		student_queryset = student_queryset.filter(section__iexact=section)


	dict = {}
	for stud in student_queryset:
		
		score_queryset = ac_models.Score.objects.all().filter(student__pk__iexact=stud.pk)
		
		if select_all_session == 0:
			score_queryset = score_queryset.filter(session__iexact=session)
		if select_all_quarter == 0:
			score_queryset = score_queryset.filter(quarter__iexact=quarter)
		subject.replace("-", " ")
		if select_all_subject == 0:
			score_queryset = score_queryset.filter(subject__iexact=subject)

		for sc in score_queryset:
			key = f'{sc.session} {sc.quarter} {stud.school.name} {stud.standard} {stud.section} {stud.name} {sc.subject}'
			value = f'{sc.score} out of {sc.score_max}'
			dict[key]=value



	return render(request, 'display/display_score.html', {'dict':dict})

############ SCORE FOR SCHOOLS ##################

@login_required
def get_display_school_score(request):
	if request.method == 'POST':
		form = forms.get_display_score_school_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			select_all_session = form.cleaned_data['select_all_session']
			quarter = form.cleaned_data['quarter']
			select_all_quarter = form.cleaned_data['select_all_quarter']
			standard = form.cleaned_data['standard']
			select_all_standard = form.cleaned_data['select_all_standard']
			section = form.cleaned_data['section']
			select_all_section = form.cleaned_data['select_all_section']
			subject = form.cleaned_data['subject']
			select_all_subject = form.cleaned_data['select_all_subject']
			school = request.user.school.pk
			select_all_school = 0
			select_all_session=int(select_all_session)
			select_all_quarter=int(select_all_quarter)
			select_all_standard=int(select_all_standard)
			select_all_section=int(select_all_section)
			select_all_subject=int(select_all_subject)



			return redirect('display:display_score_stats', session=session, select_all_session=select_all_session, quarter=quarter, select_all_quarter=select_all_quarter, school=school, select_all_school=select_all_school, standard=standard, select_all_standard=select_all_standard,section=section, select_all_section=select_all_section, subject=subject, select_all_subject=select_all_subject)
			
	else:
		form = forms.get_display_score_school_form()

	return render(request, 'display/get_display_score_school_form.html', {'form': form})


##################### GRAPH VIEWS #####################

@login_required
def get_analysis_type(request):
	if request.method == 'POST':
		form = forms.get_analysis_type_form(request.POST)
		if form.is_valid():
			type = form.cleaned_data['type']
			if type == slugify('All Students Of a particular section'):
				return redirect('display:get_analysis_type1_requirement')

			if type ==slugify('All Students Of a particular standard'):
				return redirect('display:get_analysis_type2_requirement')

			if type ==slugify('Section wise of a particular standard'):
				return redirect('display:get_analysis_type3_requirement')

			if type ==slugify('School Wise for particular quarter and session'):
				return redirect('display:get_analysis_type4_requirement')

			if type ==slugify('Class Wise of a particular school'):
				return redirect('display:get_analysis_type5_requirement')

			if type == slugify('Quarter wise of a particular school'):
				return redirect('display:get_analysis_type6_requirement')

			if type ==slugify('Session wise of a particular school'):
				return redirect('display:get_analysis_type7_requirement')

	else:
		form = forms.get_analysis_type_form()

	return render(request, 'display/graphs/attendance/get_analysis_type_form.html', {'form': form})

def get_analysis_type1_requirement(request):
	if request.method == 'POST':
		form = forms.get_analysis_type1_requirement_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			school = form.cleaned_data['school']
			standard = form.cleaned_data['standard']
			section = form.cleaned_data['section']
			school = int(school)

			return redirect('display:get_analysis_type1',session=session, quarter=quarter, school=school, standard=standard, section=section ) 

	else:
		form = forms.get_analysis_type1_requirement_form()

	return render(request, 'display/graphs/attendance/get_analysis_type1_requirement_form.html',{'form':form})
def get_analysis_type1(request, session, quarter, school, standard, section):

	stud_list = [u['roll_no'] for u in s_models.Student.objects.all().filter(school__pk__iexact = school, standard__iexact=standard, section__iexact=section).values('roll_no')]
	stud_attendance = []
	dict={}
	for stud in stud_list:
		attendance_object = ac_models.Attendance.objects.get(student__roll_no__iexact=stud, student__school__pk__iexact = school, session=session, quarter=quarter, student__standard__iexact=standard, student__section__iexact=section) 
		attendance = attendance_object.attendance
		dict[stud] = attendance
		stud_attendance.append(attendance)
	data = {
			"label":stud_list,
			"value":stud_attendance
	}

	jsondata = json.dumps(data)

	return render(request, 'display/graphs/attendance/display_attendance_graph.html',{'jsondata':jsondata, 'dict':dict})


def get_analysis_type2_requirement(request):
	if request.method == 'POST':
		form = forms.get_analysis_type2_requirement_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			school = form.cleaned_data['school']
			standard = form.cleaned_data['standard']
			school = int(school)

			return redirect('display:get_analysis_type2',session=session, quarter=quarter, school=school, standard=standard, ) 

	else:
		form = forms.get_analysis_type2_requirement_form()

	return render(request, 'display/graphs/attendance/get_analysis_type2_requirement_form.html',{'form':form})
def get_analysis_type2(request, session, quarter, school, standard):

	sec_list = [u['section'] for u in s_models.Student.objects.all().filter(school__pk__iexact = school, standard__iexact=standard).values('section')]
	sec_list = sorted(list(set(sec_list)))
	max_stud_list=[]
	stud_attendance = []
	dict={}

	for sec in sec_list:
		stud_list = [u['roll_no'] for u in s_models.Student.objects.all().filter(school__pk__iexact = school, standard__iexact=standard, section__iexact=sec).values('roll_no')]
		for stud in stud_list:
			max_stud_list.append(sec+str(stud))
		for stud in stud_list:
			attendance_object_list = ac_models.Attendance.objects.all().filter(student__roll_no__iexact=stud, student__school__pk__iexact = school, session=session, quarter=quarter, student__standard__iexact=standard, student__section__iexact=sec) 
			for attendance_object in attendance_object_list:
				attendance = attendance_object.attendance
				dict[sec+str(stud)] = attendance
				stud_attendance.append(attendance)
	

	data = {
			"label":max_stud_list,
			"value":stud_attendance
	}


	jsondata = json.dumps(data)

	return render(request, 'display/graphs/attendance/display_attendance_graph.html',{'jsondata':jsondata, 'dict':dict})


def get_analysis_type3_requirement(request):
	if request.method == 'POST':
		form = forms.get_analysis_type2_requirement_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			school = form.cleaned_data['school']
			standard = form.cleaned_data['standard']
			school = int(school)

			return redirect('display:get_analysis_type3',session=session, quarter=quarter, school=school, standard=standard, ) 

	else:
		form = forms.get_analysis_type2_requirement_form()

	return render(request, 'display/graphs/attendance/get_analysis_type3_requirement_form.html',{'form':form})
def get_analysis_type3(request, session, quarter, school, standard):

	sec_list = [u['section'] for u in s_models.Student.objects.all().filter(school__pk__iexact = school, standard__iexact=standard).values('section')]
	sec_list = sorted(list(set(sec_list)))
	stud_attendance = []
	attendance=0
	dict={}

	for sec in sec_list:
		attendance_object_list = ac_models.Attendance.objects.all().filter(student__school__pk__iexact = school, session=session, quarter=quarter, student__standard__iexact=standard, student__section__iexact=sec) 
		for attendance_object in attendance_object_list:
			attendance += attendance_object.attendance
		attendance = attendance/len(attendance_object_list)
		attendance = round(attendance,3)
		dict[sec] = attendance
		stud_attendance.append(attendance)
	

	data = {
			"label":sec_list,
			"value":stud_attendance
	}


	jsondata = json.dumps(data)

	return render(request, 'display/graphs/attendance/display_attendance_graph.html',{'jsondata':jsondata, 'dict':dict})


def get_analysis_type4_requirement(request):
	if request.method == 'POST':
		form = forms.get_analysis_type4_requirement_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			return redirect('display:get_analysis_type4',session=session, quarter=quarter) 

	else:
		form = forms.get_analysis_type4_requirement_form()

	return render(request, 'display/graphs/attendance/get_analysis_type4_requirement_form.html',{'form':form})
def get_analysis_type4(request, session, quarter):

	school_list = [u['name'] for u in s_models.School.objects.all().filter(verified__iexact=1).values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().filter(verified__iexact=1).values('pk')]	
	school_list = sorted(list(set(school_list)))
	stud_attendance = []
	attendance=0
	dict={}

	for school in school_pk_list:
		attendance_object_list = ac_models.Attendance.objects.all().filter(student__school__pk__iexact = school, session=session, quarter=quarter)
		for attendance_object in attendance_object_list:
			attendance += attendance_object.attendance
		attendance = attendance/len(attendance_object_list)
		attendance = round(attendance,3)
		dict[school_list[school_pk_list.index(school)]] = attendance
		stud_attendance.append(attendance)
	

	data = {
			"label":school_list,
			"value":stud_attendance
	}


	jsondata = json.dumps(data)

	return render(request, 'display/graphs/attendance/display_attendance_graph.html',{'jsondata':jsondata, 'dict':dict})


def get_analysis_type5_requirement(request):
	if request.method == 'POST':
		form = forms.get_analysis_type5_requirement_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			school = form.cleaned_data['school']
			return redirect('display:get_analysis_type5',session=session, quarter=quarter, school=school) 

	else:
		form = forms.get_analysis_type5_requirement_form()

	return render(request, 'display/graphs/attendance/get_analysis_type5_requirement_form.html',{'form':form})
def get_analysis_type5(request, session, quarter, school):

	std_list = [u['standard'] for u in s_models.Student.objects.all().filter(school__pk__iexact = school).values('standard')]
	std_list = sorted(list(set(std_list)))
	stud_attendance = []
	attendance=0
	dict={}

	for std in std_list:
		attendance_object_list = ac_models.Attendance.objects.all().filter(student__school__pk__iexact = school, session=session, quarter=quarter, student__standard__iexact=std) 
		for attendance_object in attendance_object_list:
			attendance += attendance_object.attendance
		attendance = attendance/len(attendance_object_list)
		attendance = round(attendance,3)
		dict[std] = attendance
		stud_attendance.append(attendance)
	

	data = {
			"label":std_list,
			"value":stud_attendance
	}


	jsondata = json.dumps(data)

	return render(request, 'display/graphs/attendance/display_attendance_graph.html',{'jsondata':jsondata, 'dict':dict})

def get_analysis_type6_requirement(request):
	if request.method == 'POST':
		form = forms.get_analysis_type6_requirement_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			school = form.cleaned_data['school']
			return redirect('display:get_analysis_type6',session=session, school=school) 

	else:
		form = forms.get_analysis_type6_requirement_form()

	return render(request, 'display/graphs/attendance/get_analysis_type6_requirement_form.html',{'form':form})
def get_analysis_type6(request, session, school):

	quarter_list = ['1','2','3','4']
	quarter_name_list = ['First','Second','Third','Fourth']
	
	stud_attendance = []
	attendance=0
	dict={}

	for quarter in quarter_list:
		attendance_object_list = ac_models.Attendance.objects.all().filter(student__school__pk__iexact = school, session=session, quarter=quarter) 
		for attendance_object in attendance_object_list:
			attendance += attendance_object.attendance
		if(len(attendance_object_list)==0):
			attendance=0
		else:
			attendance = attendance/len(attendance_object_list)
		attendance = round(attendance,3)
		dict[quarter] = attendance
		stud_attendance.append(attendance)
	

	data = {
			"label":quarter_name_list,
			"value":stud_attendance
	}


	jsondata = json.dumps(data)

	return render(request, 'display/graphs/attendance/display_attendance_graph.html',{'jsondata':jsondata, 'dict':dict})

def get_analysis_type7_requirement(request):
	if request.method == 'POST':
		form = forms.get_analysis_type7_requirement_form(request.POST)
		if form.is_valid():
			school = form.cleaned_data['school']
			return redirect('display:get_analysis_type7', school=school) 

	else:
		form = forms.get_analysis_type7_requirement_form()

	return render(request, 'display/graphs/attendance/get_analysis_type7_requirement_form.html',{'form':form})
def get_analysis_type7(request, school):

	ses_list = [u['session'] for u in ac_models.Attendance.objects.all().filter(student__school__pk__iexact = school).values('session')]
	ses_list = sorted(list(set(ses_list)))
	stud_attendance = []
	attendance=0
	dict={}

	for ses in ses_list:
		attendance_object_list = ac_models.Attendance.objects.all().filter(student__school__pk__iexact = school, session=ses) 
		for attendance_object in attendance_object_list:
			attendance += attendance_object.attendance
		attendance = attendance/len(attendance_object_list)
		attendance = round(attendance,3)
		dict[ses] = attendance
		stud_attendance.append(attendance)
	

	data = {
			"label":ses_list,
			"value":stud_attendance
	}


	jsondata = json.dumps(data)

	return render(request, 'display/graphs/attendance/display_attendance_graph.html',{'jsondata':jsondata, 'dict':dict})


###################SCHOOL ATTENDANCE ANALYSIS########################
@login_required
def get_analysis_type_school(request):
	if request.method == 'POST':
		form = forms.get_analysis_type_school_form(request.POST)
		if form.is_valid():
			type = form.cleaned_data['type']
			if type == slugify('All Students Of a particular section'):
				return redirect('display:get_analysis_type1_requirement_school')

			if type ==slugify('All Students Of a particular standard'):
				return redirect('display:get_analysis_type2_requirement_school')

			if type ==slugify('Section wise of a particular standard'):
				return redirect('display:get_analysis_type3_requirement_school')

			if type ==slugify('Class Wise of a particular school'):
				return redirect('display:get_analysis_type5_requirement_school')

			if type == slugify('Quarter wise of a particular school'):
				return redirect('display:get_analysis_type6_requirement_school')

			if type ==slugify('Session wise of a particular school'):
				return redirect('display:get_analysis_type7_requirement_school')

	else:
		form = forms.get_analysis_type_school_form()

	return render(request, 'display/graphs/attendance/get_analysis_type_school_form.html', {'form': form})

def get_analysis_type1_requirement_school(request):
	if request.method == 'POST':
		form = forms.get_analysis_type1_requirement_school_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			standard = form.cleaned_data['standard']
			section = form.cleaned_data['section']
			school = request.user.school.pk

			return redirect('display:get_analysis_type1',session=session, quarter=quarter, school=school, standard=standard, section=section ) 

	else:
		form = forms.get_analysis_type1_requirement_school_form()

	return render(request, 'display/graphs/attendance/get_analysis_type1_requirement_school_form.html',{'form':form})

def get_analysis_type2_requirement_school(request):
	if request.method == 'POST':
		form = forms.get_analysis_type2_requirement_school_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			standard = form.cleaned_data['standard']
			school = request.user.school.pk

			return redirect('display:get_analysis_type2',session=session, quarter=quarter, school=school, standard=standard, ) 

	else:
		form = forms.get_analysis_type2_requirement_school_form()

	return render(request, 'display/graphs/attendance/get_analysis_type2_requirement_school_form.html',{'form':form})

def get_analysis_type3_requirement_school(request):
	if request.method == 'POST':
		form = forms.get_analysis_type2_requirement_school_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			standard = form.cleaned_data['standard']
			school = request.user.school.pk

			return redirect('display:get_analysis_type3',session=session, quarter=quarter, school=school, standard=standard, ) 

	else:
		form = forms.get_analysis_type2_requirement_school_form()

	return render(request, 'display/graphs/attendance/get_analysis_type3_requirement_school_form.html',{'form':form})

def get_analysis_type5_requirement_school(request):
	if request.method == 'POST':
		form = forms.get_analysis_type5_requirement_school_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			quarter = form.cleaned_data['quarter']
			school = request.user.school.pk
			return redirect('display:get_analysis_type5',session=session, quarter=quarter, school=school) 

	else:
		form = forms.get_analysis_type5_requirement_school_form()

	return render(request, 'display/graphs/attendance/get_analysis_type5_requirement_school_form.html',{'form':form})

def get_analysis_type6_requirement_school(request):
	if request.method == 'POST':
		form = forms.get_analysis_type6_requirement_school_form(request.POST)
		if form.is_valid():
			session = form.cleaned_data['session']
			school = request.user.school.pk
			return redirect('display:get_analysis_type6',session=session, school=school) 

	else:
		form = forms.get_analysis_type6_requirement_school_form()

	return render(request, 'display/graphs/attendance/get_analysis_type6_requirement_school_form.html',{'form':form})

def get_analysis_type7_requirement_school(request):
	school = request.user.school.pk
	return redirect('display:get_analysis_type7', school=school) 