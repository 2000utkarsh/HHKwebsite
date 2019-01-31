from django.db import models
from schools import models as s_models
import datetime


# Create your models here.

class Attendance(models.Model):

	QUARTER_CHOICES = ((1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),)
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1)] 
	student = models.ForeignKey('schools.Student', related_name='attendances', on_delete = models.CASCADE)
	session = models.CharField(max_length = 15, choices=SESSION_CHOICES)
	quarter = models.PositiveIntegerField(choices=QUARTER_CHOICES)

	

	


	##########CONSTRAINT###########
	attendance_max = models.PositiveIntegerField()
	attendance = models.PositiveIntegerField()

	
	def __str__(self):
		return f'{self.session} {self.quarter}'


	class Meta():
		unique_together = ["student", "session", "quarter"]



class Score(models.Model):
	
	QUARTER_CHOICES = [(1, 'First'),(2, 'Second'),(3, 'Third'),(4, 'Fourth'),]
	year = datetime.datetime.now().year
	SESSION_CHOICES = [(f'{r}-{r+1}',f'{r}-{r+1}') for r in range(year-3,year+1) ]
	student = models.ForeignKey('schools.Student', related_name='scores', on_delete = models.CASCADE)
	session = models.CharField(max_length = 15, choices=SESSION_CHOICES)
	quarter = models.PositiveIntegerField(choices=QUARTER_CHOICES)
	subject = models.CharField(max_length=50)
	score_max = models.PositiveIntegerField()
	score = models.PositiveIntegerField()

	def __str__(self):
		return f'{self.session} {self.quarter}'


class Subject(models.Model):
	name = models.CharField(max_length=50)
	verified = models.BooleanField(default=False)

	def __str__(self):
		return self.name