from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_auth.decorators import auth_or_not
from accounts.models import *
from .forms import ComplaintForm
from PIL import Image
from taggit.models import Tag
import random

# Create your views here.

def complaint_detail_components(request, complaint_id):
	"""
	Components regularly needed in context, for keeps code DRY
	"""
	complaint = Complaint.objects.get(id = complaint_id)
	updates = Message.objects.filter(message_type = "update", message_complaint = complaint)
	comments = Message.objects.filter(message_type = "comment", message_complaint = complaint)
	print(request.user, complaint.complaint_filer, request.user == complaint.complaint_filer)
	return {'complaint':complaint, 'updates':updates, 'comments':comments}

def exploreComplaints(request):
	"""
	See availible complaints, shown on user login
	"""
	complaints = Complaint.objects.filter(complaint_status='active')
	context = {'complaints':complaints}
	return render(request, 'complaints/complaints.html', context)

def showComplaintDetail(request, complaint_id):
	"""
	Show detail of a particular compaint
	"""
	context = complaint_detail_components(request, complaint_id)
	return render(request, 'complaints/complaint_detail.html', context)

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def complaintStatus(request, user_id):
	"""
	Extra function to check complaint's status
	"""
	user = User.objects.get(id = user_id)
	complaints = Complaint.objects.filter(complaint_filer = user)
	context = {'user':user, 'complaints':complaints}
	return render(request, 'complaints/previous_complaint.html', context)

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def createComplaint(request, user_id):
	"""
	Create a Complaint
	"""
	user = User.objects.get(id = user_id)
	if request.method == "POST":
		form = ComplaintForm(request.POST, request.FILES)
		if form.is_valid():
			Complaint.objects.filter(complaint_filer = user).delete()
			form.save()
			complaint = Complaint.objects.filter(complaint_filer = None, complaint_status="active")
			complaint.update(complaint_filer = user)
			#Complaint.objects.filter(user=None, status='active').update(user=user)
		return redirect('complaints:explore-complaints')
	else:
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

		context = complaint_detail_components(request, complaint_id)
		return render(request, 'complaints/complaint_detail.html', context)
	else:
		context = complaint_detail_components(request, complaint_id)
		return render(request, 'complaints/complaint_detail.html', context)