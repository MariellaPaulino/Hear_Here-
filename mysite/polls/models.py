from django.db import models

# Create your models here.

class Hearing_Center(models.Model):
	hearing_center_id = models.CharField(max_length=120)
	address = models.CharField(max_length=120)
	zip_code = models.CharField(max_length=5)
	zip_code = models.ForeignKey(Clients)
	specialties = models.IntegerField()
	email = models.CharField(max_length=120)
	telephone = models.CharField(max_length=120)
	Twitter = models.CharField(max_length=120)
	Facebook = models.CharField(max_length=120)
	Youtube = models.CharField(max_length=120)
	Chat_Services = models.BooleanField()
	Online_Scheduling = models.BooleanField()

class Care_Providers(models.Model):
	care_provider_id = models.CharField(max_length=120)
	***care_provider_id = models.ForeignKey (Hearing Center)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	certifications = models.IntegerField()
	specialties = models.IntegerField()
	languages = models.IntegerField()
	sex = models.IntegerField()
	places_of_work = models.CharField(max_length=500)
	email = models.CharField(max_length=120)
	telephone = models.CharField(max_length=120)
	Twitter = models.CharField(max_length=120)
	
class Clients(models.Model):
	client_id = models.CharField(max_length=120)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	email = models.CharField(max_length=120)
	child_had_services_before = models.BooleanField()
	interests = models.IntegerField()
	insurance = models.IntegerField()

