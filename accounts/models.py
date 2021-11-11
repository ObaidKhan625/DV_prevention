from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.

class User(AbstractUser):
	role_choices = (
		('Normal user/Victim', 'Normal user/Victim'), 
		('NGO/Activist/Mod', 'NGO/Activist/Mod'),
	)
	user_phone = 				models.CharField(max_length = 200, unique = True, null = True, blank = True)
	email = 					models.CharField(max_length = 200, unique = True, null = True, blank = True)
	user_other =  				models.CharField(max_length = 200, null = True, blank = True)
	user_profile_image =  		models.ImageField(null = True, upload_to = 'profiles', blank = True)
	user_role = 				models.CharField(max_length = 50, null = True, choices = role_choices)
	user_description = 			models.TextField(null = True, blank = True)
	
class Complaint(models.Model):
	complaint_title = 					models.CharField(max_length = 1000, null = True)
	complaint_filer = 					models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	complaint_description = 			models.TextField(null = True)
	complaint_status = 					models.CharField(max_length = 10, default = 'active')
	complaint_request_image = 			models.ImageField(null = True, blank = True, upload_to = 'complaints', default = 'complaints/default-image.jpg')
	complaint_place = 					models.CharField(max_length = 1000, null = True)
	complaint_under_investigation_by = 	models.CharField(max_length = 1000, null = True, blank = True)

	def __str__(self):
		return self.title

class Message(models.Model):
	message_user = 			models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	message_complaint = 	models.ForeignKey(Complaint, null = True, on_delete = models.CASCADE)
	message_type = 			models.CharField(max_length = 50, default = "comment")
	message_content = 		models.CharField(max_length = 1000, null = True)

class User_Documents(models.Model):
	user_name = 			models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	user_files = 			models.ImageField(null = True, upload_to = 'identity')
	
	def __str__(self):
		return str(self.user_name)