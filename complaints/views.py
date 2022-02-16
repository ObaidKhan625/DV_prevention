from .forms import ComplaintForm
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from user_auth.decorators import auth_or_not
from accounts.models import User
from PIL import Image
from taggit.models import Tag
import random
from django.shortcuts import render, get_object_or_404

# Create your views here.

#Helper Functions
def complaint_detail_components(request, complaint_id):
	"""
	Components regularly needed in context, for keeping code DRY
	"""
	comments = Message.objects.filter(message_type = "comment", message_complaint = complaint)
	total_updates = len(updates)
	total_comments = len(comments)
	investigations = Investigation.objects.filter(investigation_complaint = complaint)
	investigastion_ongoing_by_curr_user = investigations.filter(investigation_in_charge = request.user).exists()
	return {'complaint':complaint, 'updates':updates, 'comments':comments, 'total_updates':total_updates, 
	'total_comments':total_comments, 'current_complaint_link':"http://127.0.0.1:8000/complaints/"+str(complaint.id), 
	'investigations':investigations, 
	'investigastion_ongoing_by_curr_user': investigastion_ongoing_by_curr_user, 'profile':profile}

def exploreComplaints(request, sorting_parameter="upvotes"):
	"""
	See availible complaints, shown on user login
	"""
	complaints = Complaint.objects.filter(complaint_status='active')
	if(sorting_parameter=="name"):
		complaints = sorted(complaints, key = lambda x : x.complaint_name, reverse = True)
	else:
		complaints = sorted(complaints, key = lambda x : x.complaint_upvotes, reverse = True)
	context = {'complaints':complaints}
	return render(request, 'complaints/complaints.html', context)

def showComplaintDetail(request, complaint_id):
	"""
	Show detail of a particular complaint
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
		print('hey', request.POST.get('comment-add'))

		if len(message_content) == 0:
			context = complaint_detail_components(request, complaint_id)
			return render(request, 'complaints/complaint_detail.html', context)
		Message.objects.create(message_user = request.user, message_complaint = complaint, 
		message_type = message_type, message_content = message_content)

	return redirect('complaints:show-complaint-detail', complaint_id = complaint.id)

def investigateComplaint(request, complaint_id):
	complaint = Complaint.objects.get(id = complaint_id)
	if(not Investigation.objects.filter(investigation_complaint = complaint, investigation_in_charge = request.user).exists()):
		Investigation.objects.create(investigation_complaint = complaint, investigation_in_charge = request.user)
	return JsonResponse({'post':True})

def complaintUpvote(request, complaint_id):
	complaint = Complaint.objects.get(id = complaint_id)
	complaint_upvotes_list = complaint.complaint_upvotes_users.split(',')
	print(complaint_upvotes_list)
	for i in complaint_upvotes_list:
		if(i == str(request.user)):
			return JsonResponse({'upvote_post':False})
	complaint.complaint_upvotes += 1
	complaint.complaint_upvotes_users += (str(request.user)+',')
	complaint.save()
	return JsonResponse({'upvote_post':True})

def complaintDownvote(request, complaint_id):
	complaint = Complaint.objects.get(id = complaint_id)
	complaint_downvotes_list = complaint.complaint_downvotes_users.split(',')
	print(complaint_downvotes_list)
	for i in complaint_downvotes_list:
		if(i == str(request.user)):
			return JsonResponse({'upvote_post':False})
	complaint.complaint_upvotes -= 1
	complaint.complaint_downvotes_users += (str(request.user)+',')
	complaint.save()
	return JsonResponse({'downvote_post':True})

