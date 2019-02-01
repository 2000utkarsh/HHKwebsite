from django import forms
import datetime
from schools import models as s_models


class get_display_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	school_name_list = [u['name'] for u in s_models.School.objects.all().values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().values('pk')]

	SCHOOL_CHOICES = []

	for i in range(0,len(school_name_list)):
		SCHOOL_CHOICES.append((school_pk_list[i], school_name_list[i]))
	

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	select_all_session = forms.BooleanField(required=False)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	select_all_quarter = forms.BooleanField(required=False)
	school = forms.ChoiceField(choices= SCHOOL_CHOICES)
	select_all_school = forms.BooleanField(required=False)
	standard = forms.CharField(max_length = 20, required=False, initial="Standard")
	select_all_standard = forms.BooleanField(required=False)
	section = forms.CharField(max_length = 20, required=False, initial="Section")
	select_all_section = forms.BooleanField(required=False)


class get_display_school_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 
	session = forms.ChoiceField(choices = SESSION_CHOICES)
	select_all_session = forms.BooleanField(required=False)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	select_all_quarter = forms.BooleanField(required=False)
	standard = forms.CharField(max_length = 20, required=False, initial="Standard")
	select_all_standard = forms.BooleanField(required=False)
	section = forms.CharField(max_length = 20, required=False, initial="Section")
	select_all_section = forms.BooleanField(required=False)