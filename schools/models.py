from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

class School(models.Model):

	user = models.OneToOneField(User,related_name = 'school', on_delete=models.CASCADE)

	reg_code = models.CharField(max_length=20, unique=True)

	name = models.CharField(max_length=167)

	head = models.CharField(max_length=50)

	address = models.TextField()

	contact = models.PositiveIntegerField()

	created_at = models.DateTimeField(auto_now=True)

	verified = models.BooleanField(default=False)

	def __str__(self):
		return self.reg_code

	
		##### CHANGE THIS #######

	def get_absolute_url(self):
		return reverse('home')


	class Meta():
		ordering = ['name']


class Student(models.Model):

	school = models.ForeignKey('schools.School', related_name='students', on_delete = models.CASCADE)

	roll_no = models.PositiveIntegerField()

	name = models.CharField(max_length=50)

	
	############ MAKE DROPDOWn #############
	standard = models.CharField(max_length=3)

	section = models.CharField(max_length=2)

	f_name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('schools:create_student', kwargs = {'username':self.username})











