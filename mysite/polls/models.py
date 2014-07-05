from django.db import models
from django.forms import ModelForm

INTEREST_CHOICES = (
	('hearing', 'hearing services'),
	('speech', 'speech services'),
	('advocacy', 'education advocacy'),
	('connections', 'connections with parents and students'),
)

LANGUAGE_CHOICES = (
	('Spanish','Spanish'),
	('English', 'English'),
)

SEX_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	('N', 'Not Specified')
)

class Hearing_Center(models.Model):
	address = models.CharField(max_length=120)
	zip_code = models.CharField(max_length=5)
	specialties = models.CharField(max_length=120, choices=INTEREST_CHOICES)
	# email = models.CharField(max_length=120)
	# telephone = models.CharField(max_length=120)
	# Twitter = models.CharField(max_length=120)
	# Facebook = models.CharField(max_length=120)
	# Youtube = models.CharField(max_length=120)
	# Chat_Services = models.BooleanField()
	# Online_Scheduling = models.BooleanField()

class Care_Providers(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	certifications_and_awards = models.CharField(max_length=120) 
	specialties = models.CharField(max_length=120, choices= INTEREST_CHOICES)
	languages = models.CharField(max_length=120, choices= LANGUAGE_CHOICES)
	sex = models.CharField(max_length=120, choices= SEX_CHOICES)
	# places_of_work = models.CharField(max_length=500)
	# email = models.CharField(max_length=120)
	# telephone = models.CharField(max_length=120)
	# Twitter = models.CharField(max_length=120)
	# hearing_center_id= models.ForeignKey(Hearing_Center)
	
class Clients(models.Model):
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	zip_code = models.CharField(max_length=5)
	email = models.CharField(max_length=120)
	care_provider_id = models.ForeignKey(Care_Providers)
	hearing_center_id = models.ManyToManyField(Hearing_Center)
	Interests = models.CharField(max_length=120, choices= INTEREST_CHOICES)
	languages = models.CharField(max_length=120, choices= LANGUAGE_CHOICES)
	# client_age = models.CharField(max_length=120)
	# insurance = forms.CharField(max_length=100)

