from django.db import models
from accounts.models import User
from complaints.models import Complaint

# Create your models here.

class Verification(models.Model):
	verified_user = 	models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'verified_user')
	verified_by = 		models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'verified_by')

	def __str__(self):
		return str(self.verified_user) + ' verified by ' + str(self.verified_by)

class Contact_Request(models.Model):
	requested_by = 		models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'contact_requested_by')
	requested_user = 	models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'contact_requested_user')
	request_note = 		models.TextField(null = True, blank = True)

	def __str__(self):
		return str(self.requested_user) + ' requested by ' + str(self.requested_by)

class Complaint_Request(models.Model):
	complaint = 		models.ForeignKey(Complaint, null = True, on_delete = models.CASCADE, related_name = 'complaint_request')
	requested_by = 		models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'complaint_requested_by')
	requested_user = 	models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'complaint_requested_user')
	request_note = 		models.TextField(null = True, blank = True)

	def __str__(self):
		return str(self.requested_user) + ' requested by ' + str(self.requested_by)

class Contact_Permission(models.Model):
	permitted_user = 	models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'permitted_user_permissions')
	permitted_by = 		models.ForeignKey(User, null = True, on_delete = models.CASCADE, related_name = 'permitted_by_permissions')

	def __str__(self):
		return str(self.permitted_user) + ' permitted by ' + str(self.permitted_by)