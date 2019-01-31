from django import forms
from .import models
import datetime
from django.utils.text import slugify



class get_std_sec_maxattendance_form(forms.Form):

	QUARTER_CHOICES = [(1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),]
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-1,year+1) ]
	standard = forms.CharField(max_length = 3)
	section = forms.CharField(max_length = 3)
	max_attendance = forms.IntegerField()
	quarter = forms.ChoiceField(choices = QUARTER_CHOICES)
	session = forms.ChoiceField(choices = SESSION_CHOICES)


class get_attendance_form(forms.ModelForm):

	roll_no = forms.IntegerField()

	class Meta():
		model = models.Attendance
		fields = ['attendance']


class get_sc_detail_form(forms.Form):
	
	SUBJECT_CHOICES = [(slugify(u['name']),u['name']) for u in models.Subject.objects.all().filter(verified__iexact=1).values('name')]
	QUARTER_CHOICES = [(1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),]
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-1,year+1) ]
	standard = forms.CharField(max_length = 3)
	section = forms.CharField(max_length = 3)
	max_score = forms.IntegerField()
	quarter = forms.ChoiceField(choices = QUARTER_CHOICES)
	session = forms.ChoiceField(choices = SESSION_CHOICES)
	subject = forms.ChoiceField(choices = SUBJECT_CHOICES)

class get_score_form(forms.ModelForm):

	roll_no = forms.IntegerField()

	class Meta():
		model = models.Score
		fields = ['score']





	

