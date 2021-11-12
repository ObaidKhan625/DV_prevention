from django.forms import ModelForm
from .models import Complaint

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = ['complaint_title', 'complaint_description', 'complaint_place', 'complaint_request_image']