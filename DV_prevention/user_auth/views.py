from .decorators import auth_or_not
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from accounts.models import User
from user_requests.models import Contact_Request, Complaint_Request
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def nullDetails(request):
	if(request.user.user_phone is None or request.user.user_phone == "None"):
		return True
	if(request.user.user_place is None or request.user.user_place == "None"):
		return True
	if(request.user.user_description is None or request.user.user_description == "None"):
		return True

@csrf_protect
@auth_or_not(0)
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user_name = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + user_name)

			return redirect('user_auth:login')
	context = {'form':form}
	return render(request, 'user_auth/register.html', context)

@csrf_protect
@auth_or_not(0)
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if nullDetails(request):
				return redirect('accounts:profile-edit')
			return redirect('complaints:explore-complaints')
		else:
			messages.info(request, 'Incorrect Username and Password combination')
	return render(request, 'user_auth/login.html')

@auth_or_not(1)
def logoutUser(request):
	logout(request)
	return redirect('user_auth:login')