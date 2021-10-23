from django.forms import ModelForm
from accounts.models import Complaint

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = ['title', 'description', 'request_image']