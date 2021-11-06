from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.

class User(AbstractUser):
	phone = 				models.CharField(max_length = 200, unique = True, null = True, blank = True)
	email = 				models.CharField(max_length = 200, unique = True, null = True, blank = True)
	other =  				models.CharField(max_length = 200, null = True, blank = True)
	profile_image =  		models.ImageField(null = True, upload_to = 'profiles', blank = True)
	role = 					models.CharField(max_length = 50, null = True, blank = True)
	
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