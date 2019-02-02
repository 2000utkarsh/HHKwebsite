from django import forms
import datetime
from schools import models as s_models
from academics import models as ac_models
from django.utils.text import slugify


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


class get_display_score_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	school_name_list = [u['name'] for u in s_models.School.objects.all().values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().values('pk')]

	SCHOOL_CHOICES = []

	for i in range(0,len(school_name_list)):
		SCHOOL_CHOICES.append((school_pk_list[i], school_name_list[i]))

	subject_name_list = [u['name'] for u in ac_models.Subject.objects.all().values('name')]
	

	SUBJECT_CHOICES = []

	for i in range(0,len(subject_name_list)):
		SUBJECT_CHOICES.append((slugify(subject_name_list[i]), subject_name_list[i]))
	

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
	subject = forms.ChoiceField(choices = SUBJECT_CHOICES)
	select_all_subject = forms.BooleanField(required=False)


class get_display_score_school_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	

	subject_name_list = [u['name'] for u in ac_models.Subject.objects.all().values('name')]
	

	SUBJECT_CHOICES = []

	for i in range(0,len(subject_name_list)):
		SUBJECT_CHOICES.append((slugify(subject_name_list[i]), subject_name_list[i]))
	

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	select_all_session = forms.BooleanField(required=False)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	select_all_quarter = forms.BooleanField(required=False)
	standard = forms.CharField(max_length = 20, required=False, initial="Standard")
	select_all_standard = forms.BooleanField(required=False)
	section = forms.CharField(max_length = 20, required=False, initial="Section")
	select_all_section = forms.BooleanField(required=False)
	subject = forms.ChoiceField(choices = SUBJECT_CHOICES)
	select_all_subject = forms.BooleanField(required=False)

#################FORMS FOR ATTENDANCE GRAPHS################

class get_analysis_type_form(forms.Form):
	TYPE_CHOICES= [
		(slugify('All Students Of a particular section'), 'All Students Of a particular section'),
		(slugify('All Students Of a particular standard'), 'All Students Of a particular standard'),
		(slugify('Section wise of a particular standard'), 'Section wise of a particular standard'),
		(slugify('School Wise for particular quarter and session'), 'School Wise for particular quarter and session'),		
		(slugify('Class Wise of a particular school'), 'Class Wise of a particular school'),
		(slugify('Quarter wise of a particular school'), 'Quarter wise of a particular school'),
		(slugify('Session wise of a particular school'), 'Session wise of a particular school'),
	]

	type = forms.ChoiceField(choices=TYPE_CHOICES)


class get_analysis_type1_requirement_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	school_name_list = [u['name'] for u in s_models.School.objects.all().values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().values('pk')]

	SCHOOL_CHOICES = []

	for i in range(0,len(school_name_list)):
		SCHOOL_CHOICES.append((school_pk_list[i], school_name_list[i]))
	

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	school = forms.ChoiceField(choices= SCHOOL_CHOICES)
	standard = forms.CharField(max_length = 20, required=False, initial="Standard")
	section = forms.CharField(max_length = 20, required=False, initial="Section")


class get_analysis_type2_requirement_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	school_name_list = [u['name'] for u in s_models.School.objects.all().values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().values('pk')]

	SCHOOL_CHOICES = []

	for i in range(0,len(school_name_list)):
		SCHOOL_CHOICES.append((school_pk_list[i], school_name_list[i]))
	

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	school = forms.ChoiceField(choices= SCHOOL_CHOICES)
	standard = forms.CharField(max_length = 20, required=False, initial="Standard")


class get_analysis_type4_requirement_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)


class get_analysis_type5_requirement_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	school_name_list = [u['name'] for u in s_models.School.objects.all().values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().values('pk')]

	SCHOOL_CHOICES = []

	for i in range(0,len(school_name_list)):
		SCHOOL_CHOICES.append((school_pk_list[i], school_name_list[i]))

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	school = forms.ChoiceField(choices= SCHOOL_CHOICES)


class get_analysis_type6_requirement_form(forms.Form):

	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	school_name_list = [u['name'] for u in s_models.School.objects.all().values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().values('pk')]

	SCHOOL_CHOICES = []

	for i in range(0,len(school_name_list)):
		SCHOOL_CHOICES.append((school_pk_list[i], school_name_list[i]))

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	school = forms.ChoiceField(choices= SCHOOL_CHOICES)


class get_analysis_type7_requirement_form(forms.Form):

	school_name_list = [u['name'] for u in s_models.School.objects.all().values('name')]
	school_pk_list = [u['pk'] for u in s_models.School.objects.all().values('pk')]

	SCHOOL_CHOICES = []

	for i in range(0,len(school_name_list)):
		SCHOOL_CHOICES.append((school_pk_list[i], school_name_list[i]))

	school = forms.ChoiceField(choices= SCHOOL_CHOICES)

#############################FORM FOR ATTENDANCE GRAPHS BY SCHOOL#####################

class get_analysis_type_school_form(forms.Form):
	TYPE_CHOICES= [
		(slugify('All Students Of a particular section'), 'All Students Of a particular section'),
		(slugify('All Students Of a particular standard'), 'All Students Of a particular standard'),
		(slugify('Section wise of a particular standard'), 'Section wise of a particular standard'),
		(slugify('Class Wise of a particular school'), 'Class Wise of a particular school'),
		(slugify('Quarter wise of a particular school'), 'Quarter wise of a particular school'),
		(slugify('Session wise of a particular school'), 'Session wise of a particular school'),
	]

	type = forms.ChoiceField(choices=TYPE_CHOICES)

class get_analysis_type1_requirement_school_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	
	standard = forms.CharField(max_length = 20, required=False, initial="Standard")
	section = forms.CharField(max_length = 20, required=False, initial="Section")

class get_analysis_type2_requirement_school_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 
	

	session = forms.ChoiceField(choices = SESSION_CHOICES)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)
	standard = forms.CharField(max_length = 20, required=False, initial="Standard")

class get_analysis_type5_requirement_school_form(forms.Form):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 


	session = forms.ChoiceField(choices = SESSION_CHOICES)
	quarter = forms.ChoiceField(choices= QUARTER_CHOICES)

class get_analysis_type6_requirement_school_form(forms.Form):

	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 


	session = forms.ChoiceField(choices = SESSION_CHOICES)
