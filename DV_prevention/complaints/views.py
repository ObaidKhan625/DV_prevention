from .forms import ComplaintForm
from .models import *
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from user_auth.decorators import auth_or_not
from accounts.models import User
from user_requests.models import Complaint_Request
from PIL import Image
from taggit.models import Tag
import random
from django.shortcuts import render, get_object_or_404
import json

# Create your views here.

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def findNearestActivist(request):
	"""
	Pass Complaint and user in context, then find 
	nearest activists from the complaint
	"""
	# complaint = Complaint.objects.get(complaint_filer = request.user)
	users = User.objects.all().exclude(username = request.user).exclude(user_place_geocode = None)
	complaint = Complaint.objects.get(complaint_filer = request.user)
	context = {'users': users, 'complaint': complaint}
	return render(request, 'complaints/nearest_activist_map.html', context)

#Helper Functions
def complaint_detail_components(request, complaint_id):
	"""
	Helper Function, returns components regularly needed in context
	"""
	complaint = Complaint.objects.get(id = complaint_id)
	profile = complaint.complaint_filer
	updates = Message.objects.filter(message_type = "update", message_complaint = complaint)
	comments = Message.objects.filter(message_type = "comment", message_complaint = complaint)
	total_updates = len(updates)
	total_comments = len(comments)
	investigations = Investigation.objects.filter(investigation_complaint = complaint)
	investigastion_ongoing_by_curr_user = False
	if(str(request.user) != "AnonymousUser"):
		investigastion_ongoing_by_curr_user = investigations.filter(investigation_in_charge = request.user).exists()
	complaint_documents = Complaint_Document.objects.filter(complaint_name = complaint)
	complaint_json = complaint.complaint_place_geocode

	return {'complaint':complaint, 'updates':updates, 'comments':comments, 'total_updates':total_updates, 
	'total_comments':total_comments, 'current_complaint_link':"http://127.0.0.1:8000/complaints/"+str(complaint.id), 
	'investigations':investigations, 
	'investigastion_ongoing_by_curr_user': investigastion_ongoing_by_curr_user, 'profile':profile, 
	'complaint_documents':complaint_documents, 'complaint_json': complaint_json}

def exploreComplaints(request, sorting_parameter="upvotes"):
	"""
	See availible complaints, shown on user login
	"""
	# request.session['notifications_for_request_user'] += 1
	# print(request.session['notifications_for_request_user'])
	complaints = Complaint.objects.filter(complaint_status='active')
	if(sorting_parameter=="name"):
		complaints = sorted(complaints, key = lambda x : x.complaint_name, reverse = True)
	else:
		complaints = sorted(complaints, key = lambda x : x.complaint_upvotes, reverse = True)
	context = {'complaints':complaints, 'complaint_page_title': 'Complaints'}
	return render(request, 'complaints/complaints.html', context)

def exploreComplaintsByTag(request, complaint_tag):
	"""
	See availible complaints, shown on user login
	"""
	tag = TagComplaint.objects.get(tag = complaint_tag)
	complaints = []
	for i in tag.tag_complaints['complaints']:
		try:
			complaint = Complaint.objects.get(complaint_title = i, complaint_status = "active")
			complaints.append(complaint)
		except:
			pass
	
	context = {'complaints':complaints, 'complaint_page_title': 'Complaints with tag #'+tag.tag, 'filtered_tag': str(tag)}
	return render(request, 'complaints/complaints.html', context)

