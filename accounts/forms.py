from django import forms
from .models import User, User_Documents

class ProfileUpdationForm(forms.ModelForm):

	token = forms.CharField(
		widget=forms.HiddenInput())
	class Meta:
		model = User
		fields = ['username', 'user_phone', 'email', 'user_other', 'user_profile_image']

class User_Documents_Form(forms.ModelForm):
	class Meta:
		model = User_Documents
		fields = ['user_files']