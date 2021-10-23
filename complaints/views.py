from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_auth.decorators import auth_or_not
from accounts.models import *
from .forms import ComplaintForm
from PIL import Image
import random

# Create your views here.

def exploreComplaints(request):
	complaints = Complaint.objects.filter(status='active')
	context = {'complaints':complaints}
	return render(request, 'complaints/complaints.html', context)

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def complaintStatus(request, user_id):
	user = User.objects.get(id = user_id)
	complaints = Complaint.objects.filter(complaint_filer = user)
	context = {'user':user, 'complaints':complaints}
	return render(request, 'complaints/previous_complaint.html', context)

@login_required(login_url='user-auth:login')
@auth_or_not(1)
def createComplaint(request, user_id):
	customer = Customer.objects.get(user=request.user)
	if request.method == "POST":
		form = DonationRequestForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			Complaint.objects.filter(user=None, status='active').update(user=customer)
			donation = Complaint.objects.filter(user=customer, status='active')
			description = donation.values_list('description', flat=True)
			Complaint.objects.filter(user=customer).update(short_description=description[:50])
		return redirect('/login-passed/user-dashboard/'+str(request.user.id))
	else:
		Complaint.objects.filter(user = customer, status='active').update(status = 'closed')
		form = DonationRequestForm()
		context = {'form':form}
		return render(request, 'complaints/create_complaint_page.html', context)