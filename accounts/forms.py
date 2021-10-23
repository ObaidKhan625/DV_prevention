from django.forms import ModelForm
from .models import User

class ProfileUpdationForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'phone', 'email', 'other', 'profile_image']