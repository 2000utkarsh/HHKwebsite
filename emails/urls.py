from django.urls import path
from . import views

app_name = 'emails'

urlpatterns = [
				
				path('send/',views.sendEmail, name='send'),
				path('send_sub/', views.sendSubEmail, name='sub_send'),
]