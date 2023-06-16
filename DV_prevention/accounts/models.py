from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
# Create your models here.

class User(AbstractUser):
	role_choices = (
		('Normal user/Victim', 'Normal user/Victim'), 
		('NGO/Activist/Mod', 'NGO/Activist/Mod'),
	)
	user_phone = 				models.CharField(max_length = 200, unique = True, null = True, blank = True)
	user_other =  				models.TextField(null = True, blank = True)
	user_profile_image =  		models.ImageField(null = True, upload_to = 'profiles', default = 'profiles/default-image.jpg')
	user_role = 				models.CharField(max_length = 50, null = True, choices = role_choices)
	user_complaints_solved = 	models.PositiveIntegerField(default = 0)
	user_description = 			models.TextField(null = True, blank = True)
	user_place = 				models.CharField(max_length = 1000, null = True, blank = True)
	user_place_geocode = 		models.JSONField(null = True, blank = True)
	user_notifications = 		models.PositiveIntegerField(default = 0)
	slug = 						models.SlugField(unique=True, max_length=100, default='some string')

	def __str__(self):
		return str(self.username)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.username)
		super(User, self).save(*args, **kwargs)

class User_Document(models.Model):
	user_name = 			models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'user_documents')
	user_file = 			models.ImageField(null = True, upload_to = 'identity')
	
	def __str__(self):
		return str(self.user_file)

class Rating(models.Model):
	rating_from = 			models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name='rating_from')
	rating_to = 			models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name='rating_to')
	rating_score = 			models.FloatField(default = 0.0)

	def __str__(self):
		return str(self.rating_from) + " to " + str(self.rating_to)