def showComplaintDetail(request, complaint_id):
	"""
	Show detail of a particular complaint
	"""
	context = complaint_detail_components(request, complaint_id)
	return render(request, 'complaints/complaint_detail.html', context)

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def createComplaint(request):
	"""
	Create a Complaint
	"""
	user = request.user
	if request.method == "POST":
		form = ComplaintForm(request.POST, request.FILES)
		if form.is_valid():
			# Delete all existing complaints of the user
			Complaint.objects.filter(complaint_filer = user).delete()
			newpost = form.save(commit=False)
			newpost.save()
			# Without this next line the tags won't be saved.
			form.save_m2m()
			complaint = Complaint.objects.filter(complaint_filer = None, complaint_status="active")
			complaint.update(complaint_filer = user)
			
			complaint = Complaint.objects.get(complaint_filer = user)
			for complaint_tag in complaint.tags.all():
				tag = TagComplaint.objects.get_or_create(tag = str(complaint_tag))
				tag[0].tag_complaints['complaints'].append(str(complaint.complaint_title))
				tag[0].save()
			# Complaint.objects.filter(user=None, status='active').update(user=user)
		else:
			print(form.errors)
		return redirect('complaints:explore-complaints')
	
	form = ComplaintForm()
	context = {'form':form}
	return render(request, 'complaints/create_complaint_page.html', context)

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def addMessage(request, complaint_id, message_type):
	"""
	Add comment/update to complaint
	"""
	if request.method == "POST":
		message_content = None
		complaint = Complaint.objects.get(id = complaint_id)
		if message_type == "update":
			message_content = request.POST.get('update-add')
		else:
			message_content = request.POST.get('comment-add')

		if len(message_content) == 0:
			context = complaint_detail_components(request, complaint_id)
			return render(request, 'complaints/complaint_detail.html', context)
		Message.objects.create(message_user = request.user, message_complaint = complaint, 
		message_type = message_type, message_content = message_content)

	return redirect(reverse('complaints:show-complaint-detail', kwargs={'complaint_id': complaint_id}))

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def investigateComplaint(request, complaint_id):
	complaint = Complaint.objects.get(id = complaint_id)
	if(not Investigation.objects.filter(investigation_complaint = complaint, investigation_in_charge = request.user).exists()):
		Investigation.objects.create(investigation_complaint = complaint, investigation_in_charge = request.user)
	if(Complaint_Request.objects.filter(requested_complaint = complaint, requested_by = complaint.complaint_filer, 
	requested_user = request.user).exists()):
		Complaint_Request.objects.filter(requested_complaint = complaint, 
		requested_by = complaint.complaint_filer, requested_user = request.user).delete()
	return JsonResponse({'post':True})

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def complaintUpvote(request, complaint_id):
	complaint = Complaint.objects.get(id = complaint_id)
	complaint_upvotes_list = complaint.complaint_upvotes_users.split(',')
	for i in complaint_upvotes_list:
		if(i == str(request.user)):
			return JsonResponse({'upvote_post':False})
	complaint.complaint_upvotes += 1
	complaint.complaint_upvotes_users += (str(request.user)+',')
	complaint.save()
	return JsonResponse({'upvote_post':True})

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def complaintDownvote(request, complaint_id):
	complaint = Complaint.objects.get(id = complaint_id)
	complaint_downvotes_list = complaint.complaint_downvotes_users.split(',')
	for i in complaint_downvotes_list:
		if(i == str(request.user)):
			return JsonResponse({'upvote_post':False})
	complaint.complaint_upvotes -= 1
	complaint.complaint_downvotes_users += (str(request.user)+',')
	complaint.save()
	return JsonResponse({'downvote_post':True})

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def complaint_drop_zone_file(request):
	context = {}
	return render(request, 'complaints/complaint_drop_zone.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def complaint_file_upload_view(request):
	"""
	Upload Verification files
	"""
	complaint = Complaint.objects.filter(complaint_filer = request.user)[0]
	if request.method == "POST":
		my_file = request.FILES.get('file')
		if(str(my_file).endswith('jpg') or str(my_file).endswith('jpeg') or str(my_file).endswith('jfif') or str(my_file).endswith('pjpeg') or str(my_file).endswith('pjp') or str(my_file).endswith('png')):
			complaint_document = Complaint_Document.objects.create(complaint_name = complaint, complaint_file = my_file)
		else:
			pass
		return redirect('/')
	return JsonResponse({'post':'false'})

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def requestHistory(request):
	if(not Complaint.objects.filter(complaint_filer = request.user).exists()):
		return render(request, 'complaints/no_complaint.html')
	complaint = Complaint.objects.get(complaint_filer = request.user)
	return redirect(reverse('complaints:show-complaint-detail', kwargs={'complaint_id': complaint.id}))

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def markComplaintAsDone(request, complaint_id):
	for i, j in zip(request.POST.items(), range(len(request.POST))):
		if j == 0:
			continue
		activist = User.objects.get(username=i[1])
		activist.user_complaints_solved += 1
		activist.save()
	Complaint.objects.get(id = complaint_id).delete()
	return redirect('complaints:explore-complaints')

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def deleteComplaint(request, complaint_id):
	Complaint.objects.get(id = complaint_id).delete()
	return redirect('complaints:explore-complaints')