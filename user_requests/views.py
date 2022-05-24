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

from django.contrib.sessions.models import Session
from channels.layers import get_channel_layer
import json
from asgiref.sync import async_to_sync

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestContactInfo(request, profile_id):
	"""
	Request a User to view their contact info
	"""
	requested_user = User.objects.get(id = profile_id)
	if(Contact_Request.objects.filter(requested_user = requested_user, requested_by = request.user).exists()):
		return JsonResponse({'request_post':False})
	
	requested_user.user_notifications += 1
	requested_user.save()
	print(requested_user.user_notifications)

	channel_layer = get_channel_layer()
	# room_name_for_notification = "requests_for_"+str(request.user)

	try:
		async_to_sync(channel_layer.group_send)(
			"notification_requests_for_"+str(requested_user),
			{
				'type': 'send_request_notification',
				'message': json.dumps("Notification")
			}
		)
	except:
		pass
	
	Contact_Request.objects.create(requested_user = requested_user, requested_by = request.user)
	return JsonResponse({'request_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def requestComplaintAction(request, profile_id):
	"""
	Request an activist to look into current user's complaint
	"""
	requested_user = User.objects.get(id = profile_id)
	complaint = Complaint.objects.filter(complaint_filer = request.user)[0]
	if(Complaint_Request.objects.filter(requested_by = request.user, requested_user = requested_user, requested_complaint = complaint).exists()):
		return JsonResponse({'request_post':False})
	
	requested_user.user_notifications += 1
	requested_user.save()

	channel_layer = get_channel_layer()
	# room_name_for_notification = "requests_for_"+str(request.user)

	try:
		async_to_sync(channel_layer.group_send)(
			"notification_requests_for_"+str(requested_user),
			{
				'type': 'send_request_notification',
				'message': json.dumps("Notification")
			}
		)
	except:
		pass
	
	Complaint_Request.objects.create(requested_by = request.user, requested_user = requested_user, requested_complaint = complaint)
	return JsonResponse({'request_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def showContactRequests(request):
	"""
	See Contact Requests availible for user's profile
	"""
	contact_requests = Contact_Request.objects.filter(requested_user = request.user)
	request.user.user_notifications = 0
	request.user.save()
	context = {'contact_requests':contact_requests, 'True':1, 'False':0}
	return render(request, 'user_requests/contact_requests.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def showComplaintRequests(request):
	"""
	See Complaint Requests availible for user's profile
	"""
	complaint_requests_all = Complaint_Request.objects.filter(requested_user = request.user)
	complaints = []
	for i in complaint_requests_all:
		if i.requested_complaint.complaint_status == 'active':
			complaints.append(i.requested_complaint)
	request.user.user_notifications = 0
	request.user.save()
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