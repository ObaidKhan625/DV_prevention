from django import forms
from .models import User, User_Document

class User_Documents_Form(forms.ModelForm):
	class Meta:
		model = User_Document
		fields = ['user_file']

class UpdateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'user_phone', 'user_other', 'email', 'user_description', 'user_profile_image', 'user_address']

	def save(self, commit=True):
		user = super(UpdateUserForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.user_description = self.cleaned_data['user_description']
		user.user_profile_image = self.cleaned_data['user_profile_image']
		print(user.email, user.user_description, user.user_profile_image)

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