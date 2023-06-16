from django.forms import ModelForm
from .models import Complaint
import json

class ComplaintForm(ModelForm):
	class Meta:
		model = Complaint
		fields = ['complaint_title', 'complaint_description', 'complaint_place', 'complaint_request_image', 'complaint_place_geocode', 'tags']

	def save(self, commit=True):
		instance = super(ComplaintForm, self).save(commit=False)
		instance.complaint_place = instance.complaint_place_geocode['place_name']
		# instance.flag1 = 'flag1' in self.cleaned_data['multi_choice'] # etc
		if commit:
			instance.save()
		return instance