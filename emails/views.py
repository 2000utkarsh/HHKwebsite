from django.shortcuts import render
from django.core.mail import send_mail
from . import models
# Create your views here.

def sendEmail(request):
	email_dict = models.Receiver.objects.all().values('email')
	email_list = [u['email'] for u in email_dict]
	send_mail("HHK, Pending School Verification Request",'A new school is registered. Please have a look at it and verify it as soon as possible','testemaildj@yahoo.com',email_list,fail_silently = False)
	return render(request,'emails/email_sent.html')



def sendSubEmail(request):
	email_dict = models.Receiver.objects.all().values('email')
	email_list = [u['email'] for u in email_dict]
	send_mail("HHK, Pending Subject Verification Request",'A new subject is registered. Please have a look at it and verify it as soon as possible','testemaildj@yahoo.com',email_list,fail_silently = False)
	return render(request,'emails/email_sub_sent.html')