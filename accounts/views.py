from .forms import ProfileUpdationForm
from .models import User, User_Documents
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from user_auth.decorators import auth_or_not

# Create your views here.

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def profileView(request, current_user_id, user_id = None):
	profile = User.objects.get(username = request.user)
	form = ProfileUpdationForm()
	if request.method == "POST":
		form = ProfileUpdationForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {'profile':profile, 'form':form}
	return render(request, 'accounts/profile.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def drop_zone_file(request):
	context = {}
	return render(request, 'accounts/drop-zone.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def file_upload_view(request):
	if request.method == "POST":
		my_file = request.FILES.get('file')
		print(my_file)
		User_Documents.objects.create(user_name = request.user, user_files = my_file)
		return JsonResponse({'post':'true'})
	return JsonResponse({'post':'false'})