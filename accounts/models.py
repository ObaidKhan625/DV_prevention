from django.db import models
import random
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
	phone = models.CharField(max_length=200, unique=True, null=True, blank=True)
	email = models.CharField(max_length=200, unique=True, null=True, blank=True)
	other = models.CharField(max_length=200, null=True, blank=True)
	profile_image = models.ImageField(null=True, upload_to='profiles', blank=True)
	role = models.CharField(max_length=50, null=True, blank=True)
	
class Complaint(models.Model):
	title = models.CharField(max_length=1000, null=True)
	complaint_filer = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	description = models.TextField(null=True)
	updates = models.TextField(default="", blank=True)
	status = models.CharField(max_length=10, default='active')
	short_description = models.CharField(max_length=50, null=True, blank=True)
	request_image = models.ImageField(null=True, upload_to='customers')
	under_investigation_by = models.CharField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return self.title

"""
class Donation_made(models.Model):		
	from_user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='donation_from_user')
	to_user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name='donation_to_user')
	amount = models.PositiveIntegerField(null=True)
	note = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return (self.from_user.user_name + ' to ' + self.to_user.user_name)

"""