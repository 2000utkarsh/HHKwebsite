from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from datetime import datetime


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