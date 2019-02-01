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
# Create your views here.


class CreateSchool(LoginRequiredMixin, generic.FormView):
    template_name = 'schools/school_form.html'
    form_class = forms.SchoolForm
    # success_url = reverse_lazy('event:all')
    success_url = reverse_lazy('emails:send')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)



class SchoolList(generic.ListView):
    model = models.School
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(verified__iexact = 1)



class SchoolDetail(LoginRequiredMixin,generic.DetailView):
    model = models.School

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk__iexact = self.kwargs.get("pk"))



class UpdateSchool(generic.UpdateView,LoginRequiredMixin):
    template_name = 'schools/school_update_form.html'
    success_url = reverse_lazy("schools:all")
    form_class = forms.UpdateSchoolForm
    model = models.School


# class DeleteEvent(LoginRequiredMixin, generic.DeleteView):
#     model = models.Event
#     success_url = reverse_lazy("event:all")

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         return queryset.filter(user_id=self.request.user.id)

#     def delete(self, *args, **kwargs):
#         messages.success(self.request, "Event Deleted")
#         return super().delete(*args, **kwargs)



######################## STUDENT VIEW ########################



@login_required
def create_student(request,pk):
    school = get_object_or_404(models.School,pk=pk)

    if request.method == 'POST':
        form = forms.CreateStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.school = school
            student.save()
            data={'standard':form.cleaned_data['standard'],'section':form.cleaned_data['section']}
            form = forms.CreateStudentForm(initial=data)
            return render(request,'schools/create_student_form.html',{'form':form})
    else:
        form = forms.CreateStudentForm()
    return render(request,'schools/create_student_form.html',{'form':form})

