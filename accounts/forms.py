from django import forms
from .models import User, User_Document
import json

class User_Documents_Form(forms.ModelForm):
	class Meta:
		model = User_Document
		fields = ['user_file']

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'user_phone', 'user_other', 'email', 'user_description', 'user_profile_image', 'user_place', 'user_place_geocode']
	
	def save(self, commit=True):
		user = super(UpdateUserForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.user_phone = self.cleaned_data['user_phone']
		user.user_description = self.cleaned_data['user_description']
		if(self.cleaned_data['user_profile_image'] is not None):
			user.user_profile_image = self.cleaned_data['user_profile_image']
		if user.user_place_geocode is not None:
			user.user_place = user.user_place_geocode['place_name']
		user.user_other = self.cleaned_data['user_other']
		# user.user_profile_image = self.cleaned_data['user_profile_image']
		if commit:
			return user.save()
		else:
			return user

"""
def clean_email(self):
	user_description = self.cleaned_data.get('email')
	user_profile_image = self.cleaned_data.get('email')

	if email and User.objects.filter(email=email).exclude(username=username).count():
		raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
	return email
"""