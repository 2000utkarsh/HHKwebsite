from django import forms
from .import models

class SchoolForm(forms.ModelForm):

	class Meta():
		model = models.School
		exclude = ['user', 'created_at', 'verified']