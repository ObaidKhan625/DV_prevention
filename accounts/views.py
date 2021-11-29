from .forms import UpdateUserForm
from .models import *
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
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

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def verifyUser(request, profile_id):
	"""
	Verify the identity of a User
	"""
	verified_user = User.objects.get(id = profile_id)
	if(Verification.objects.filter(verified_user = verified_user, verified_by = request.user).exists()):
		return JsonResponse({'verification_post':False})
	else:
		Verification.objects.create(verified_user = verified_user, verified_by = request.user)
		return JsonResponse({'verification_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestContactInfo(request, profile_id):
	"""
	Request a User to view their contact info
	"""
	requested_user = User.objects.get(id = profile_id)
	if(Contact_Request.objects.filter(requested_to = requested_user, requested_by = request.user).exists()):
		return JsonResponse({'request_post':False})
	else:
		Contact_Request.objects.create(requested_to = requested_user, requested_by = request.user)
		return JsonResponse({'request_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def showContactRequests(request):
	"""
	See Contact Requests availible for user's profile
	"""
	contact_requests = Contact_Request.objects.filter(requested_to = request.user)
	context = {'contact_requests':contact_requests, 'True':1, 'False':0}
	return render(request, 'accounts/contact_requests.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestContactInfoAction(request, request_id, action):
	"""
	Permit a User to see current user's contact request
	"""
	contact_info_request = Contact_Request.objects.get(id = request_id)
	if(action == 1):
		Contact_Permission.objects.create(permitted_user = contact_info_request.requested_by, 
		permitted_by = request.user)
		Contact_Request.objects.get(id = request_id).delete()
	else:
		Contact_Request.objects.get(id = request_id).delete()
	return redirect('accounts:show-contact-requests')