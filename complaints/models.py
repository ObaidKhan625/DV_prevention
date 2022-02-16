from django.db import models
from accounts.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Complaint(models.Model):
	complaint_title = 					models.CharField(max_length = 1000, null = True)
	complaint_filer = 					models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	complaint_description = 			models.TextField(null = True)
	complaint_status = 					models.CharField(max_length = 10, default = 'active')
	complaint_request_image = 			models.ImageField(null = True, blank = True, upload_to = 'complaints', default = 'complaints/default-image.jpg')
	complaint_place = 					models.CharField(max_length = 1000, null = True)
	complaint_under_investigation_by = 	models.CharField(max_length = 1000, null = True, blank = True)
	complaint_upvotes = 				models.IntegerField(default = 0)
	complaint_upvotes_users = 			models.TextField(default=',', blank = True)
	complaint_downvotes_users = 		models.TextField(default=',', blank = True)
	tags = TaggableManager()

	def __str__(self):
		return self.complaint_title

class Message(models.Model):
	message_user = 			models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	message_complaint = 	models.ForeignKey(Complaint, null = True, on_delete = models.CASCADE)
	message_type = 			models.CharField(max_length = 50, default = "comment")
	message_content = 		models.CharField(max_length = 1000, null = True)

	def __str__(self):
		return self.message_user + " message on " + self.message_complaint

class Investigation(models.Model):
	investigation_complaint =		models.ForeignKey(Complaint, null = True, on_delete = models.CASCADE)
	investigation_in_charge = 		models.ForeignKey(User, null = True, on_delete = models.CASCADE)