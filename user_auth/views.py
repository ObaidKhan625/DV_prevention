from .decorators import auth_or_not
from .forms import CreateUserForm
from django.shortcuts import render, redirect
from accounts.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.

@auth_or_not(0)
def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user_name = form.cleaned_data.get('username')

			messages.success(request, 'Account was created for ' + user_name)

			return redirect('user_auth:login')
	context = {'form':form}
	return render(request, 'user_auth/register.html', context)

@auth_or_not(0)
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('complaints:explore-complaints')
		else:
			messages.info(request, 'Incorrect Username and Password combination')
	context = {}
	return render(request, 'user_auth/login.html', context)

@auth_or_not(1)
def logoutUser(request):
	logout(request)
	return redirect('user_auth:login')