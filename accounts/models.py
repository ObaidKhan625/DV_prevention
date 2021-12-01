from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	role_choices = (
		('Normal user/Victim', 'Normal user/Victim'), 
		('NGO/Activist/Mod', 'NGO/Activist/Mod'),
	)
	user_phone = 				models.CharField(max_length = 200, unique = True, null = True, blank = True)
	user_other =  				models.TextField(max_length = 200, null = True, blank = True)
	user_profile_image =  		models.ImageField(null = True, upload_to = 'profiles', default = 'profiles/default-image.jpg')
	user_role = 				models.CharField(max_length = 50, null = True, choices = role_choices)
	user_description = 			models.TextField(null = True, blank = True)

class User_Document(models.Model):
	user_name = 			models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'user_documents')
	user_file = 			models.ImageField(null = True, upload_to = 'identity')
	user_file_thumbnail = 	models.ImageField(null = True, upload_to = 'profiles', default = 'profiles/default-image.jpg')
	
	def __str__(self):
		return str(self.user_file)