from django.db import models
from schools import models as s_models

# Create your models here.

class Attendance(models.Model):

	QUARTER_CHOICES = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
    )

	student = models.ForeignKey('s_models.Student', related_name='attendances', on_delete = models.CASCADE)
	session = models.CharField(max_length = 15)
	quarter = models.PositiveIntegerField(choices=QUARTER_CHOICES)


	##########CONSTRAINT###########
	attendance_max = models.PositiveIntegerField()
	attendance = models.PositiveIntegerField()

	
	def __str__(self):
		return f'{self.session} {self.quarter}'



class Score(models.Model):
	QUARTER_CHOICES = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Fourth'),
    )

	student = models.ForeignKey('s_models.Student', related_name='attendances', on_delete = models.CASCADE)
	session = models.CharField(max_length = 15)
	quarter = models.PositiveIntegerField(choices=QUARTER_CHOICES)

	score_max = models.PositiveIntegerField()
	score = models.PositiveIntegerField()


