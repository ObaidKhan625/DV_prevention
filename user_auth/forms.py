from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']