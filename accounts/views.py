from django.shortcuts import render, reverse, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from user_auth.decorators import auth_or_not
from .forms import ProfileUpdationForm
# Create your views here.

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def profileView(request, current_user_id, user_id):
	profile = User.objects.get(username = request.user)
	form = ProfileUpdationForm()
	if request.method == "POST":
		form = ProfileUpdationForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {'profile':profile, 'form':form}
	return render(request, 'accounts/profile.html', context)