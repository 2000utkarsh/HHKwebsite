from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

class School(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	reg_code = models.CharField(max_length=20)

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







