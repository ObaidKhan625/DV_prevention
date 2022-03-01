from .models import *
from accounts.models import User
from complaints.models import Complaint
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse, redirect
from user_auth.decorators import auth_or_not
# Create your views here.

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def verifyUser(request, profile_id):
	"""
	Verify the identity of a User
	"""
	verified_user = User.objects.get(id = profile_id)
	if(verified_user == request.user):
		return JsonResponse({'verification_post':False})
	if(Verification.objects.filter(verified_user = verified_user, verified_by = request.user).exists()):
		return JsonResponse({'verification_post':False})
	else:
		Verification.objects.create(verified_user = verified_user, verified_by = request.user)
		return JsonResponse({'verification_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def reportUser(request, profile_id):
	"""
	Report the identity of a User
	"""
	reported_user = User.objects.get(id = profile_id)
	if(reported_user == request.user):
		return JsonResponse({'verification_post':False})
	if(Report.objects.filter(reported_user = reported_user, reported_by = request.user).exists()):
		return JsonResponse({'report_post':False})
	else:
		Report.objects.create(reported_user = reported_user, reported_by = request.user)
		return JsonResponse({'report_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestContactInfo(request, profile_id):
	"""
	Request a User to view their contact info
	"""
	requested_user = User.objects.get(id = profile_id)
	print(requested_user)
	if(Contact_Request.objects.filter(requested_user = requested_user, requested_by = request.user).exists()):
		return JsonResponse({'request_post':False})
	else:
		Contact_Request.objects.create(requested_user = requested_user, requested_by = request.user)
		return JsonResponse({'request_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestComplaint(request, profile_id, complaint_id):
    """
    Request a particular Activist/NGO to look into the complaint
    """
    activist = User.objects.get(id = profile_id)
    complaint = Complaint.objects.get(id = complaint_id)
    complaint_requests = Contact_Request.objects.create(requested_user = activist, requested_by = request.user, 
    complaint = complaint)
    context = {'activist':activist, 'complaint_requests':complaint_requests}
    return render(request, 'user_requests/complaint_requests.html', context)

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
	return redirect('user_requests:show-contact-requests')

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestComplaintInfo(request, profile_id):
	"""
	Request a Activist/NGO to view their contact info
	"""
	requested_user = User.objects.get(id = profile_id)
	if(Contact_Request.objects.filter(requested_user = requested_user, requested_by = request.user).exists()):
		return JsonResponse({'request_post':False})
	else:
		Contact_Request.objects.create(requested_user = requested_user, requested_by = request.user)
		return JsonResponse({'request_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def showContactRequests(request):
	"""
	See Contact Requests availible for user's profile
	"""
	contact_requests = Contact_Request.objects.filter(requested_user = request.user)
	context = {'contact_requests':contact_requests, 'True':1, 'False':0}
	return render(request, 'user_requests/contact_requests.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def showComplaintRequests(request):
	"""
	See Complaint Requests availible for user's profile
	"""
	complaint_requests_all = Complaint_Request.objects.filter(requested_user = request.user)
	print(complaint_requests_all)
	complaints = []
	for i in complaint_requests_all:
		if i.complaint.complaint_status == 'active':
			complaints.append(i.complaint)
	context = {'complaints':complaints, 'complaint_page_title':'Complaint Requests for '+ str(request.user)}
	return render(request, 'complaints/complaints.html', context)

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
	return redirect('user_requests:show-contact-requests')

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestComplaintAction(request, profile_id):
	"""
	Request an activist to look into current user's complaint
	"""
	profile = User.objects.get(id = profile_id)
	complaint = Complaint.objects.filter(complaint_filer = request.user)[0]
	Complaint_Request.objects.get_or_create(requested_by = request.user, requested_user = profile, complaint = complaint)
	return redirect(reverse('accounts:profile-view', kwargs={'profile_slug':profile.slug}))