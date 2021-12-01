from .forms import UpdateUserForm
from .models import *
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from user_auth.decorators import auth_or_not

# Create your views here.

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def profileView(request, profile_id):
	"""
	View the profile
	"""
	profile = User.objects.get(id = profile_id)
	verifications_count = Verification.objects.filter(verified_user = profile).count()
	user_documents = User_Document.objects.filter(user_name = profile)
	contact_permitted_instances = Contact_Permission.objects.filter(permitted_user = request.user)
	contact_permitted_users = []
	for i in contact_permitted_instances:
		contact_permitted_users.append(i.permitted_user)
	context = {'profile':profile, 'user_documents':user_documents, 'verifications_count':verifications_count,
	'contact_permitted_users':contact_permitted_users}
	return render(request, 'accounts/profile.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def profileEdit(request):
	"""
	Edit Profile
	"""
	profile = User.objects.get(username = request.user)
	form = UpdateUserForm()

	if request.method == "POST":
		form = UpdateUserForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {'profile':profile, 'form':form}
	return render(request, 'accounts/profile_edit_form.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def drop_zone_file(request):
	context = {}
	return render(request, 'accounts/drop-zone.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def file_upload_view(request):
	"""
	Upload Verification files
	"""
	if request.method == "POST":
		my_file = request.FILES.get('file')
		if(str(my_file).endswith('jpg') or str(my_file).endswith('jpeg') or str(my_file).endswith('jfif') or str(my_file).endswith('pjpeg') or str(my_file).endswith('pjp') or str(my_file).endswith('png')):
			user_document = User_Document.objects.create(user_name = request.user, user_file = my_file, 
			user_file_thumbnail = my_file)
		else:
			user_document = User_Document.objects.create(user_name = request.user, user_file = my_file)
		return redirect('/')
	return JsonResponse({'post':'false'})