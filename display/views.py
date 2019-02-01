from django.shortcuts import render, redirect
from django.urls import reverse
from .import forms
from django.contrib.auth.decorators import login_required
from schools import models as s_models
from academics import models as ac_models


# Create your views here.

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





	