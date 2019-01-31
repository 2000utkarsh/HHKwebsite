from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from datetime import datetime
from .import forms

from schools import models as s_models
from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def create_attendance(request,pk):
    school = get_object_or_404(models.Student,pk=pk)

    if request.method == 'POST':
        form = forms.CreateStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.school = school
            student.save()
            form = forms.CreateStudentForm()
            return render(request,'schools/create_student_form.html',{'form':form})
    else:
        form = forms.CreateStudentForm()
    return render(request,'schools/create_student_form.html',{'form':form})


def get_std_sec_maxattendance(request, pk):
    if request.method == 'POST':
        form = forms.get_std_sec_maxattendance_form(request.POST)

        if form.is_valid():
        
            pk = pk
            standard = form.cleaned_data['standard']
            section = form.cleaned_data['section']
            max_attendance = form.cleaned_data['max_attendance']
            quarter = form.cleaned_data['quarter']
            session = form.cleaned_data['session']
            return redirect('academics:get_attendance', pk=pk, standard=standard, section=section, quarter =quarter, session=session, max_attendance=max_attendance)

    else:
        form = forms.get_std_sec_maxattendance_form()
    return render(request, 'academics/get_max_attendance.html', {'form':form})



def get_attendance(request, pk, standard, section, max_attendance, quarter, session):
    school = get_object_or_404(s_models.School, pk=pk)

    if request.method == 'POST':
        form = forms.get_attendance_form(request.POST)
        if form.is_valid():
            r_no = form.cleaned_data['roll_no']
            student = s_models.Student.objects.get(roll_no=r_no, standard=standard, section=section, school=school)
            try:
                try_object = models.Attendance.objects.get(student=student, session=session, quarter=quarter)

            except:
                attendance = form.save(commit=False)
                attendance.student = student
                attendance.session = session
                attendance.quarter = quarter
                attendance.attendance_max = max_attendance
                attendance.save()
            else:
                try_object.attendance=form.cleaned_data['attendance']
                try_object.save()

            data={'roll_no':form.cleaned_data['roll_no']+1}
            form = forms.get_attendance_form(initial=data)
            return render(request,'academics/get_attendance.html',{'form':form,'pk':pk, 'standard':standard, 'section':section, 'quarter':quarter, 'session':session, 'max_attendance':max_attendance})
    else:
        form = forms.get_attendance_form()
    return render(request, 'academics/get_attendance.html', {'form':form,'pk':pk, 'standard':standard, 'section':section, 'quarter':quarter, 'session':session, 'max_attendance':max_attendance})



def get_sc_detail(request, pk):
    if request.method == 'POST':
        form = forms.get_sc_detail_form(request.POST)

        if form.is_valid():
        
            pk = pk
            standard = form.cleaned_data['standard']
            section = form.cleaned_data['section']
            max_score = form.cleaned_data['max_score']
            quarter = form.cleaned_data['quarter']
            session = form.cleaned_data['session']
            subject = form.cleaned_data['subject']
            return redirect('academics:get_score', pk=pk, standard=standard, section=section, quarter =quarter, session=session, max_score=max_score, subject=subject)

    else:
        form = forms.get_sc_detail_form()
    return render(request, 'academics/get_max_score.html', {'form':form})



def get_score(request, pk, standard, section, max_score, quarter, session, subject):
    school = get_object_or_404(s_models.School, pk=pk)

    if request.method == 'POST':
        form = forms.get_score_form(request.POST)
        if form.is_valid():
            r_no = form.cleaned_data['roll_no']
            student = s_models.Student.objects.get(roll_no=r_no, standard=standard, section=section, school=school)
            try:
                try_object = models.Score.objects.get(student=student, session=session, quarter=quarter, subject=subject)

            except:
                score = form.save(commit=False)
                score.student = student
                score.session = session
                score.quarter = quarter
                score.score_max = max_score
                score.subject = subject
                score.save()
            else:
                try_object.score=form.cleaned_data['score']
                try_object.save()

            data={'roll_no':form.cleaned_data['roll_no']+1}
            form = forms.get_score_form(initial=data)
            return render(request,'academics/get_score.html',{'form':form,'pk':pk, 'standard':standard, 'section':section, 'quarter':quarter, 'session':session, 'max_score':max_score, 'subject':subject})
    else:
        form = forms.get_score_form()
    return render(request, 'academics/get_score.html', {'form':form,'pk':pk, 'standard':standard, 'section':section, 'quarter':quarter, 'session':session, 'max_score':max_score, 'subject':subject})
 