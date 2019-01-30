from django import forms
from .import models

class SchoolForm(forms.ModelForm):

	class Meta():
		model = models.School
		exclude = ['user', 'created_at', 'verified']


class UpdateSchoolForm(forms.ModelForm):

	class Meta():
		model = models.School
		exclude = ['user', 'created_at', 'verified', 'name', 'reg_code']


class CreateStudentForm(forms.ModelForm):

	class Meta():
		model = models.Student
		exclude = ['school']



