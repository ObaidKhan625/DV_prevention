from .forms import ComplaintForm
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify
from user_auth.decorators import auth_or_not
from accounts.models import User
from PIL import Image
from taggit.models import Tag
import random
from django.shortcuts import render, get_object_or_404

# Create your views here.

#Helper Functions
def complaint_detail_components(request, complaint_slug):
	"""
	Components regularly needed in context, for keeping code DRY
	"""
	complaint = Complaint.objects.get(slug = complaint_slug)
	#tag = get_object_or_404(Tag, slug=complaint_slug)
	#print(tag)
	updates = Message.objects.filter(message_type = "update", message_complaint = complaint)
	comments = Message.objects.filter(message_type = "comment", message_complaint = complaint)
	return {'complaint':complaint, 'updates':updates, 'comments':comments}

def exploreComplaints(request):
	"""
	See availible complaints, shown on user login
	"""
	complaints = Complaint.objects.filter(complaint_status='active')
	context = {'complaints':complaints}
	return render(request, 'complaints/complaints.html', context)

def showComplaintDetail(request, complaint_slug):
	"""
	Show detail of a particular complaint
	"""
	context = complaint_detail_components(request, complaint_slug)
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
def createComplaint(request):
	"""
	Create a Complaint
	"""
	user = request.user
	if request.method == "POST":
		form = ComplaintForm(request.POST, request.FILES)
		if form.is_valid():
			#Complaint.objects.filter(complaint_filer = user).delete()
			newpost = form.save(commit=False)
			newpost.slug = slugify(newpost.complaint_title)
			newpost.save()
			# Without this next line the tags won't be saved.
			form.save_m2m()
			complaint = Complaint.objects.filter(complaint_filer = None, complaint_status="active")
			complaint.update(complaint_filer = user)
			#Complaint.objects.filter(user=None, status='active').update(user=user)
		return redirect('complaints:explore-complaints')
	
	form = ComplaintForm()
	context = {'form':form}
	return render(request, 'complaints/create_complaint_page.html', context)

"""
def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Complaint.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)
"""

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