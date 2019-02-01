from django.shortcuts import render, redirect
from django.urls import reverse
from .import forms
from django.contrib.auth.decorators import login_required
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